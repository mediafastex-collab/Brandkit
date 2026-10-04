"""Builds the Canva-importable files in canva/ from the brand kit content.

canva/brand-guidelines.html   full guidelines deck (1920x1080 pages)
canva/templates/*.html        one editable social / ad template per file, at real size

Usage: python3 tools/build_canva.py
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "canva"
LOGOS = ROOT / "assets" / "logos"
E = html.escape


def logo(name, w=None, h=None):
    s = (LOGOS / f"{name}.svg").read_text()
    s = re.sub(r"<title>.*?</title>", "", s)
    attrs = (f' width="{w}"' if w else "") + (f' height="{h}"' if h else "")
    return s.replace("<svg ", f"<svg{attrs} ", 1)


FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Inter:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap">'
CSS = """
body{margin:0;background:#E9E7E3;font-family:Inter,Arial,sans-serif;color:#0D0D0D}
.page{width:1920px;height:1080px;position:relative;overflow:hidden;background:#FBFAF8;margin:0 auto 40px;box-sizing:border-box;padding:100px 130px}
.dark{background:#0D0D0D;color:#FFFFFF}
.orange{background:#FF6600;color:#0D0D0D}
h1,h2,h3,h4{font-family:Outfit,Arial,sans-serif;font-weight:600;margin:0;letter-spacing:-0.02em}
h1{font-size:150px;line-height:0.95}
h2{font-size:76px;line-height:1.02}
h3{font-size:36px;line-height:1.15}
h4{font-size:30px;line-height:1.2}
p{margin:0;font-size:26px;line-height:1.5}
.eyebrow{font-size:21px;letter-spacing:0.14em;text-transform:uppercase;color:#63636B;font-weight:500}
.dark .eyebrow{color:#9C9A95}
.muted{color:#63636B}
.dark .muted{color:#B5B3AE}
.row{display:flex;gap:44px}
.col{flex:1}
.rule{width:96px;height:6px;background:#FF6600;margin:24px 0 34px}
.foot{position:absolute;left:130px;right:130px;bottom:54px;display:flex;justify-content:space-between;font-size:20px;color:#63636B}
.dark .foot{color:#8E8C87}
.box{background:#FFFFFF;border:2px solid #E6E3DE;border-radius:26px;padding:36px}
.dark .box{background:#17171A;border-color:#2A2A2E}
.soft{background:#F3F1ED;border:0}
.good{background:#E8F4EC;border:0}
.bad{background:#FBEBEC;border:0}
.big{font-family:Outfit,Arial,sans-serif;font-weight:600;font-size:116px;line-height:1;letter-spacing:-0.04em}
ul{margin:0;padding-left:32px;font-size:25px;line-height:1.5}
li{margin-bottom:10px}
.tag{display:inline-block;font-size:19px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;padding:8px 16px;border-radius:100px}
.ok{background:#E8F4EC;color:#1D7A4C}
.no{background:#FBEBEC;color:#B4232C}
.band{position:absolute;top:-100px;bottom:-100px;width:150px;background:#FF6600;transform:skewX(33.69deg)}
table{border-collapse:collapse;width:100%;font-size:23px}
th,td{text-align:left;padding:16px 18px;border-bottom:2px solid #E6E3DE;vertical-align:top}
.dark th,.dark td{border-color:#2A2A2E}
th{font-size:17px;letter-spacing:0.1em;text-transform:uppercase;color:#63636B;font-weight:500}
.pill{display:inline-block;border-radius:100px;padding:16px 30px;font-weight:600;font-size:24px;border:2px solid #0D0D0D}
.mono{font-family:'DM Mono',monospace}
.chev{display:inline-block;width:18px;height:24px;background:#FF6600;clip-path:polygon(0 0,40% 0,100% 50%,40% 100%,0 100%,60% 50%);margin-right:14px}
"""


def page(label, body, cls="", eyebrow=None, title=None, foot=None):
    head = ""
    if eyebrow:
        head += f'<p class="eyebrow">{eyebrow}</p><div class="rule"></div>'
    if title:
        head += f"<h2>{title}</h2>"
    f = f'<div class="foot">{foot}</div>' if foot else ""
    return f'<section class="page {cls}" data-document-role="page" data-label="{E(label)}">{head}{body}{f}</section>\n'


def section_divider(num, name, sub):
    return page(name, f"""
  <div class="band" style="left:1250px"></div><div class="band" style="left:1480px;opacity:0.25"></div>
  <p class="eyebrow" style="margin-top:260px">Section {num}</p>
  <h1 style="margin-top:24px">{name}</h1>
  <p class="muted" style="margin-top:30px;max-width:980px;font-size:30px">{sub}</p>""", cls="dark")


def table(head, rows, style=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table style="{style}"><tr>{th}</tr>{trs}</table>'


def dd(do_title, do_items, dont_title, dont_items, style=""):
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    return f"""<div class="row" style="{style}">
  <div class="col box good"><span class="tag ok">{do_title}</span><ul style="margin-top:20px">{li(do_items)}</ul></div>
  <div class="col box bad"><span class="tag no">{dont_title}</span><ul style="margin-top:20px">{li(dont_items)}</ul></div></div>"""


P = []

# ------------------------------------------------------------------ cover + contents
P.append(page("Cover", f"""
  <div class="band" style="left:1180px;opacity:0.9"></div><div class="band" style="left:1420px;opacity:0.25"></div>
  {logo('fx-mark-reversed', 250, 226)}
  <p class="eyebrow" style="margin-top:140px">Fastex Media · Brand guidelines v1.0 · 4 Oct 2026</p>
  <h1 style="margin-top:24px">One brand,<br>built to book meetings.</h1>
  <p class="muted" style="margin-top:34px;max-width:1000px">The logo, the way we sound and the way we market. Use this kit so every post, ad, email and deck looks and reads like Fastex Media.</p>""", cls="dark"))

P.append(page("Contents", """
  <div class="row" style="margin-top:20px">
    <div class="col"><h3>1 · Overview</h3><p class="muted">At a glance, main factors, positioning, purpose, proof, method, who we serve</p>
      <h3 style="margin-top:40px">2 · Logo</h3><p class="muted">All 10 versions, anatomy, clear space, minimum size, backgrounds, misuse</p>
      <h3 style="margin-top:40px">3 · Voice &amp; Tone</h3><p class="muted">Personality, five traits, we are / we are not, tone by context, quick rules, vocabulary, style rules, before and after</p></div>
    <div class="col"><h3>4 · Design</h3><p class="muted">Palette, proportion, contrast, typefaces, type scale, type rules, the 56° cut, elements, imagery, layout grid</p>
      <h3 style="margin-top:40px">5 · Marketing</h3><p class="muted">Strategy: messaging house, industries, funnel, outreach, case studies, checklist. Social media. Ads.</p>
      <h3 style="margin-top:40px">6 · Resources</h3><p class="muted">Files and the master prompt</p></div>
  </div>""", eyebrow="Contents"))

# ------------------------------------------------------------------ 1 overview
P.append(section_divider(1, "Overview", "Who we are, what we promise and the three things that matter most."))

P.append(page("At a glance", f"""
  <div class="row" style="margin-top:30px;gap:30px">
    <div class="col box"><div style="width:120px;height:120px;border-radius:60px;background:#FF6600"></div><h3 style="margin-top:30px">Fastex Orange</h3><p class="muted">#FF6600</p></div>
    <div class="col box"><div style="width:120px;height:120px;border-radius:60px;background:#0D0D0D"></div><h3 style="margin-top:30px">Ink</h3><p class="muted">#0D0D0D</p></div>
    <div class="col box"><div style="height:120px;font:600 96px/120px Outfit,Arial,sans-serif">Aa</div><h3 style="margin-top:30px">Outfit + Inter</h3><p class="muted">Google Fonts</p></div>
    <div class="col box"><div style="width:34px;height:120px;background:#FF6600;transform:skewX(33.69deg);margin-left:40px"></div><h3 style="margin-top:30px">The 56° cut</h3><p class="muted">One angle everywhere</p></div>
  </div>
  <h3 style="margin-top:70px">The three things that matter most</h3>
  <div class="row" style="margin-top:24px">
    <div class="col"><h4>Logo</h4><p class="muted">10 official files, with clear space, minimum sizes and what not to do.</p></div>
    <div class="col"><h4>Brand voice</h4><p class="muted">Our personality in words: five traits, words to use and avoid, and before-and-after rewrites.</p></div>
    <div class="col"><h4>Marketing tone</h4><p class="muted">How the voice shifts across the website, LinkedIn, cold email, WhatsApp, ads and sales.</p></div>
  </div>""", eyebrow="Overview", title="At a glance"))

P.append(page("Positioning", """
  <h2 style="max-width:1500px;margin-top:10px">We build outbound systems that put qualified B2B meetings on your sales calendar. Every week.</h2>
  <div class="box soft" style="margin-top:64px"><p>For <b>B2B companies in IT, solar, manufacturing, education and real estate</b> who need a predictable pipeline, <b>Fastex Media</b> is the lead generation partner that builds a multi-channel outbound system across LinkedIn, cold email, WhatsApp and paid media, and measures it on one number: <b>qualified meetings booked</b>. Unlike agencies that report impressions and clicks, we already know who signs in your industry.</p></div>""",
                eyebrow="Overview · Positioning"))

P.append(page("Purpose, promise, personality", """
  <div class="row" style="margin-top:40px">
    <div class="col"><p class="eyebrow">Purpose</p><h3 style="margin-top:16px">Help good businesses get discovered by the buyers who should know them.</h3><p class="muted" style="margin-top:20px">Owners have put years into their product. Our job is to put it in front of the right decision-makers.</p></div>
    <div class="col"><p class="eyebrow">Promise</p><h3 style="margin-top:16px">Qualified meetings, not vanity metrics.</h3><p class="muted" style="margin-top:20px">We report on meetings booked and pipeline created. Likes and impressions are inputs, never the result.</p></div>
    <div class="col"><p class="eyebrow">Personality</p><h3 style="margin-top:16px">The operator in the room.</h3><p class="muted" style="margin-top:20px">Calm, specific and sure of the system. The person who already has the numbers when everyone else has opinions.</p></div>
  </div>""", eyebrow="Overview", title="Purpose, promise, personality"))

P.append(page("Proof points", """
  <div class="row" style="margin-top:90px;border-top:2px solid #E6E3DE;border-bottom:2px solid #E6E3DE;padding:50px 0">
    <div class="col"><div class="big">13+</div><p class="muted">Active client brands</p></div>
    <div class="col"><div class="big">3X</div><p class="muted">Average lead growth</p></div>
    <div class="col"><div class="big">60%</div><p class="muted">Average reduction in cost per lead</p></div>
    <div class="col"><div class="big">4.9★</div><p class="muted">Client satisfaction, out of 5</p></div>
  </div>
  <p class="muted" style="margin-top:40px">Figures as published on fastexmedia.com. Re-check them every quarter, and always describe them as averages across client accounts (see the claims rules in Ads).</p>""",
                eyebrow="Overview", title="Proof points"))

P.append(page("Method", """
  <div class="row" style="margin-top:100px">
    <div class="col" style="border-top:4px solid #FF6600;padding-top:30px"><p style="color:#FF6600;font-size:22px">Move 1</p><h3 style="margin-top:12px">Map the market</h3><p class="muted" style="margin-top:14px">Define the accounts worth winning and build a verified dataset of the decision-makers inside them.</p></div>
    <div class="col" style="border-top:4px solid #FF6600;padding-top:30px"><p style="color:#FF6600;font-size:22px">Move 2</p><h3 style="margin-top:12px">Build the system</h3><p class="muted" style="margin-top:14px">Multi-channel sequences across LinkedIn, email, WhatsApp and paid, with personalisation built in.</p></div>
    <div class="col" style="border-top:4px solid #FF6600;padding-top:30px"><p style="color:#FF6600;font-size:22px">Move 3</p><h3 style="margin-top:12px">Scale what converts</h3><p class="muted" style="margin-top:14px">Track replies and meetings by channel, then move budget and effort to what works.</p></div>
  </div>""", cls="dark", eyebrow="Overview · Method", title="Three moves. One machine."))

P.append(page("Who we serve", """
  <div class="row" style="margin-top:40px"><div class="col"><h4>Primary buyer</h4><p class="muted" style="margin-top:10px">Founders, CEOs, sales heads and marketing heads at B2B companies with an average deal size that justifies outbound. They are busy and sceptical, and have been burned by agencies that reported clicks.</p></div>
    <div class="col"><h4>Core industries</h4><p class="muted" style="margin-top:10px">IT &amp; Software · Solar &amp; Renewable Energy · Manufacturing · Educational Institutes · Real Estate. Industry depth is a selling point: we already know who signs.</p></div></div>
  <div class="row" style="margin-top:50px"><div class="col"><h4>Services</h4><p class="muted" style="margin-top:10px">Performance Marketing · LinkedIn Lead Generation · Cold Email Marketing · WhatsApp Marketing · Social Media Marketing · Lead Research · Appointment Setting.</p></div>
    <div class="col"><h4>Lines in use</h4><p class="muted" style="margin-top:10px">Tagline: "Your brand. Your next chapter."<br>Sign-off: "Engineered for B2B scale."<br>Main CTA: "Book a Free Strategy Call".</p></div></div>""",
                eyebrow="Overview", title="Who we serve"))

# ------------------------------------------------------------------ 2 logo
P.append(section_divider(2, "Logo", "Two letters doing one job: the F holds steady and the orange chevron drives forward through the X. Always use the official files and never redraw the mark."))

VERS = [("fx-mark-primary", "Primary mark", "Default on white and light backgrounds", "#FBFAF8"),
        ("fx-mark-reversed", "Reversed mark", "On Ink, dark photos and dark UI", "#0D0D0D"),
        ("fx-mark-black", "One-colour black", "Single-colour print, stamps, engraving", "#FBFAF8"),
        ("fx-mark-white", "One-colour white", "Over Fastex Orange or busy photography", "#FF6600"),
        ("fx-avatar-dark", "Dark badge", "Profile pictures, app icons, favicons", "#FBFAF8"),
        ("fx-avatar-light", "Light tile", "Square avatars where a light tile is needed", "#0D0D0D")]
LOCK = [("fx-lockup-horizontal", "Horizontal lockup", "Website header, email signature, decks", "#FBFAF8"),
        ("fx-lockup-horizontal-reversed", "Horizontal lockup, reversed", "Dark headers, video end cards", "#0D0D0D"),
        ("fx-lockup-stacked", "Stacked lockup", "Square spaces, event banners, merchandise", "#FBFAF8"),
        ("fx-lockup-stacked-reversed", "Stacked lockup, reversed", "Dark square spaces", "#0D0D0D")]


def logo_card(lid, name, use, bg, size):
    w, h = size
    return (f'<div style="flex:1"><div style="height:{h + 80}px;background:{bg};border:2px solid #E6E3DE;border-radius:22px;'
            f'display:flex;align-items:center;justify-content:center">{logo(lid, w, h)}</div>'
            f'<h4 style="margin-top:16px;font-size:26px">{name}</h4><p class="muted" style="font-size:21px">{use}</p></div>')


P.append(page("Logo versions: marks", '<div class="row" style="gap:26px;margin-top:20px">' +
              "".join(logo_card(*v, (150, 136) if "mark" in v[0] else (150, 150)) for v in VERS[:3]) +
              '</div><div class="row" style="gap:26px;margin-top:30px">' +
              "".join(logo_card(*v, (150, 136) if "mark" in v[0] else (150, 150)) for v in VERS[3:]) + "</div>",
              eyebrow="Logo · Versions 1–6",
              foot="<span>All files are in the Fastex Media Brand Kit folder in Canva, and at mediafastex-collab.github.io/Brandkit</span>"))
P.append(page("Logo versions: lockups", '<div class="row" style="gap:26px;margin-top:20px">' +
              "".join(logo_card(*v, (600, 105)) for v in LOCK[:2]) +
              '</div><div class="row" style="gap:26px;margin-top:30px">' +
              "".join(logo_card(*v, (380, 200)) for v in LOCK[2:]) + "</div>",
              eyebrow="Logo · Versions 7–10",
              foot="<span>Use SVG for print and web, PNG for slides and social.</span>"))

ANAT = """<svg viewBox="40 120 900 380" width="1500" height="633" xmlns="http://www.w3.org/2000/svg">
<path fill="#0D0D0D" d="M138 241H261.33L290.67 285H138ZM138 330H291.33L262 374H181V461H138Z"/><path fill="#0D0D0D" d="M416 155H476L380.5 298.25L350.5 253.25ZM416 461H476L380.5 317.75L350.5 362.75Z"/><path fill="#FF6600" d="M204 155H264L366 308L264 461H204L306 308Z"/>
<g stroke="#63636B" stroke-width="2" fill="none"><path d="M160 263V140H560"/><path d="M330 230H560"/><path d="M440 420H560"/><path d="M360 300L560 320"/></g>
<g font-family="Inter,Arial,sans-serif" font-size="22" fill="#0D0D0D" font-weight="500"><text x="572" y="147">F bars: the stable foundation</text><text x="572" y="226">Chevron: forward motion</text><text x="572" y="416">X arms: reach into the market</text><text x="572" y="316">The gap between chevron and X</text></g>
<g font-family="Inter,Arial,sans-serif" font-size="18" fill="#63636B"><text x="572" y="252">Always Fastex Orange #FF6600</text><text x="572" y="342">Never close it or fill it</text><text x="700" y="470">every diagonal, one angle</text></g>
<text x="572" y="470" font-family="DM Mono,monospace" font-size="24" fill="#C94A00">2 : 3 → 56.3°</text></svg>"""
P.append(page("Anatomy", f'<div style="margin-top:0">{ANAT}</div>', eyebrow="Logo · Construction", title="Anatomy"))

CLEAR = """<svg viewBox="40 55 538 506" width="640" height="602" xmlns="http://www.w3.org/2000/svg">
<rect x="78" y="95" width="458" height="426" fill="none" stroke="#C94A00" stroke-width="2.5" stroke-dasharray="10 8"/>
<path fill="#0D0D0D" d="M138 241H261.33L290.67 285H138ZM138 330H291.33L262 374H181V461H138Z"/><path fill="#0D0D0D" d="M416 155H476L380.5 298.25L350.5 253.25ZM416 461H476L380.5 317.75L350.5 362.75Z"/><path fill="#FF6600" d="M204 155H264L366 308L264 461H204L306 308Z"/>
<g stroke="#63636B" stroke-width="2"><path d="M204 140H264M204 132V148M264 132V148M78 308H138M476 308H536M307 461V521"/></g>
<g font-family="DM Mono,monospace" font-size="24" fill="#C94A00"><text x="226" y="128">x</text><text x="100" y="298">x</text><text x="498" y="298">x</text><text x="318" y="500">x</text></g></svg>"""
P.append(page("Clear space and minimum size", f"""
  <div class="row" style="align-items:flex-start">
    <div style="width:680px">{CLEAR}</div>
    <div class="col">
      <h3>Clear space</h3><p class="muted" style="margin-top:12px"><b style="color:#0D0D0D">x</b> is the width of the chevron stroke. Keep at least <b style="color:#0D0D0D">1x</b> clear on every side of the mark, and <b style="color:#0D0D0D">1.5x</b> around lockups. No text, edges or other logos inside this area.</p>
      <h3 style="margin-top:50px">Minimum size</h3>
      <div class="row" style="align-items:flex-end;margin-top:20px;gap:50px">
        <div>{logo('fx-mark-primary', 48, 43)}<p style="font-size:21px;margin-top:10px"><b>24 px · 8 mm</b><br><span class="muted">Mark</span></p></div>
        <div>{logo('fx-avatar-dark', 56, 56)}<p style="font-size:21px;margin-top:10px"><b>32 px</b><br><span class="muted">Badge, favicon</span></p></div>
        <div>{logo('fx-lockup-horizontal', 280, 49)}<p style="font-size:21px;margin-top:10px"><b>140 px · 35 mm</b><br><span class="muted">Horizontal lockup</span></p></div>
      </div>
      <p class="muted" style="margin-top:30px">Below these sizes the gap between the chevron and the X closes up. For favicons and app icons under 32 px, use the dark badge.</p>
    </div>
  </div>""", eyebrow="Logo · Construction"))


def tile(bg, inner, cap, verdict=None):
    v = f'<span class="tag {"ok" if verdict else "no"}" style="margin-right:12px">{"Yes" if verdict else "No"}</span>' if verdict is not None else '<span style="color:#B4232C;font-weight:700;margin-right:10px">✕</span>'
    return (f'<div style="flex:1"><div style="height:300px;background:{bg};border:2px solid #E6E3DE;border-radius:20px;display:flex;align-items:center;justify-content:center;overflow:hidden">{inner}</div>'
            f'<p style="font-size:22px;margin-top:14px">{v}{cap}</p></div>')


P.append(page("Backgrounds", '<div class="row" style="gap:26px;margin-top:40px">' +
              tile("#FBFAF8", logo("fx-mark-primary", 170, 154), "Paper or white: primary mark", True) +
              tile("#0D0D0D", logo("fx-mark-reversed", 170, 154), "Ink or dark photo: reversed mark", True) +
              tile("#FF6600", logo("fx-mark-black", 170, 154), "Orange: one-colour black", True) +
              tile("linear-gradient(135deg,#7a7f88,#c9b9a6 45%,#3d4450)", logo("fx-mark-primary", 170, 154), "Busy or mid-tone photo: add a dark overlay first", False) +
              "</div>", eyebrow="Logo · Usage", title="Backgrounds"))


def mk(style="", ch="#FF6600"):
    return (f'<svg viewBox="138 155 338 306" width="170" height="154" style="{style}" xmlns="http://www.w3.org/2000/svg"><path fill="#0D0D0D" d="M138 241H261.33L290.67 285H138ZM138 330H291.33L262 374H181V461H138Z"/>'
            f'<path fill="#0D0D0D" d="M416 155H476L380.5 298.25L350.5 253.25ZM416 461H476L380.5 317.75L350.5 362.75Z"/><path fill="{ch}" d="M204 155H264L366 308L264 461H204L306 308Z"/></svg>')


P.append(page("Misuse", '<div class="row" style="gap:26px;margin-top:30px">' +
              tile("#FBFAF8", mk("transform:scaleX(1.55)"), "Don't stretch or squash it") +
              tile("#FBFAF8", mk("transform:rotate(-18deg)"), "Don't rotate it") +
              tile("#FBFAF8", mk("", "#2B6BFF"), "Don't recolour the chevron") +
              '</div><div class="row" style="gap:26px;margin-top:30px">' +
              tile("#FBFAF8", mk("filter:drop-shadow(6px 8px 0 rgba(255,102,0,.45))"), "Don't add shadows, glows or outlines") +
              tile("#FBFAF8", mk("transform:scaleX(-1)"), "Don't flip the chevron backwards") +
              tile("#C94A00", mk(), "Don't place it on low-contrast colour") +
              "</div>", eyebrow="Logo · Usage · Misuse"))

# ------------------------------------------------------------------ 3 voice & tone
P.append(section_divider(3, "Voice &amp; Tone", "Our voice is our personality in words and it stays the same everywhere. The tone shifts with the context."))

P.append(page("Personality", f"""
  <div class="box" style="margin-top:60px;display:flex;gap:50px;align-items:center;padding:60px">{logo('fx-mark-reversed', 200, 181)}
  <div><h2 style="font-size:72px">The operator in the room.</h2><p class="muted" style="margin-top:20px">Calm, specific and sure of the system. Has the numbers when everyone else has opinions, and respects what the client has built.</p></div></div>""",
                cls="dark", eyebrow="Brand voice · Personality"))

TRAITS = [("Direct", "Lead with the outcome. Give the number, the timeline and the next step. Cut anything a busy founder would skip.", "We book meetings with plant heads. Worth 15 minutes on Thursday?"),
          ("Proof-first", "Every claim travels with a figure, a client type or a method. If we can't prove it, we don't say it.", "60% lower cost per lead, averaged across client accounts."),
          ("Calm confidence", "Certainty comes from the system, not from adjectives. No hype, no exclamation marks, no \"revolutionary\".", "Three moves. One machine."),
          ("Industry-fluent", "Use the buyer's own words: EPC, OEM, admissions cycle, channel partners. Show we understand their market before we pitch.", "Admissions teams don't need more enquiries in May. They need them in January."),
          ("Human", "Respect what the client has built. Write like a sharp colleague, in plain English, with short sentences.", "You've put a lot into building your business. Let's help more people discover it.")]
P.append(page("Five voice traits", table(["Trait", "What it means", "Sounds like"],
              [(f"<b>{t}</b>", d, f'<span style="font-family:Outfit,Arial,sans-serif">"{q}"</span>') for t, d, q in TRAITS],
              "margin-top:30px;font-size:22px"), eyebrow="Brand voice", title="Five voice traits"))

P.append(page("We are / we are not", table(["We are", "We are not", "Why it matters"], [
    ("<b>Confident</b>", "Cocky", "Buyers trust the agency with a system, not the loudest one."),
    ("<b>Specific</b>", "Technical for show", '"Reply rate" is useful. "Omnichannel synergy" is noise.'),
    ("<b>Warm</b>", "Chummy", 'No "Hey buddy!" in a first message to a CEO.'),
    ("<b>Ambitious</b>", "Hyped", "We promise a machine that compounds, not overnight 10X."),
    ("<b>Honest</b>", "Defensive", "When a channel underperforms, we say so first and explain the fix.")], "margin-top:40px;font-size:26px"),
    eyebrow="Brand voice", title="We are / we are not"))

TONE = [("Website", [55, 65, 75, 35], "You've put a lot into building your business. Let's help more people discover it.", "Confident and welcoming. Lead with the outcome, back it with a number, end with one clear CTA."),
        ("LinkedIn", [40, 55, 80, 45], "Most B2B pipelines don't have a lead problem. They have a follow-up problem.", "Opinionated and useful. Take a clear position, then share the playbook. Write as a practitioner, not a brand."),
        ("Cold email", [35, 60, 40, 20], "Saw you're adding rooftop solar for factories in Gujarat. We book meetings with plant heads for EPCs like yours. Worth 15 minutes next week?", "Brief and personal. Under 90 words, about them rather than us, one ask."),
        ("WhatsApp", [20, 45, 35, 10], "Hi Priya, thanks for reaching out. Here's the case study you asked for. Want me to hold Thursday 11am for a quick call?", "Friendly and quick. Use first names and short lines, and always suggest the next step."),
        ("Ads", [35, 50, 90, 20], "Your sales calendar, full. Qualified B2B meetings, every week.", "Bold and spare. One promise, one proof point, one action, readable in a single glance."),
        ("Sales &amp; proposals", [65, 70, 60, 60], "In the first 14 days we map your market. From week 3 you get one number every Friday: meetings booked.", "Assured and precise. Show the method, the timeline and the reporting."),
        ("Client reporting", [70, 80, 30, 70], "This week: 9 meetings booked, 2 more than last week. LinkedIn drove 6, so we're moving budget from Meta to LinkedIn on Monday.", "Factual and calm. Start with the headline number, then the reason, then what changes next."),
        ("When things go wrong", [60, 90, 20, 40], "Reply rates dropped because a sending domain was flagged. We've paused it, moved volume to two warmed domains and expect recovery by Wednesday.", "Own it first. Say what happened, what we've done and when it will be fixed.")]
AXES = [("Casual", "Formal"), ("Playful", "Serious"), ("Reserved", "Bold"), ("Simple", "Technical")]


def dial(vals):
    out = ""
    for (a, b), v in zip(AXES, vals):
        out += (f'<div style="margin-bottom:16px"><div style="display:flex;justify-content:space-between;font-size:17px;color:#63636B"><span>{a}</span><span>{b}</span></div>'
                f'<div style="position:relative;height:8px;border-radius:8px;background:#E6E3DE;margin-top:8px"><div style="position:absolute;left:calc({v}% - 11px);top:-7px;width:22px;height:22px;border-radius:11px;background:#FF6600"></div></div></div>')
    return out


def tone_card(name, vals, sample, note):
    return (f'<div class="box" style="flex:1;padding:30px"><h4>{name}</h4><div style="margin-top:18px">{dial(vals)}</div>'
            f'<p style="font-family:Outfit,Arial,sans-serif;font-size:22px;line-height:1.35;border-left:4px solid #FF6600;padding-left:14px;margin-top:10px">"{sample}"</p>'
            f'<p class="muted" style="font-size:19px;margin-top:12px">{note}</p></div>')


for i in (0, 4):
    P.append(page(f"Marketing tone {i // 4 + 1}", '<div class="row" style="gap:22px;align-items:stretch">' +
                  "".join(tone_card(*t) for t in TONE[i:i + 4]) + "</div>",
                  eyebrow=f"Marketing tone · Tone by context ({i // 4 + 1} of 2)"))

P.append(page("Tone quick rules", """
  <div class="row" style="margin-top:60px">
    <div class="col box"><h3>Never shout</h3><p class="muted" style="margin-top:14px">No exclamation marks, all-caps sentences or "AMAZING". Ads get bolder through fewer words, not louder ones.</p></div>
    <div class="col box"><h3>Always one next step</h3><p class="muted" style="margin-top:14px">Every message ends with a single clear action: a call, a reply or a link. Never three.</p></div>
    <div class="col box"><h3>Bad news first</h3><p class="muted" style="margin-top:14px">When something goes wrong, say what happened before anything else, then the fix and the date.</p></div>
  </div>""", eyebrow="Marketing tone", title="Quick rules"))

P.append(page("Vocabulary", dd("Say", ["qualified meetings · booked · pipeline", "decision-makers · verified data", "system · sequence · reply rate", "cost per lead · sales calendar", "accounts · scale what converts"],
                               "Avoid", ["guaranteed results · leads galore · viral", "growth hacking · synergy · 10X overnight", "cheap leads · blast", "best agency in India · cutting-edge", "solutions · !!!"], "margin-top:30px"),
              eyebrow="Writing style", title="Vocabulary"))

P.append(page("Style rules", """
  <div class="row" style="margin-top:40px"><div class="col"><h4>Name</h4><p class="muted" style="margin-top:10px">Always <b style="color:#0D0D0D">Fastex Media</b>: two words, capital F and M. "Fastex" is fine on second mention. Never FastEx, FASTEX MEDIA in running text, Fastex media or FM.</p></div>
    <div class="col"><h4>Numbers</h4><p class="muted" style="margin-top:10px">Always use numerals: 3 channels, 15 minutes. Multipliers take a capital X with no space (3X). Percentages take the symbol (60%). Currency comes first: ₹50,000 or $2,500.</p></div></div>
  <div class="row" style="margin-top:50px"><div class="col"><h4>Headlines</h4><p class="muted" style="margin-top:10px">Sentence case, 8 words or fewer and no full stop, unless it's one of the short punchy lines like "Three moves. One machine."</p></div>
    <div class="col"><h4>Spelling and dates</h4><p class="muted" style="margin-top:10px">US English spelling (optimize, color) in public copy. Write dates as 4 Oct 2026. Use the Oxford comma. Use emoji only on Instagram and WhatsApp, and never more than one.</p></div></div>""",
                eyebrow="Writing style", title="Style rules"))

RW = [("We are a leading full-service digital marketing agency offering innovative, cutting-edge solutions for all your business needs!", "We build outbound systems that book qualified B2B meetings, and we report on one number: meetings booked."),
      ("Get unlimited leads guaranteed with our amazing LinkedIn growth hacks!", "We research the decision-makers in your market, reach them on LinkedIn and book the call for you."),
      ("Hi Sir, hope you are doing well. We are Fastex Media and we provide many services. Kindly check our website.", "Saw you're adding rooftop solar for factories in Gujarat. We book meetings with plant heads for EPCs like yours. Open to a 15-minute call next week?")]
P.append(page("Before and after", "".join(
    f'<div class="row" style="margin-top:22px;gap:0;border:2px solid #E6E3DE;border-radius:20px;background:#fff"><div class="col" style="padding:24px 28px;border-right:2px solid #E6E3DE"><span class="tag no">Before</span><p class="muted" style="margin-top:12px;font-size:23px;text-decoration:line-through">{b}</p></div>'
    f'<div class="col" style="padding:24px 28px"><span class="tag ok">After</span><p style="margin-top:12px;font-size:23px;font-weight:500">{a}</p></div></div>' for b, a in RW),
    eyebrow="Writing style", title="Before and after"))

# ------------------------------------------------------------------ 4 design
P.append(section_divider(4, "Design", "Mostly paper and ink, with orange used sparingly so it stays a signal. Two typefaces and one angle, taken from the mark."))

SW = [("Fastex Orange", "#FF6600", "255 102 0", "0 60 100 0", "Pantone ≈ 1505 C", "Logo chevron, highlights, primary buttons", "#0D0D0D", 2),
      ("Ink", "#0D0D0D", "13 13 13", "0 0 0 95", "", "Text, logo, dark backgrounds", "#FFFFFF", 1),
      ("Paper", "#FBFAF8", "251 250 248", "0 0 1 2", "", "Default page background", "#0D0D0D", 1),
      ("Ember", "#C94A00", "201 74 0", "0 63 100 21", "", "Links and small orange text on light", "#FFFFFF", 1),
      ("Slate", "#63636B", "99 99 107", "7 7 0 58", "", "Secondary text, captions", "#FFFFFF", 1)]
P.append(page("Palette", '<div class="row" style="gap:20px;height:640px;margin-top:10px">' + "".join(
    f'<div style="flex:{fl};background:{hx};color:{fg};border-radius:26px;padding:30px;display:flex;flex-direction:column;justify-content:flex-end;{"border:2px solid #E6E3DE;" if hx == "#FBFAF8" else ""}">'
    f'<h3>{n}</h3><p style="font-size:20px;margin-top:8px;opacity:.85">{role}</p><p class="mono" style="font-size:20px;margin-top:14px">HEX {hx}<br>RGB {rgb}<br>CMYK {cmyk}{"<br>" + pan if pan else ""}</p></div>'
    for n, hx, rgb, cmyk, pan, role, fg, fl in SW) + "</div>", eyebrow="Design · Colour", title="Palette"))

PAIRS = [("#0D0D0D", "#FBFAF8", "Ink on Paper", "Body text, headlines", "18.6:1", "AAA"),
         ("#FFFFFF", "#0D0D0D", "White on Ink", "Reversed text, dark sections", "19.4:1", "AAA"),
         ("#0D0D0D", "#FF6600", "Ink on Orange", "Buttons, badges, carousel covers", "6.6:1", "AA"),
         ("#FF6600", "#0D0D0D", "Orange on Ink", "Stats and highlights on dark", "6.6:1", "AA"),
         ("#63636B", "#FBFAF8", "Slate on Paper", "Captions and secondary text", "5.7:1", "AA"),
         ("#C94A00", "#FBFAF8", "Ember on Paper", "Links and small accent text", "4.5:1", "AA"),
         ("#FFFFFF", "#FF6600", "White on Orange", "Not allowed for text", "2.9:1", "Fail"),
         ("#FF6600", "#FBFAF8", "Orange on Paper", "Graphics and the logo only, never text", "2.8:1", "Fail")]
P.append(page("Proportion and contrast", f"""
  <div style="display:flex;height:70px;border-radius:14px;overflow:hidden;border:2px solid #E6E3DE">
    <div style="flex:58;background:#FBFAF8;padding:18px;font-size:19px">Paper &amp; white 58%</div><div style="flex:30;background:#0D0D0D;color:#fff;padding:18px;font-size:19px">Ink 30%</div>
    <div style="flex:8;background:#FF6600;padding:18px;font-size:19px">Orange 8%</div><div style="flex:4;background:#63636B;color:#fff;padding:18px;font-size:19px">4%</div></div>
  <p class="muted" style="font-size:21px;margin-top:10px">Orange should cover less than about a tenth of any layout. If everything is orange, nothing stands out.</p>
  <div class="row" style="margin-top:30px;gap:30px;flex-wrap:wrap">""" + "".join(
    f'<div style="width:390px;display:flex;gap:16px;align-items:center"><div style="width:90px;height:64px;border-radius:12px;background:{bg};color:{fg};border:2px solid #E6E3DE;display:flex;align-items:center;justify-content:center;font:600 28px Outfit,Arial,sans-serif">Aa</div>'
    f'<div><p style="font-size:21px"><b>{n}</b> · <span class="mono">{r}</span> <span class="tag {"no" if v == "Fail" else "ok"}" style="font-size:14px;padding:4px 10px">{v}</span></p><p class="muted" style="font-size:18px">{u}</p></div></div>'
    for fg, bg, n, u, r, v in PAIRS) + "</div>" +
    dd("Do", ["Ink text on Fastex Orange for buttons and badges (6.6:1).", "Ember for links and small accent text on light backgrounds."],
       "Don't", ["White text on Fastex Orange (2.9:1 fails).", "Orange body text on paper or white (2.8:1)."], "margin-top:30px"),
    eyebrow="Design · Colour · WCAG 2.1"))

P.append(page("Typefaces", """
  <div class="row" style="margin-top:10px">
    <div class="col box"><p class="eyebrow">Display · Outfit</p><div class="big" style="font-size:190px;margin-top:16px">Aa 3X</div><p class="muted" style="font-family:Outfit,Arial,sans-serif;font-size:24px;margin-top:10px">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789 ₹$%★</p><p class="muted" style="margin-top:16px;font-size:21px">Medium 500, SemiBold 600 (default), Bold 700 for big stats only. Headlines, stats, social buttons and the wordmark.</p></div>
    <div class="col box"><p class="eyebrow">Body · Inter</p><div style="font-family:Inter,Arial,sans-serif;font-weight:500;font-size:190px;line-height:1;margin-top:16px">Aa</div><p style="font-size:24px;margin-top:10px">We map the market, build the system and scale what converts.</p><p class="muted" style="margin-top:16px;font-size:21px">Regular 400, Medium 500, SemiBold 600. Body copy, UI, captions, emails and decks.</p></div>
  </div>""", eyebrow="Design · Typography", foot="<span>Both free at fonts.google.com</span>"))

SCALE = [("Display", "64/1.0 · 600 · −3%", "font:600 84px/1 Outfit,Arial,sans-serif;letter-spacing:-0.03em", "Your calendar, full."),
         ("H1", "48/1.05 · 600 · −2%", "font:600 64px/1.05 Outfit,Arial,sans-serif;letter-spacing:-0.02em", "Three moves. One machine."),
         ("H2", "32/1.15 · 600 · −1.5%", "font:600 46px/1.15 Outfit,Arial,sans-serif", "Map the market"),
         ("H3", "22/1.25 · 600", "font:600 34px/1.25 Outfit,Arial,sans-serif", "Verified decision-maker data"),
         ("Body L", "18/1.6 · 400", "font-size:28px", "We build outbound systems that book qualified B2B meetings."),
         ("Body", "16/1.6 · 400", "font-size:24px", "Every channel reports on one number: meetings booked."),
         ("Label", "12/1.2 · 500 · +12% caps", "font-size:20px;letter-spacing:0.12em;text-transform:uppercase;font-weight:500", "Client result · Solar EPC")]
P.append(page("Type scale", "".join(
    f'<div style="display:flex;gap:30px;align-items:baseline;padding:12px 0;border-bottom:2px solid #E6E3DE"><div class="mono muted" style="width:300px;font-size:18px">{n}<br>{m}</div><div style="{st}">{t}</div></div>'
    for n, m, st, t in SCALE), eyebrow="Design · Typography · Web, base 16 px"))

P.append(page("Type rules", """
  <div class="row" style="margin-top:60px">
    <div class="col box"><h3>Tight on top, open below</h3><p class="muted" style="margin-top:14px">Track headlines −1.5% to −3% and set body text at 1.6 line height. Keep body lines to about 65 characters.</p></div>
    <div class="col box"><h3>Stats are the hero</h3><p class="muted" style="margin-top:14px">Set numbers in Outfit SemiBold or Bold, tabular, large and in orange on Ink. Put the label underneath in Inter.</p></div>
    <div class="col box"><h3>Fallbacks</h3><p class="muted" style="margin-top:14px">If Outfit and Inter can't load (Word, Gmail, PowerPoint), use Arial. Never use Times or Comic Sans, and never mix in a third typeface.</p></div>
  </div>""", eyebrow="Design · Typography", title="Rules"))

P.append(page("The 56° cut", """
  <div class="row" style="align-items:center;margin-top:20px">
    <div style="width:800px;height:520px;background:#0D0D0D;border-radius:26px;position:relative;overflow:hidden"><div style="position:absolute;top:-40px;bottom:-40px;left:330px;width:110px;background:#FF6600;transform:skewX(33.69deg)"></div><div style="position:absolute;top:-40px;bottom:-40px;left:500px;width:110px;background:#FF6600;opacity:.35;transform:skewX(33.69deg)"></div><p class="mono" style="position:absolute;right:30px;top:24px;color:#FF6600;font-size:40px">56.3°</p><p style="position:absolute;left:30px;bottom:24px;color:#fff;font-size:22px">The Fastex cut: 2 across, 3 down</p></div>
    <div class="col"><p>Every diagonal in the mark leans 2 units across for every 3 down. Use that same angle for image crops, colour bands, section dividers and motion paths. Never use 45°.</p><p class="muted" style="margin-top:24px">In CSS: <span class="mono">transform: skewX(33.69deg)</span><br>In Canva, Figma or Illustrator: rotate 33.69° from vertical.</p></div>
  </div>""", eyebrow="Design · Graphic language", title="The 56° cut"))

ICONS = ['<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M9 15l2 2 4-4"/>', '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
         '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>', '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>']
icons = "".join(f'<svg viewBox="0 0 24 24" width="64" height="64" fill="none" stroke="{"#C94A00" if i == 0 else "#0D0D0D"}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:22px">{d}</svg>' for i, d in enumerate(ICONS))
P.append(page("Elements", f"""
  <div class="row" style="margin-top:30px">
    <div class="col box"><h3>Chevron marker</h3><p class="muted" style="margin-top:10px">Use the chevron in place of bullets and arrows. Always point it forward.</p><p style="margin-top:24px"><span class="chev"></span>Map the market<br><span class="chev"></span>Build the system<br><span class="chev"></span>Scale what converts</p></div>
    <div class="col box"><h3>Buttons</h3><p class="muted" style="margin-top:10px">Pill shape, fully rounded. One primary button per screen.</p><div style="margin-top:24px;display:flex;flex-direction:column;gap:14px;align-items:flex-start"><span class="pill" style="background:#FF6600;border-color:#FF6600">Book a Free Strategy Call</span><span class="pill" style="background:#0D0D0D;color:#fff">See case studies</span><span class="pill">View service →</span></div></div>
    <div class="col box"><h3>Icons</h3><p class="muted" style="margin-top:10px">2 px line icons on a 24 px grid, rounded caps, in Ink. Ember for at most one icon per set.</p><div style="margin-top:30px">{icons}</div></div>
  </div>""", eyebrow="Design · Graphic language", title="Elements"))

P.append(page("Imagery", dd("Use", ["Real people at work: sales teams, founders, site visits, factory floors and campuses from our five industries.", "Real product evidence: dashboards, calendars and reply screens with private data blurred.", "Warm, natural light. 60 to 75% Ink overlay when text sits on top.", "Crops along the 56° cut."],
                            "Avoid", ["Stock handshakes, people pointing at screens, glowing brains and rocket ships.", "Images recoloured orange. Orange belongs to graphics, not photos.", "Busy backgrounds behind the logo.", "Images of results that we can't back up."], "margin-top:30px"),
              eyebrow="Design · Graphic language", title="Imagery"))

P.append(page("Layout grid", """
  <div class="row" style="margin-top:60px">
    <div class="col box"><h3>8 px spacing</h3><p class="muted" style="margin-top:14px">All spacing in steps of 8 px: 8, 16, 24, 32, 48, 64, 96. On social, use 6 to 9% of the width as the outer margin.</p></div>
    <div class="col box"><h3>12 columns</h3><p class="muted" style="margin-top:14px">Web: 12 columns, 24 px gutter, 1200 px max width. Decks use the same grid at 1920 × 1080.</p></div>
    <div class="col box"><h3>Corners</h3><p class="muted" style="margin-top:14px">Buttons and tags are pills. Cards use 16 px corners, photos 12 px. Don't mix corner styles on one surface.</p></div>
  </div>""", eyebrow="Design · Graphic language", title="Layout grid"))

# ------------------------------------------------------------------ 5 marketing
P.append(section_divider(5, "Marketing", "What we say to whom, on which channel, and how we measure it. Strategy first, then social media and ads, which each have their own rules."))

P.append(page("Messaging house", """
  <div style="background:#0D0D0D;color:#fff;border-radius:24px;padding:36px 44px;margin-top:10px"><p class="eyebrow" style="color:#9C9A95">Brand promise</p><h3 style="font-size:52px;margin-top:10px">Qualified meetings on your sales calendar. Every week.</h3></div>
  <div class="row" style="gap:20px;margin-top:20px">
    <div class="col box"><h4>Market mapped</h4><p class="muted" style="font-size:22px;margin-top:8px">We define the accounts and verify every decision-maker before outreach.</p></div>
    <div class="col box"><h4>Multi-channel system</h4><p class="muted" style="font-size:22px;margin-top:8px">LinkedIn, cold email, WhatsApp and paid, working as one sequence.</p></div>
    <div class="col box"><h4>Measured on meetings</h4><p class="muted" style="font-size:22px;margin-top:8px">One number in every report: qualified meetings booked.</p></div>
    <div class="col box"><h4>Industry depth</h4><p class="muted" style="font-size:22px;margin-top:8px">Five sectors we know well. We already know who signs.</p></div>
  </div>
  <div style="background:#FFF1E7;border-radius:20px;padding:22px 30px;margin-top:20px"><p><b>Proof:</b> 13+ active brands · 3X average lead growth · 60% average CPL reduction · 4.9★ client satisfaction</p></div>""",
                eyebrow="Marketing · Strategy", title="Messaging house"))

P.append(page("Industry messaging", table(["Industry", "Who signs", "Their pain", "Our message", "Lead channel"], [
    ("<b>IT &amp; Software</b>", "Founder, VP Sales, CRO", "SDR time lost to research; long sales cycles", '"Your SDRs sell. We fill their calendar."', "LinkedIn + cold email"),
    ("<b>Solar &amp; Renewable</b>", "EPC owner, BD head", "Commercial rooftop buyers are hard to reach", '"Meetings with plant heads, not tyre-kickers."', "LinkedIn + WhatsApp"),
    ("<b>Manufacturing</b>", "MD, export manager", "Relies on trade fairs and referrals", '"A trade fair\'s worth of buyer meetings, every month."', "Cold email + LinkedIn"),
    ("<b>Education</b>", "Director, admissions head", "Enquiries arrive too late in the cycle", '"Fill next year\'s intake before the rush."', "Meta + WhatsApp"),
    ("<b>Real Estate</b>", "Developer, sales head", "Low-quality portal leads, slow follow-up", '"Qualified site visits, followed up in minutes."', "Meta + Google + WhatsApp")], "margin-top:30px;font-size:22px"),
    eyebrow="Marketing · Strategy", title="Industry messaging"))

FUN = [("Reach", "Ads, LinkedIn content, cold email first touch", "Cost per 1,000 · ICP match"), ("Engage", "Replies, comments, profile visits, clicks", "Reply rate · CTR"),
       ("Converse", "Positive replies, WhatsApp chats, form fills", "Positive reply rate · CPL"), ("Meet", "Qualified meeting booked and held", "Cost per meeting · show rate"),
       ("Pipeline", "Opportunity created in the client's CRM", "Pipeline value · win rate")]
P.append(page("Funnel and KPIs", "".join(
    f'<div style="display:flex;gap:30px;align-items:center;background:#fff;border:2px solid #E6E3DE;border-radius:18px;padding:20px 30px;margin-top:14px;margin-left:{i * 40}px"><h4 style="width:220px">{a}</h4><p style="flex:1;font-size:23px">{b}</p><p class="mono" style="color:#C94A00;font-size:20px;width:380px">{c}</p></div>'
    for i, (a, b, c) in enumerate(FUN)), eyebrow="Marketing · Strategy", title="Funnel and KPIs",
    foot="<span>The headline number in every report is qualified meetings booked. Everything else explains it.</span>"))

P.append(page("Cold email and WhatsApp", """
  <div class="row" style="margin-top:10px;gap:30px">
    <div class="col box" style="padding:0;overflow:hidden"><div style="padding:18px 26px;border-bottom:2px solid #E6E3DE;font-size:20px"><span class="muted">Subject</span><br><b>plant heads in vapi</b></div>
      <div style="padding:22px 26px;font-size:21px;line-height:1.5">Hi Rakesh,<br><br>Saw Sunrise EPC just finished a 2 MW rooftop for a textile unit in Vapi. Nice project.<br><br>We book meetings with plant heads at factories with high power bills, so EPCs like yours spend time quoting instead of prospecting.<br><br>Open to a 15-minute call on Thursday?<br><br>Aagam<br><span class="muted">Fastex Media · fastexmedia.com</span></div></div>
    <div class="col" style="background:#E7DDD3;border-radius:26px;padding:26px;display:flex;flex-direction:column;gap:14px">
      <div style="background:#fff;border-radius:14px;padding:14px 18px;font-size:21px;max-width:80%">Hi, saw your ad. How does the LinkedIn lead gen work?</div>
      <div style="background:#D9FDD3;border-radius:14px;padding:14px 18px;font-size:21px;max-width:85%;align-self:flex-end">Hi Priya, thanks for asking. We research the decision-makers you want, reach them on LinkedIn and book the call for you. Here's a 2-minute case study from an IT services client.</div>
      <div style="background:#D9FDD3;border-radius:14px;padding:14px 18px;font-size:21px;align-self:flex-end">Want me to hold Thursday 11am for a quick call?</div>
      <div style="align-self:flex-end;display:flex;gap:10px"><span style="background:#fff;color:#0A7CFF;border-radius:100px;padding:10px 20px;font-size:19px">Yes, book it</span><span style="background:#fff;color:#0A7CFF;border-radius:100px;padding:10px 20px;font-size:19px">Another time</span></div></div>
    <div class="col"><ul style="font-size:22px"><li><b>Email:</b> plain text, under 90 words, one ask, no attachments on the first touch. Lowercase subject of 2 to 4 words.</li><li><b>Email:</b> open with something real about them. Never "Hope you are doing well."</li><li><b>WhatsApp:</b> opted-in contacts only, approved templates. Reply within 5 minutes in business hours.</li><li><b>WhatsApp:</b> 3 short lines or fewer per message. Quick-reply buttons for the next step.</li></ul></div>
  </div>""", eyebrow="Marketing · Strategy · Outreach", foot="<span>Names and companies are examples only.</span>"))

P.append(page("Case study format", """
  <div class="row" style="margin-top:60px;gap:24px">
    <div class="col box"><p class="eyebrow">Client</p><p style="margin-top:14px">Industry, size and market, plus a logo if approved.</p></div>
    <div class="col box"><p class="eyebrow">Challenge</p><p style="margin-top:14px">One sentence in the client's words.</p></div>
    <div class="col box"><p class="eyebrow">System</p><p style="margin-top:14px">Channels, data and sequence: the three moves.</p></div>
    <div class="col box"><p class="eyebrow">Result</p><p style="margin-top:14px">Meetings, CPL and pipeline over a stated time period, with a quote.</p></div>
  </div>""", eyebrow="Marketing · Strategy", title="Case study format"))

# social
P.append(page("Social: post templates", """
  <div class="row" style="margin-top:20px;gap:30px;align-items:flex-start">
    <div style="width:380px"><div style="width:380px;height:380px;background:#0D0D0D;color:#fff;border-radius:16px;padding:34px;box-sizing:border-box;position:relative"><p style="font-size:14px;letter-spacing:.12em;color:#A9A7A2">CLIENT RESULT · AVERAGE</p><div class="big" style="font-size:144px;color:#FF6600;margin-top:30px">60%</div><p style="font-family:Outfit,Arial,sans-serif;font-size:26px;font-weight:500;margin-top:8px">lower cost per lead across client accounts</p></div><h4 style="font-size:24px;margin-top:14px">Stat post · 1:1</h4><p class="muted" style="font-size:19px">One number, one line, Ink background. For proof.</p></div>
    <div style="width:330px"><div style="width:330px;height:412px;background:#FBFAF8;border:2px solid #E6E3DE;border-radius:16px;padding:32px;box-sizing:border-box"><div style="width:30px;height:42px;background:#FF6600;clip-path:polygon(0 0,40% 0,100% 50%,40% 100%,0 100%,60% 50%)"></div><p style="font-family:Outfit,Arial,sans-serif;font-size:29px;font-weight:500;line-height:1.15;margin-top:26px">"Fastex Media built a lead system that fills our sales calendar every week."</p><p class="muted" style="font-size:15px;margin-top:24px">Fastex Media client · B2B services</p></div><h4 style="font-size:24px;margin-top:14px">Testimonial · 4:5</h4><p class="muted" style="font-size:19px">Real quotes only, approved in writing.</p></div>
    <div style="width:330px"><div style="width:330px;height:412px;background:#FF6600;border-radius:16px;padding:32px;box-sizing:border-box"><p class="mono" style="font-size:15px">01 / 07</p><p style="font-family:Outfit,Arial,sans-serif;font-size:46px;font-weight:600;line-height:0.95;margin-top:80px">Three moves. One machine.</p><p style="font-size:16px;margin-top:20px">How we book qualified B2B meetings, step by step.</p></div><h4 style="font-size:24px;margin-top:14px">Carousel cover · 4:5</h4><p class="muted" style="font-size:19px">Orange cover, black one-colour mark. Ink inside, 5–9 slides.</p></div>
    <div style="width:232px"><div style="width:232px;height:412px;background:#0D0D0D;color:#fff;border-radius:16px;padding:26px;box-sizing:border-box;position:relative;overflow:hidden"><div style="position:absolute;top:-20px;bottom:-20px;right:-14px;width:70px;background:#FF6600;transform:skewX(33.69deg)"></div><p style="position:relative;font-family:Outfit,Arial,sans-serif;font-size:30px;font-weight:600;line-height:1;margin-top:150px;max-width:150px">Your sales calendar, full.</p><p style="position:absolute;left:20px;right:20px;bottom:30px;background:#fff;color:#0D0D0D;border-radius:100px;padding:10px;text-align:center;font-size:13px;font-weight:600">Book a free strategy call</p></div><h4 style="font-size:24px;margin-top:14px">Story · 9:16</h4><p class="muted" style="font-size:19px">Keep top and bottom 14% clear.</p></div>
  </div>""", eyebrow="Marketing · Social media", foot="<span>Editable full-size versions of each template are in the Canva folder.</span>"))

P.append(page("Social: platform specs", table(["Platform", "Role", "Feed sizes", "Other sizes", "Cadence"], [
    ("<b>LinkedIn</b><br><span class='muted'>company + founder</span>", "Main channel. Authority and inbound.", "1080 × 1350 (4:5) · 1200 × 1200 · Carousel PDF 1080 × 1350", "Banner 1128 × 191 · Logo 400 × 400 · Link 1200 × 627", "Company 3–4/wk · Founder 4–5/wk"),
    ("<b>Instagram</b><br><span class='muted'>@fastexmedia_</span>", "Culture, proof, reels.", "1080 × 1350 (4:5) · key content in centre 3:4", "Stories/Reels 1080 × 1920 · Profile 320 × 320", "3/wk + stories daily"),
    ("<b>X</b><br><span class='muted'>@shahaagamn</span>", "Founder voice, quick insights.", "1600 × 900 (16:9) · 1080 × 1080", "Header 1500 × 500 · Profile 400 × 400", "1/day"),
    ("<b>WhatsApp Business</b>", "Conversations, follow-up, status.", "Status 1080 × 1920", "Profile 640 × 640 (badge) · Catalogue 1080 × 1080", "Status 2–3/wk")], "margin-top:30px;font-size:22px"),
    eyebrow="Marketing · Social media", title="Platform specs"))

P.append(page("Social: content pillars", """
  <div class="row" style="margin-top:60px;gap:24px">
    <div class="col box"><p class="big" style="font-size:90px;color:#C94A00">40%</p><h3 style="margin-top:14px">Proof</h3><p class="muted" style="margin-top:8px">Results, case studies, client wins, testimonials.</p></div>
    <div class="col box"><p class="big" style="font-size:90px;color:#C94A00">30%</p><h3 style="margin-top:14px">Playbooks</h3><p class="muted" style="margin-top:8px">How outbound works: sequences, subject lines, data tips.</p></div>
    <div class="col box"><p class="big" style="font-size:90px;color:#C94A00">20%</p><h3 style="margin-top:14px">Industry insight</h3><p class="muted" style="margin-top:8px">What buyers in solar, IT, manufacturing, education and real estate care about now.</p></div>
    <div class="col box"><p class="big" style="font-size:90px;color:#C94A00">10%</p><h3 style="margin-top:14px">Behind the machine</h3><p class="muted" style="margin-top:8px">Team, process, the office in Surat, lessons learned.</p></div>
  </div>""", eyebrow="Marketing · Social media", title="Content pillars"))

P.append(page("Social: caption formula", f"""
  <div class="row" style="margin-top:20px;gap:40px">
    <div class="col box"><div style="display:flex;gap:14px;align-items:center">{logo('fx-avatar-dark', 64, 64)}<p style="font-size:22px"><b>Fastex Media</b><br><span class="muted" style="font-size:18px">B2B Lead Generation Agency · 1d</span></p></div>
      <p style="margin-top:22px;font-size:22px"><span class="mono" style="color:#C94A00;font-size:16px">HOOK</span><br>Most B2B pipelines don't have a lead problem. They have a follow-up problem.</p>
      <p style="margin-top:14px;font-size:22px"><span class="mono" style="color:#C94A00;font-size:16px">PROOF</span><br>Across our client accounts, more meetings come from touches 3 to 5 than from the first message.</p>
      <p style="margin-top:14px;font-size:22px"><span class="mono" style="color:#C94A00;font-size:16px">INSIGHT</span><br>So we build every sequence across LinkedIn, email and WhatsApp before we write a single word of copy.</p>
      <p style="margin-top:14px;font-size:22px"><span class="mono" style="color:#C94A00;font-size:16px">ASK</span><br>How many touches does your team make before giving up?</p></div>
    <div class="col"><ul style="font-size:23px"><li>The first 2 lines must work alone: that's all people see before "…see more".</li><li>Short lines with white space between them.</li><li>3 to 5 hashtags at the end: #B2BMarketing #LeadGeneration #Outbound plus one industry tag.</li><li>Tag the client only with written approval.</li><li>Links in the first comment on LinkedIn, not in the post.</li><li>Reply to every comment within 2 working hours on posting day.</li><li>Every template includes the mark or fastexmedia.com.</li></ul></div>
  </div>""", eyebrow="Marketing · Social media · Hook, Proof, Insight, Ask"))

# ads
P.append(page("Ads: principles", """
  <div class="row" style="margin-top:60px">
    <div class="col box"><h3>One message</h3><p class="muted" style="margin-top:14px">Each ad makes one promise. If you need "and", make it two ads.</p></div>
    <div class="col box"><h3>Proof in the frame</h3><p class="muted" style="margin-top:14px">A number, an industry or a method should be visible without reading the caption.</p></div>
    <div class="col box"><h3>Brand in the first second</h3><p class="muted" style="margin-top:14px">Ink + orange + Outfit, mark in a corner. For video, show the mark within 2 seconds and at the end.</p></div>
  </div>""", eyebrow="Marketing · Ads", title="Ads get one glance"))

P.append(page("Ads: mock-ups", f"""
  <div class="row" style="gap:36px;margin-top:10px;align-items:flex-start">
    <div style="width:820px" class="box" ><div style="display:flex;gap:14px;align-items:center">{logo('fx-avatar-dark', 56, 56)}<p style="font-size:21px"><b>Fastex Media</b><br><span class="muted" style="font-size:17px">Promoted</span></p></div>
      <p style="font-size:21px;margin-top:14px">Your SDRs shouldn't spend Monday building lists. We research decision-makers, run the outreach and put qualified meetings on your calendar.</p>
      <div style="margin-top:16px;height:390px;background:#0D0D0D;color:#fff;border-radius:12px;padding:44px;box-sizing:border-box;position:relative;overflow:hidden"><div style="position:absolute;top:-40px;bottom:-40px;right:150px;width:70px;background:#FF6600;transform:skewX(33.69deg)"></div><p style="position:relative;font-family:Outfit,Arial,sans-serif;font-size:62px;font-weight:600;line-height:1;max-width:460px">Your sales calendar, <span style="color:#FF6600">full.</span></p><p style="position:relative;color:#B5B3AE;font-size:20px;margin-top:20px">Qualified B2B meetings · every week</p></div>
      <div style="display:flex;justify-content:space-between;align-items:center;margin-top:16px"><p style="font-size:21px"><b>Book a free strategy call</b><br><span class="muted" style="font-size:17px">fastexmedia.com</span></p><span class="pill" style="border-color:#C94A00;color:#C94A00;font-size:19px;padding:10px 22px">Learn more</span></div></div>
    <div class="col">
      <div class="box" style="font-family:Arial,sans-serif"><p style="font-size:18px;font-weight:700">Sponsored</p><p class="muted" style="font-size:18px;margin-top:6px">Fastex Media · fastexmedia.com/b2b-lead-generation</p><p style="color:#1A0DAB;font-size:28px;line-height:1.3;margin-top:10px">B2B Lead Generation Agency | Qualified Meetings Booked | Free Strategy Call</p><p class="muted" style="font-size:20px;margin-top:8px">Multi-channel outbound across LinkedIn, email and WhatsApp. Verified decision-maker data. Reported on meetings booked.</p></div>
      <div class="box" style="margin-top:24px"><h4>Formula: Pain, Proof, Prompt</h4><p style="font-size:21px;margin-top:10px"><b>Pain:</b> "Your SDRs shouldn't spend Monday building lists."<br><b>Proof:</b> "3X average lead growth across client accounts."<br><b>Prompt:</b> "Book a free strategy call."</p></div>
    </div>
  </div>""", eyebrow="Marketing · Ads · LinkedIn and Google"))

P.append(page("Ads: specs and limits", table(["Platform", "Format", "Image / video", "Copy limits (aim for)"], [
    ("<b>LinkedIn</b>", "Single image", "1200 × 627 · 1200 × 1200 · 720 × 900", 'Intro ~150 chars before "see more" · Headline ~70'),
    ("<b>LinkedIn</b>", "Document / carousel", "1080 × 1350 PDF, 5–10 pages", "Intro ~150 · first page works as a cover"),
    ("<b>LinkedIn</b>", "Lead gen form", "As above", "3–4 fields max · pre-fill from profile"),
    ("<b>Meta</b>", "Feed / Reels / Stories", "1080 × 1350 · 1080 × 1920 · 1080 × 1080", "Primary text 125 · Headline 40 · Description 30"),
    ("<b>Google Search</b>", "Responsive search ad", "Assets: logo 1200 × 1200 &amp; 1200 × 300", "Up to 15 headlines × 30 · 4 descriptions × 90 · Paths 2 × 15"),
    ("<b>Google Display / PMax</b>", "Responsive display", "1200 × 628 · 1200 × 1200 · 960 × 1200", "Short headline 30 · Long headline 90 · Description 90")], "margin-top:24px;font-size:22px"),
    eyebrow="Marketing · Ads", title="Specs and limits", foot="<span>Platforms change their specs. Check each platform's help page before launch.</span>"))

P.append(page("Ads: CTA library and claims", """
  <h3>CTA library</h3>
  <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:18px"><span class="pill" style="background:#FF6600;border-color:#FF6600">Book a Free Strategy Call</span><span class="pill">See case studies</span><span class="pill">Get the playbook</span><span class="pill">Map my market</span><span class="pill">Talk to us on WhatsApp</span><span class="pill">View service →</span></div>
  <h3 style="margin-top:44px">Claims and compliance</h3>""" +
    dd("Do", ['Call every figure an average and say what of: "3X average lead growth across client accounts".', "Keep a source sheet for every number used in an ad.", "Get written approval before naming a client or using their logo.", "Only click-to-WhatsApp ads with opted-in contacts."],
       "Don't", ['"Guaranteed leads", "guaranteed ROI" or a fixed meeting count without contract terms.', "Competitor names or trademarks without legal review.", 'Fake urgency: "only 2 spots left" unless true.', "More than about 20% text on paid images."], "margin-top:18px"),
    eyebrow="Marketing · Ads"))

P.append(page("Before you publish", """
  <div class="row" style="margin-top:30px">
    <ul class="col" style="font-size:30px;list-style:none;padding:0"><li>☐ Does it make one clear promise?</li><li>☐ Is every number sourced and described as an average?</li><li>☐ Does it use the official logo file, with clear space?</li><li>☐ Is orange under 10%, with no white-on-orange text?</li></ul>
    <ul class="col" style="font-size:30px;list-style:none;padding:0"><li>☐ Is it set in Outfit and Inter only?</li><li>☐ Is it free of the avoid list ("guaranteed", "viral", "!!!")?</li><li>☐ Is client approval in writing, if a client is named?</li><li>☐ Is there one CTA from the CTA library?</li></ul>
  </div>""", cls="orange", eyebrow="Marketing · Checklist", title="Before you publish"))

# ------------------------------------------------------------------ 6 resources
P.append(section_divider(6, "Resources", "Files and the master prompt used to build this kit."))
P.append(page("Files", table(["File", "Where", "Use"], [
    ("<b>10 logo files (SVG)</b>", "Canva folder · Fastex Media Brand Kit", "Primary, reversed, one-colour black and white, badge, tile, horizontal and stacked lockups"),
    ("<b>PNG logos, any size</b>", "mediafastex-collab.github.io/Brandkit → Resources", "Pick 512 to 4096 px"),
    ("<b>Full ZIP</b>", "Website → Download kit", "All logos, original artwork, tokens, prompt"),
    ("<b>Colour tokens (CSS, JSON)</b>", "Website → Resources", "For developers and Figma"),
    ("<b>Social and ad templates</b>", "Canva folder", "Stat post, testimonial, carousel, story, LinkedIn ad, banners"),
    ("<b>Master prompt</b>", "Canva folder (Doc) · Website", "Regenerate or extend these guidelines with Claude")], "margin-top:30px;font-size:24px"),
    eyebrow="Resources", title="Files"))

prompt = (ROOT / "BRANDKIT_PROMPT.md").read_text()
body = prompt.split("## Prompt", 1)[1].strip().strip("-").strip()
parts = body.split("### 3.")
for i, chunk in enumerate([parts[0], "### 3." + parts[1]]):
    txt = E(chunk).replace("**", "")
    txt = re.sub(r"^### (.*)$", r"<b>\1</b>", txt, flags=re.M)
    txt = txt.replace("\n", "<br>")
    P.append(page(f"Master prompt {i + 1}", f'<div class="box soft mono" style="font-size:17px;line-height:1.5;padding:28px;height:760px;overflow:hidden">{txt}</div>',
                  eyebrow=f"Resources · Master prompt ({i + 1} of 2)"))

P.append(page("Contact", f"""
  {logo('fx-lockup-horizontal-reversed', 700, 123)}
  <h2 style="margin-top:120px">Questions about the brand?</h2>
  <p class="muted" style="margin-top:24px;font-size:30px">hello@fastexmedia.com · +91 93286 80929<br>The Junomoneta Tower, Surat, Gujarat<br>fastexmedia.com · mediafastex-collab.github.io/Brandkit</p>""",
                cls="dark", foot="<span>© 2026 Fastex Media. Engineered for B2B scale.</span>"))

doc = f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>Fastex Media Brand Guidelines</title>{FONTS}<style>{CSS}</style></head><body>\n' + "".join(P) + "</body></html>\n"
(OUT / "brand-guidelines.html").write_text(doc)
print("deck pages:", len(P))

# ------------------------------------------------------------------ templates
T = OUT / "templates"
T.mkdir(parents=True, exist_ok=True)


def tpl(fname, title, w, h, inner, bg):
    (T / fname).write_text(
        f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>{FONTS}<style>body{{margin:0;font-family:Inter,Arial,sans-serif}}'
        f'h1,h2,p{{margin:0}}.page{{width:{w}px;height:{h}px;position:relative;overflow:hidden;background:{bg};box-sizing:border-box}}'
        f'.band{{position:absolute;background:#FF6600;transform:skewX(33.69deg)}}</style></head><body>{inner}</body></html>')


def pg(inner, label="Page"):
    return f'<section class="page" data-document-role="page" data-label="{label}">{inner}</section>'


tpl("stat-post-1080.html", "Fastex - Stat post 1080x1080", 1080, 1080, pg(f"""
<div style="padding:97px">
<p style="font:500 38px Inter,Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#A9A7A2">Client result · average</p>
<p style="font:600 400px/0.85 Outfit,Arial,sans-serif;letter-spacing:-0.05em;color:#FF6600;margin-top:100px">60%</p>
<p style="font:500 74px/1.15 Outfit,Arial,sans-serif;color:#fff;margin-top:40px;max-width:760px">lower cost per lead across client accounts</p></div>
<div style="position:absolute;left:97px;bottom:86px">{logo('fx-mark-reversed', 140, 127)}</div>
<p style="position:absolute;right:97px;bottom:100px;font:500 36px Inter,Arial,sans-serif;color:#A9A7A2">fastexmedia.com</p>""", "Stat post"), "#0D0D0D")

tpl("testimonial-1080x1350.html", "Fastex - Testimonial 1080x1350", 1080, 1350, pg(f"""
<div style="padding:108px 97px">
<div style="width:97px;height:140px;background:#FF6600;clip-path:polygon(0 0,40% 0,100% 50%,40% 100%,0 100%,60% 50%)"></div>
<p style="font:500 92px/1.14 Outfit,Arial,sans-serif;letter-spacing:-0.02em;color:#0D0D0D;margin-top:86px">"Fastex Media built a lead system that fills our sales calendar every week."</p>
<p style="font:500 38px Inter,Arial,sans-serif;color:#63636B;margin-top:76px">Fastex Media client · B2B services</p></div>
<div style="position:absolute;left:97px;bottom:113px;width:324px;height:9px;background:#0D0D0D"></div>
<div style="position:absolute;right:97px;bottom:97px">{logo('fx-mark-primary', 119, 108)}</div>""", "Testimonial"), "#FBFAF8")

car_inner = f"""<div style="padding:108px 97px;color:#fff"><p style="font:500 38px 'DM Mono',monospace;color:#FF6600">02 / 07</p>
<p style="font:600 110px/1 Outfit,Arial,sans-serif;letter-spacing:-0.035em;margin-top:200px">Map the market</p>
<p style="font:400 44px/1.45 Inter,Arial,sans-serif;color:#C9C7C2;margin-top:50px;max-width:820px">Define the accounts worth winning and build a verified dataset of the decision-makers inside them.</p></div>
<div style="position:absolute;left:97px;bottom:86px">{logo('fx-mark-reversed', 119, 108)}</div>"""
tpl("carousel-1080x1350.html", "Fastex - LinkedIn carousel 1080x1350", 1080, 1350, pg(f"""
<div style="padding:108px 97px;color:#0D0D0D"><p style="font:500 38px 'DM Mono',monospace">01 / 07</p>
<p style="font:600 146px/0.95 Outfit,Arial,sans-serif;letter-spacing:-0.04em;margin-top:238px">Three moves. One machine.</p>
<p style="font:500 48px/1.35 Inter,Arial,sans-serif;margin-top:65px;max-width:880px">How we book qualified B2B meetings, step by step.</p></div>
<div style="position:absolute;left:97px;bottom:86px">{logo('fx-mark-black', 119, 108)}</div>
<p style="position:absolute;right:97px;bottom:97px;font:600 43px Inter,Arial,sans-serif;color:#0D0D0D">Swipe →</p>""", "Cover").replace('class="page"', 'class="page" style="background:#FF6600"') +
    pg(car_inner, "Inside page").replace('class="page"', 'class="page" style="background:#0D0D0D"'), "#FF6600")

tpl("story-1080x1920.html", "Fastex - Story 1080x1920", 1080, 1920, pg(f"""
<div class="band" style="top:-100px;bottom:-100px;right:-65px;width:324px"></div>
<div style="position:absolute;left:97px;top:130px">{logo('fx-mark-reversed', 162, 147)}</div>
<p style="position:absolute;left:97px;right:324px;top:845px;font:600 130px/1 Outfit,Arial,sans-serif;letter-spacing:-0.035em;color:#fff">Your sales calendar, full.</p>
<p style="position:absolute;left:97px;right:97px;bottom:151px;background:#fff;color:#0D0D0D;border-radius:100px;padding:54px;text-align:center;font:600 54px Inter,Arial,sans-serif">Book a free strategy call</p>""", "Story"), "#0D0D0D")

tpl("linkedin-ad-1200x627.html", "Fastex - LinkedIn ad 1200x627", 1200, 627, pg(f"""
<div class="band" style="top:-60px;bottom:-60px;right:168px;width:108px"></div>
<div style="padding:84px 72px;position:relative"><p style="font:600 96px/1 Outfit,Arial,sans-serif;letter-spacing:-0.03em;color:#fff;max-width:680px">Your sales calendar, <span style="color:#FF6600">full.</span></p>
<p style="font:500 32px Inter,Arial,sans-serif;color:#B5B3AE;margin-top:40px">Qualified B2B meetings · every week</p></div>
<div style="position:absolute;right:54px;bottom:60px">{logo('fx-mark-reversed', 84, 76)}</div>""", "LinkedIn ad"), "#0D0D0D")

tpl("linkedin-banner-1128x191.html", "Fastex - LinkedIn banner 1128x191", 1128, 191, pg(f"""
<div class="band" style="top:-30px;bottom:-30px;left:700px;width:46px"></div><div class="band" style="top:-30px;bottom:-30px;left:780px;width:46px;opacity:.35"></div>
<p style="position:absolute;left:300px;top:48px;font:600 44px/1 Outfit,Arial,sans-serif;letter-spacing:-0.02em;color:#fff">Qualified B2B meetings. Every week.</p>
<p style="position:absolute;left:300px;top:110px;font:500 20px Inter,Arial,sans-serif;color:#B5B3AE">LinkedIn · Cold email · WhatsApp · Performance marketing</p>
<p style="position:absolute;right:40px;bottom:30px;font:500 18px Inter,Arial,sans-serif;color:#FF6600">fastexmedia.com</p>""", "Banner"), "#0D0D0D")

tpl("x-header-1500x500.html", "Fastex - X header 1500x500", 1500, 500, pg(f"""
<div class="band" style="top:-80px;bottom:-80px;left:1000px;width:110px"></div><div class="band" style="top:-80px;bottom:-80px;left:1170px;width:110px;opacity:.3"></div>
<div style="position:absolute;left:90px;top:120px">{logo('fx-lockup-horizontal-reversed', 600, 105)}</div>
<p style="position:absolute;left:90px;top:290px;font:500 40px Outfit,Arial,sans-serif;color:#fff">Engineered for B2B scale.</p>""", "X header"), "#0D0D0D")

print("templates:", len(list(T.glob("*.html"))))
