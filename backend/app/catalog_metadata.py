"""Katalog etiketlerinden tempo ve öneri hedef kitlesi üretir.

Hedef kitle bir yaş sınıflandırması değildir; keşif arayüzü için geniş bir etikettir.
"""


def editorial_metadata(category: str, genres: list[str], themes: list[str], moods: list[str]) -> tuple[str, str]:
    genre = set(genres)
    theme = set(themes)
    mood = set(moods)
    if "gerilimli" in mood or genre.intersection({"aksiyon", "gerilim", "korku", "hayatta kalma"}):
        pace = "hızlı"
    elif "sakin" in mood and not genre.intersection({"aksiyon", "gerilim"}):
        pace = "sakin"
    else:
        pace = "orta"

    if genre.intersection({"korku", "gerilim", "distopya"}) or theme.intersection({"şiddet", "savaş", "suç"}):
        audience = "yetişkin"
    elif genre.intersection({"masal", "animasyon"}) or (category == "oyun" and genre.intersection({"simülasyon", "bulmaca", "platform"}) and "karanlık" not in mood):
        audience = "genel"
    else:
        audience = "genç ve yetişkin"
    return pace, audience
