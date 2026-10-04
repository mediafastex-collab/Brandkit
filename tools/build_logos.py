"""Builds the Fastex Media logo SVGs and injects them into the brand kit page.

Geometry was measured from the supplied 616x616 master artwork. Every diagonal
runs at 2 units across for 3 units down, the angle used throughout the identity.

Usage: python3 tools/build_logos.py
Needs tools/wordmark.json (outlined Outfit glyphs) next to this script.
"""
import base64
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORANGE, INK, WHITE = "#FF6600", "#0D0D0D", "#FFFFFF"

CHEVRON = "M204 155H264L366 308L264 461H204L306 308Z"
ARMS = "M416 155H476L380.5 298.25L350.5 253.25ZM416 461H476L380.5 317.75L350.5 362.75Z"
# Full-colour bars meet the chevron edge exactly, as in the master artwork.
BARS = "M138 241H261.33L290.67 285H138ZM138 330H291.33L262 374H181V461H138Z"
# One-colour bars step back by the same 21-unit gap the X arms keep, so the F stays legible.
BARS_MONO = "M138 241H240.33L269.67 285H138ZM138 330H270.33L241 374H181V461H138Z"

MARK_BOX = (138, 155, 338, 306)  # tight bounds of the mark


def mark_paths(fg, accent, mono=False):
    bars = BARS_MONO if mono else BARS
    return (f'<path fill="{fg}" d="{bars}"/><path fill="{fg}" d="{ARMS}"/>'
            f'<path fill="{accent}" d="{CHEVRON}"/>')


def svg(viewbox, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" role="img">'
            f'<title>{title}</title>{body}</svg>')


glyphs = json.loads((ROOT / "tools" / "wordmark.json").read_text())


def wordmark(color, scale, x, baseline):
    fastex_d, fastex_w = glyphs["semibold"]["FASTEX"]
    media_d, _ = glyphs["medium"]["MEDIA"]
    media_x = fastex_w + 300  # word space
    return (f'<g fill="{color}" transform="translate({x} {baseline}) scale({scale})">'
            f'<path d="{fastex_d}"/><path transform="translate({media_x} 0)" d="{media_d}"/></g>')


def word_width(scale):
    return (glyphs["semibold"]["FASTEX"][1] + 300 + glyphs["medium"]["MEDIA"][1]) * scale


mx, my, mw, mh = MARK_BOX
tight = f"{mx} {my} {mw} {mh}"


def horizontal(fg):
    s = 122 / 703  # cap height = 40% of mark height
    gap = 90
    w = mw + gap + word_width(s)
    body = (f'<g transform="translate({-mx} {-my})">{mark_paths(fg, ORANGE)}</g>'
            + wordmark(fg, round(s, 5), mw + gap, mh / 2 + 61))
    return svg(f"0 0 {w:.0f} {mh}", body, "Fastex Media")


def stacked(fg):
    s = 0.115
    w = word_width(s)
    cap = 703 * s
    body = (f'<g transform="translate({(w - mw) / 2 - mx:.2f} {-my})">{mark_paths(fg, ORANGE)}</g>'
            + wordmark(fg, s, 0, mh + 70 + cap))
    return svg(f"0 0 {w:.0f} {mh + 70 + cap + 4:.0f}", body, "Fastex Media")


LOGOS = [
    # id, name, use, svg, preview background
    ("fx-mark-primary", "Primary mark", "Default on white and light backgrounds",
     svg(tight, mark_paths(INK, ORANGE), "Fastex Media mark"), "light"),
    ("fx-mark-reversed", "Reversed mark", "On Ink, dark photos and dark UI",
     svg(tight, mark_paths(WHITE, ORANGE), "Fastex Media mark"), "dark"),
    ("fx-mark-black", "One-colour black", "Fax, stamps, single-colour print and engraving",
     svg(tight, mark_paths(INK, INK, mono=True), "Fastex Media mark"), "light"),
    ("fx-mark-white", "One-colour white", "Over Fastex Orange or busy photography",
     svg(tight, mark_paths(WHITE, WHITE, mono=True), "Fastex Media mark"), "orange"),
    ("fx-avatar-dark", "Dark badge", "Profile pictures, app icons, favicons",
     svg("0 0 616 616", f'<circle cx="308" cy="308" r="308" fill="{INK}"/>' + mark_paths(WHITE, ORANGE),
         "Fastex Media badge"), "light"),
    ("fx-avatar-light", "Light tile", "Square avatars where a light tile is needed",
     svg("0 0 616 616", f'<rect width="616" height="616" fill="{WHITE}"/>' + mark_paths(INK, ORANGE),
         "Fastex Media tile"), "dark"),
    ("fx-lockup-horizontal", "Horizontal lockup", "Website header, email signature, decks",
     horizontal(INK), "light"),
    ("fx-lockup-horizontal-reversed", "Horizontal lockup, reversed", "Dark headers, video end cards",
     horizontal(WHITE), "dark"),
    ("fx-lockup-stacked", "Stacked lockup", "Square spaces, event banners, merchandise",
     stacked(INK), "light"),
    ("fx-lockup-stacked-reversed", "Stacked lockup, reversed", "Dark square spaces",
     stacked(WHITE), "dark"),
]

out_dir = ROOT / "assets" / "logos"
out_dir.mkdir(parents=True, exist_ok=True)
for lid, _, _, s, _ in LOGOS:
    (out_dir / f"{lid}.svg").write_text(s)

originals = {}
for name in ("fx-mark-light.png", "fx-mark-dark-badge.png"):
    p = ROOT / "assets" / "original" / name
    if p.exists():
        originals[name] = base64.b64encode(p.read_bytes()).decode()

data = {
    "logos": [dict(id=i, name=n, use=u, svg=s, bg=b) for i, n, u, s, b in LOGOS],
    "originals": originals,
}
blob = "const BRAND_ASSETS = " + json.dumps(data, separators=(",", ":")) + ";"

src = (ROOT / "tools" / "brandkit.src.html").read_text()
import html
prompt = (ROOT / "BRANDKIT_PROMPT.md").read_text()
page = src.replace("/*__BRAND_ASSETS__*/", blob).replace("<!--__PROMPT__-->", html.escape(prompt, quote=False))
(ROOT / "brandkit.html").write_text(page)  # body-only page, published as the Artifact
(ROOT / "index.html").write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    '<link rel="icon" href="assets/logos/fx-avatar-dark.svg">\n</head>\n<body>\n'
    + page + "\n</body>\n</html>\n")
print("wrote", len(LOGOS), "logos;", f"page {len(page) // 1024} KB")
