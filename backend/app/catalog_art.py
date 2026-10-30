"""Eserler için özgün, temsili SVG görseller üretir.

Resmî kapak, afiş veya oyun görseli kullanılmaz. Girdi katalog metnidir;
üretilen her dosyada eser adı, kategori ve esere göre değişen soyut desen vardır.
"""
from hashlib import sha256
from html import escape
from pathlib import Path
import textwrap
import xml.etree.ElementTree as ET

from .catalog_expansion import DATA as EXPANSION

COLORS = {
    "kitap": ("#271e4b", "#7960b5", "#eecf93"),
    "film": ("#302235", "#b45672", "#f6bf73"),
    "dizi": ("#153746", "#3d97a0", "#f2d2a8"),
    "oyun": ("#203e34", "#67a67b", "#e8ce7e"),
}


def _records():
    from .catalog import DATA
    for category, block in DATA.items():
        lines = block.splitlines() + EXPANSION.get(category, "").splitlines()
        for number, line in enumerate(lines, 1):
            title, genres, themes, moods, *_ = line.split("|", 4)
            yield category, number, title, genres, themes, moods


def svg(category, title, genre, themes, moods):
    base, accent, light = COLORS[category]
    digest = sha256((category + "|" + title).encode("utf-8")).digest()
    circles = []
    for index in range(11):
        x = 45 + digest[index] * 2.1
        y = 55 + digest[index + 11] * 3.0
        radius = 12 + digest[index + 21] % 65
        opacity = .10 + digest[index + 4] % 19 / 100
        circles.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{light}" opacity="{opacity:.2f}"/>')
    lines = []
    for index, part in enumerate(textwrap.wrap(title, width=20, break_long_words=False, break_on_hyphens=False)[:4]):
        lines.append(f'<text x="50" y="{475 + index * 63}" class="title">{escape(part)}</text>')
    subtitle = escape((themes.split(",")[0] + " · " + moods.split(",")[0]).upper())
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="900" viewBox="0 0 640 900" role="img" aria-label="{escape(title, quote=True)} için özgün temsili görsel">
<title>{escape(title)} — Öneri Atlası temsili görseli</title>
<desc>Resmî kapak veya afiş değildir. Öneri Atlası için özgün olarak üretilmiş soyut tipografik görsel. Lisans: proje içi kullanım.</desc>
<defs><linearGradient id="ground" x2="1" y2="1"><stop stop-color="{base}"/><stop offset="1" stop-color="{accent}"/></linearGradient></defs>
<rect width="640" height="900" fill="url(#ground)"/>
{''.join(circles)}
<path d="M-30 310 Q220 160 670 290 M-30 350 Q310 190 670 370" fill="none" stroke="{light}" opacity=".35" stroke-width="3"/>
<rect x="34" y="340" width="572" height="430" rx="20" fill="{base}" opacity=".84"/>
<text x="50" y="392" font-family="sans-serif" font-size="23" fill="{light}" letter-spacing="3">{escape(category.upper())} · {escape(genre.upper())}</text>
<style>.title{{font: bold 49px Georgia,serif;fill:#fff}}</style>
{''.join(lines)}
<text x="50" y="810" font-family="sans-serif" font-size="18" fill="{light}" letter-spacing="2">{subtitle}</text>
<text x="50" y="858" font-family="sans-serif" font-size="16" fill="#fff" opacity=".7">ÖNERİ ATLASI · TEMSİLİ GÖRSEL</text>
</svg>'''


def generate(root=None):
    target = Path(root) if root else Path(__file__).resolve().parents[2] / "frontend" / "public" / "art"
    target.mkdir(parents=True, exist_ok=True)
    paths = []
    for category, number, title, genre, themes, moods in _records():
        path = target / f"{category}-{number}.svg"
        document = svg(category, title, genre, themes, moods)
        ET.fromstring(document)
        path.write_text(document, encoding="utf-8")
        paths.append(path)
    return paths


if __name__ == "__main__":
    print(f"{len(generate())} temsili SVG üretildi.")
