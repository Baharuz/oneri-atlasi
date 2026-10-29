from collections import defaultdict

LABELS = {"siyasi entrika":"siyasi entrika", "ayrıntılı evren":"ayrıntılı evren"}

def recommend(contents, sources, answers, profile=None, feedback=None):
    """Weighted tag overlap with bounded novelty. Scores are ranking signals, not probabilities."""
    profile = profile or {}
    feedback = feedback or {}
    weights = defaultdict(float)
    source_ids = {item.id for item in sources}
    for item in sources:
        for tag in item.themes: weights[("theme", tag)] += 2
        for tag in item.moods: weights[("mood", tag)] += 1.5
        # Genres are only useful within their own category.
        for tag in item.genres: weights[("genre", item.category, tag)] += 1
    for tag in profile.get("features", []): weights[("theme", tag)] += 1.5
    for tag in profile.get("moods", []): weights[("mood", tag)] += 1
    for tag in answers.get("features", []): weights[("theme", tag)] += 5
    for tag in answers.get("moods", []): weights[("mood", tag)] += 3
    mode = answers.get("mode", "close")
    target = answers.get("categories") or ["kitap", "film", "dizi", "oyun"]
    by_category = {}
    for category in target:
        scored = []
        for item in contents:
            if item.category != category or item.id in source_ids or feedback.get(item.id) == "dislike": continue
            matches = []
            score = 0.0
            for tag in item.themes:
                value = weights[("theme", tag)]
                if value: score += value; matches.append((value, tag))
            for tag in item.moods:
                value = weights[("mood", tag)]
                if value: score += value; matches.append((value, tag))
            for tag in item.genres:
                value = weights[("genre", category, tag)]
                if value: score += value; matches.append((value, tag))
            if not matches: continue
            if feedback.get(item.id) == "like": score += 2
            if mode == "surprise": score += min(2, len(set(item.themes) - set(answers.get("features", []))))
            elif mode == "discover": score += min(1, len(set(item.themes) - set(answers.get("features", []))))
            matches.sort(reverse=True)
            reason = " ve ".join(tag for _, tag in matches[:2]) + " tercihlerinle örtüştüğü için önerildi."
            scored.append((score, item, reason))
        scored.sort(key=lambda row: (-row[0], row[1].title))
        if mode in ("discover", "surprise"):
            selected, used = [], set()
            while scored and len(selected) < 8:
                best = max(scored, key=lambda row: row[0] - (1.5 if mode == "discover" else 3) * len(used.intersection(row[1].themes + row[1].moods)))
                selected.append(best); used.update(best[1].themes + best[1].moods); scored.remove(best)
            scored = selected
        by_category[category] = [{"content": item, "score": round(score, 2), "reason": reason} for score, item, reason in scored[:8]]
    return by_category
