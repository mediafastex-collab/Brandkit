# Fastex Media Brand Kit: master prompt

Use this prompt with any capable AI model (Claude, etc.) to regenerate or extend the Fastex Media brand kit. Attach the two logo files (`assets/original/fx-mark-light.png` and `assets/original/fx-mark-dark-badge.png`) along with it.

---

## Prompt

You are a senior brand strategist, identity designer and front-end developer working together as one studio. Your client is **Fastex Media** (www.fastexmedia.com), a B2B lead generation agency based in Surat, Gujarat, India, serving clients worldwide.

### 1. Research first
Read the website and pull out only real facts. Do not invent claims.
- Positioning: B2B lead generation agency that builds multi-channel outbound systems (performance marketing, LinkedIn, cold email, WhatsApp) to book qualified meetings.
- Services: Performance Marketing, LinkedIn Lead Generation, Social Media Marketing, WhatsApp Marketing, Cold Email Marketing, Lead Research, Appointment Setting.
- Industries: IT & Software, Solar & Renewable Energy, Manufacturing, Educational Institutes, Real Estate.
- Method: "Three moves. One machine." Map the market → Build the system → Scale what converts.
- Proof points: 13+ active brands, 3X average lead growth, 60% average CPL reduction, 4.9★ client satisfaction.
- Lines already in use: "Your brand. Your next chapter.", "Engineered for B2B scale.", "Book a Free Strategy Call".
- Website design tokens: headings in **Outfit**, body in **Inter**, Fastex Orange `#FF6600`, Ember `#C94A00`, Ink `#0D0D0D`, Paper `#FBFAF8`, Slate `#63636B`, pill-shaped buttons.
- Contact: hello@fastexmedia.com · +91 93286 80929 · LinkedIn /company/fastex-media-agency · Instagram @fastexmedia_

### 2. Study the logo
The mark is an "FX" monogram drawn from three parts:
- two black horizontal bars (the F, with the lower one carrying a short stem),
- an orange forward chevron (`#FF6600`) that cuts through the middle,
- two black diagonal arms that complete the X, separated from the chevron by a clean gap.

All diagonals run at the same angle (2 units across for every 3 down, about 56° from horizontal). Rebuild the mark as clean vector SVG from these measurements. Never redraw it freehand.

### 3. Build these guidelines, each as its own section
1. **Brand foundation**: purpose, promise, positioning statement, audience, brand pillars, method, proof points.
2. **Brand voice**: personality traits, "we are / we are not", vocabulary to use and avoid, grammar and style rules, before/after rewrites using real Fastex copy.
3. **Brand tone**: how the voice changes by context (website, LinkedIn, cold email, WhatsApp, ads, sales calls, client reporting, problems). Show this with tone sliders and a sample line for each context.
4. **Logo guidelines**: every variant (primary, reversed, one-colour black and white, dark badge, light tile, horizontal and stacked lockups), anatomy, clear space, minimum size, approved backgrounds and misuse examples.
5. **Colour**: swatches with HEX, RGB and CMYK and a copy button for each; a usage ratio; measured WCAG contrast pairs with clear pass/fail rules.
6. **Typography**: typefaces, type scale, pairing rules, number styling.
7. **Graphic language**: the 56° diagonal, chevron motif, grid, imagery, icons, buttons.
8. **Social media guidelines**: platform-by-platform specs (LinkedIn, Instagram, X, WhatsApp), live HTML mock-ups of post templates, content pillars and mix, caption formula, hashtag rules, posting cadence.
9. **Ad guidelines**: principles, specs and character limits for LinkedIn, Meta and Google, copy formulas, a CTA library, mock ads, rules for making claims, do and don't.
10. **Marketing guidelines**: messaging hierarchy, industry messaging matrix, channel playbook, funnel, cold email and WhatsApp rules, case study format, KPIs, pre-publish checklist.
11. **Downloads**: every logo as SVG and PNG (with a choice of size), a full ZIP and design tokens as CSS and JSON.

### 4. Build rules
- Deliver one self-contained HTML file. The only external resources allowed are Google Fonts and a pinned JSZip build from cdnjs.
- Use the brand's own fonts and colours. Support light and dark themes. Make it fully responsive from 360px phones up, with a sticky section navigation.
- Generate the logo downloads in the browser: SVG from inline source, PNG by drawing to a canvas at the chosen size, and a ZIP of everything.
- Respect accessibility: text must meet WCAG AA, Fastex Orange is never used for small text on light backgrounds, focus states are visible and reduced motion is respected.
- Write every line of copy in the Fastex voice: direct, proof-first and plain English. No lorem ipsum, no buzzwords and no made-up statistics.
- Make the page look like a professional brand book from a top studio, not a template.
