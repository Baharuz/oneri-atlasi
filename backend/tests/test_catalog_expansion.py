from app.catalog import DATA as CURRENT
from app.catalog_expansion import DATA as EXPANSION
from app.catalog_art import generate
import xml.etree.ElementTree as ET


def test_expansion_has_unique_curated_entries():
    for category in ("kitap", "film", "dizi"):
        old_titles = {line.split("|")[0].casefold().strip() for line in CURRENT[category].splitlines()}
        rows = [line.split("|") for line in EXPANSION[category].splitlines()]
        titles = [row[0].casefold().strip() for row in rows]
        assert len(rows) == len(set(titles)) == 100
        assert not old_titles.intersection(titles)
        for row in rows:
            assert len(row) == 5
            title, genre, themes, moods, description = row
            assert title and genre and themes and moods
            assert len(description) >= 60
            assert " temalarını " not in description


def test_generated_art_is_unique_and_parseable(tmp_path):
    paths = generate(tmp_path)
    assert len(paths) == len(set(path.name for path in paths)) == 400
    assert len(set(path.read_bytes() for path in paths)) == 400
    for path in paths:
        root = ET.parse(path).getroot()
        assert root.tag.endswith("svg")
        assert "temsili görsel" in root.attrib["aria-label"]
