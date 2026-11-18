"""Builds the Fastex Media logo SVGs and injects them into the brand kit page.

Geometry was measured from the supplied 616x616 master artwork. Every diagonal
runs at 2 units across for 3 units down, the angle used throughout the identity.

Usage: python3 tools/build_logos.py
Needs tools/wordmark.json ("FASTEX MEDIA" outlined in Inter 700, 0.025em tracking).
Optional: resvg_py, to render the cropped-mark PNGs (kept on disk once rendered).
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
    return (f'<g fill="{color}" transform="translate({x:.2f} {baseline:.2f}) scale({scale:.5f})">'
            f'<path d="{glyphs["d"]}"/></g>')


mx, my, mw, mh = MARK_BOX
tight = f"{mx} {my} {mw} {mh}"
CAP = glyphs["capHeight"] / glyphs["upm"]  # cap height per unit of font size


def horizontal(fg):
    # Social/ads spec: 62 px mark, 32 px Inter 700 wordmark, 20 px gap, centred vertically.
    size = mh * 32 / 62
    s = size / glyphs["upm"]
    gap = mh * 20 / 62
    w = mw + gap + glyphs["width"] * s
    body = (f'<g transform="translate({-mx} {-my})">{mark_paths(fg, ORANGE)}</g>'
            + wordmark(fg, s, mw + gap, mh / 2 + CAP * size / 2))
    return svg(f"0 0 {w:.0f} {mh}", body, "Fastex Media")


def stacked(fg):
    w = mw * 2.6
    s = w / glyphs["width"]
    cap = CAP * s * glyphs["upm"]
    body = (f'<g transform="translate({(w - mw) / 2 - mx:.2f} {-my})">{mark_paths(fg, ORANGE)}</g>'
            + wordmark(fg, s, 0, mh + 70 + cap))
    return svg(f"0 0 {w:.0f} {mh + 70 + cap + 2:.0f}", body, "Fastex Media")


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

# Cropped marks for social posts and ads: the FX glyph only, no disc, no padding.
CROPPED = {
    "FX-mark-cropped-for-light-bg": svg(tight, mark_paths(INK, ORANGE), "Fastex Media mark"),
    "FX-mark-cropped-for-dark-bg": svg(tight, mark_paths(WHITE, ORANGE), "Fastex Media mark"),
}
cropped = {}
for name, sv in CROPPED.items():
    (out_dir / f"{name}.svg").write_text(sv)
    png = out_dir / f"{name}.png"
    try:
        import resvg_py
        h = 620  # 10x the 62 px spec on a 1080 x 1350 post
        w = round(h * mw / mh)
        data = bytes(resvg_py.svg_to_bytes(svg_string=sv.replace("<svg ", f'<svg width="{w}" height="{h}" ', 1)))
        png.write_bytes(data)
    except ImportError:
        pass
    if png.exists():
        cropped[f"{name}.png"] = base64.b64encode(png.read_bytes()).decode()
    cropped[f"{name}.svg"] = sv

originals = {}
for name in ("fx-mark-light.png", "fx-mark-dark-badge.png"):
    p = ROOT / "assets" / "original" / name
    if p.exists():
        originals[name] = base64.b64encode(p.read_bytes()).decode()

docs = {}
for name in ("Master_Social_Media_Canvas_Sizes.docx",):
    p = ROOT / name
    if p.exists():
        docs[name] = base64.b64encode(p.read_bytes()).decode()

data = {
    "cropped": cropped,
    "docs": docs,
    "logos": [dict(id=i, name=n, use=u, svg=s, bg=b) for i, n, u, s, b in LOGOS],
    "originals": originals,
}
blob = "const BRAND_ASSETS = " + json.dumps(data, separators=(",", ":")) + ";"

src = (ROOT / "tools" / "brandkit.src.html").read_text()
import html
prompt = (ROOT / "BRANDKIT_PROMPT.md").read_text()
page = src.replace("/*__BRAND_ASSETS__*/", blob).replace("<!--__PROMPT__-->", html.escape(prompt, quote=False)).replace("<!--__RULES__-->", html.escape((ROOT / "Brand-Design-Rules-Variable-Template.md").read_text(), quote=False))
(ROOT / "brandkit.html").write_text(page)  # body-only page, published as the Artifact
(ROOT / "index.html").write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    '<link rel="icon" href="assets/logos/fx-avatar-dark.svg">\n</head>\n<body>\n'
    + page + "\n</body>\n</html>\n")
print("wrote", len(LOGOS), "logos;", f"page {len(page) // 1024} KB")
