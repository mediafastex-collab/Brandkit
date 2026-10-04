# Brand Design Rules: Variable Template

Use this template for static posts and carousels. Replace the brand variables once when setting up a brand. Replace the content variables for each post. Keep the layout rules fixed.

## 1. Brand variables — change once per brand

| Variable | What to enter |
| --- | --- |
| `{{BRAND_NAME}}` | Exact brand name |
| `{{ACCENT_COLOR}}` | Approved primary accent, as a HEX colour |
| `{{LIGHT_BACKGROUND}}` | Approved light background, as a HEX colour |
| `{{DARK_BACKGROUND}}` | Approved dark background, as a HEX colour |
| `{{TEXT_ON_LIGHT}}` | Dark text colour with clear contrast on the light background |
| `{{TEXT_ON_DARK}}` | Light text colour with clear contrast on the dark background |
| `{{SUPPORTING_COLORS}}` | Approved supporting colours for artwork; omit if none |
| `{{HEADLINE_FONT}}` | Approved bold headline and CTA font family |
| `{{BODY_FONT}}` | Approved body font family |
| `{{LABEL_FONT}}` | Approved label, counter and footer font family |
| `{{BRAND_LOGO_ASSET}}` | Supplied original logo file; empty when unavailable |
| `{{BRAND_LOGO_MODE}}` | `reserve_only` or `place_approved` |
| `{{PARTNER_1_NAME}}` / `{{PARTNER_2_NAME}}` | Names of approved partners, if applicable |
| `{{PARTNER_1_ASSET}}` / `{{PARTNER_2_ASSET}}` | Supplied original partner-logo files; empty when unavailable |
| `{{PARTNER_LOGO_MODE}}` | `reserve_only` or `place_approved` |
| `{{CONTACT_TEXT}}` | One short email address, website or phone number |
| `{{FOOTER_TEXT}}` | Short approved tagline or footer; empty to omit |
| `{{AUDIENCE}}` | Who should understand and relate to the post |
| `{{BRAND_VOICE}}` | For example: clear, practical, calm and professional |
| `{{LANGUAGE}}` | Content language; selected fonts must support it |
| `{{VISUAL_STYLE}}` | One approved visual style, such as clean 3D illustration or product photography |
| `{{APPROVED_PROOF}}` | Optional verified achievements or facts, with their exact meaning and source |

Set these values before designing. Keep them consistent across the brand's full set. Changing a font family does not change its fixed size, box or baseline. Set an optional variable to empty when it is not needed; never print unresolved variables on the design.

For the current logo-free delivery, use `reserve_only` for both logo modes. The spaces remain empty even when no logo asset is supplied.

## 2. Content variables — change per post

| Variable | What to enter |
| --- | --- |
| `{{POST_FORMAT}}` | `static` or `carousel` |
| `{{POST_THEME}}` | `light` or `dark` for a static post |
| `{{SLIDE_COUNT}}` | Total carousel slides; fixed for that carousel |
| `{{SLIDE_NUMBER}}` | Current slide number |
| `{{TOPIC}}` | One clear topic or problem |
| `{{SECTION_LABEL}}` | Short category or section number |
| `{{HEADLINE}}` | Short, clear headline; maximum three lines |
| `{{BODY_COPY}}` | Problem, useful explanation or practical fix; maximum three lines |
| `{{HIGHLIGHT_PHRASE}}` | Exact words to emphasise in the accent colour |
| `{{VISUAL_BRIEF}}` | A scene that clearly represents this slide's content |
| `{{VISUAL_CAPTION}}` | Optional short label for the artwork |
| `{{CTA}}` | One clear next action; maximum two lines |
| `{{POST_CAPTION}}` | Complete social caption in the brand voice |
| `{{HASHTAGS}}` | Five to seven relevant brand, industry or problem hashtags |

Each slide can have different content and artwork. The same type of element must always stay at the same position.

## 3. Fixed layout — do not change per brand, post or slide

Canvas: **1080 × 1350 px, portrait, 4:5**. Export a complete opaque RGB PNG. Coordinates below are in pixels from the top-left corner. A baseline is the line on which the text sits.

| Element | Fixed position or region | Fixed size and behaviour |
| --- | --- | --- |
| Content edges | Left x64; right x1016 | 64 px side margins; width 952; left-aligned text |
| Reserved top header | y0–195 across the full canvas | No content, artwork, shadow or decoration; only an approved logo when its mode allows placement |
| Brand-logo safe area | x640, y48, w376, h120 | Top-right; preserve the complete logo's proportions and clear space |
| Reference logo footprint | x662, y72, maximum w330, h72 | Contain the full logo, including any tagline; never stretch or crop it |
| Section label / section number | x64, y196, w952, h32; baseline 220 | `{{LABEL_FONT}}`, 24 px; 1.5 px tracking |
| Headline | x64, y252, w952, h231; baselines 308 / 385 / 462 | `{{HEADLINE_FONT}}`, bold 70 px; 77 px line spacing; maximum 3 lines; −1.3 px tracking |
| Body | x64, y482, w952, h117; baselines 514 / 553 / 592 | `{{BODY_FONT}}`, 31 px; 39 px line spacing; maximum 3 lines |
| Full visual window | x64, y618, w952, h480 | Only artwork and its optional caption belong here |
| Artwork | x64, y618, w952, h442 | Scale proportionally; keep complete objects inside this region |
| Visual caption | x64; baseline 1090 | `{{LABEL_FONT}}`, 20 px; one short line; omit when empty |
| Accent separator | x64, y1134, w88, h4 | `{{ACCENT_COLOR}}` |
| CTA | x64, y1164, w952, h76; baselines 1192 / 1230 | `{{HEADLINE_FONT}}`, bold 30 px; 38 px line spacing; maximum 2 lines |
| Regular carousel footer | x64; baseline 1262 | `{{LABEL_FONT}}`, 20 px; one short line |
| Static / final-carousel contact | x704; baseline 1262; maximum width312 | `{{LABEL_FONT}}`, 20 px; one short line |
| Reserved partner band | x64, y1248, w620, h80 | Required on every static and final carousel slide |
| Partner 1 slot | x64, y1256, w280, h64 | Contain the full approved logo without distortion |
| Partner 2 slot | x376, y1256, w280, h64 | Contain the full approved logo without distortion |
| Carousel counter | Right edge x1016; baseline 1290 | `{{LABEL_FONT}}`, 24 px; two-digit format such as `01 / 06` |

The fonts and colours are variables. The positions, font sizes, margins, line spacing, alignment and maximum line counts are fixed.

## 4. Fixed design behaviour

1. Use one structure for covers, middle slides and closing slides. Never redesign the cover's headline, body, CTA or counter position.
2. Keep the full headline and body regions reserved even when the copy is shorter. Do not move following blocks up or down.
3. Keep section numbers at the section anchor and slide counters at the counter anchor. Their positions must not jump when swiping.
4. Carousel odd slides use `{{DARK_BACKGROUND}}`; even slides use `{{LIGHT_BACKGROUND}}`. Use the matching text colour. Static posts use `{{POST_THEME}}`.
5. Use `{{ACCENT_COLOR}}` for the approved highlight phrase and separator. Supporting artwork colours must come from `{{SUPPORTING_COLORS}}` and the approved palette.
6. Shorten or rephrase draft copy to fit its box while preserving meaning. Never shrink one slide's font, move its blocks, crop its text or stretch its artwork to force a fit. Export approved copy exactly; flag any remaining overflow.
7. Artwork may vary within the visual window. Keep one visual style for the brand. Do not let an object, label or shadow spill into text or logo areas.
8. Use natural proportions, clear text contrast and balanced composition. Avoid filler graphics or large unexplained gaps inside the active content area. The reserved logo spaces remain protected.
9. Generate or source artwork separately from exact text. Place approved headlines, labels, numbers, captions and CTAs on the fixed layout so spelling and alignment remain reliable.
10. Do not display drafting guides, placeholder outlines, missing-variable text, fake logos or imitation certification badges in final exports.

### Logo and footer behaviour

- **Brand logo — `reserve_only`:** leave the entire top header as pure slide background. No logo, wordmark, tagline artwork, placeholder or decoration.
- **Brand logo — `place_approved`:** place only `{{BRAND_LOGO_ASSET}}` within the fixed top-right area. Keep the remainder of the header empty. Use the original artwork and its approved clear space.
- **Partner logos — `reserve_only`:** on statics and final carousel slides, leave the entire bottom-left partner band as pure slide background. No logo, label, outline, shadow, footer or artwork inside it.
- **Partner logos — `place_approved`:** place only the supplied, approved partner assets in their two fixed slots. Use names and certifications only when they are confirmed for that brand. An empty asset leaves its slot empty.
- **Static and final carousel:** use `{{CONTACT_TEXT}}` at the right contact anchor. Omit the regular left footer to protect the partner band. The final carousel keeps its counter in the usual position.
- **Other carousel slides:** use `{{FOOTER_TEXT}}` at the regular footer anchor and keep the usual counter. Omit the footer when its variable is empty.
- **Static posts:** omit the slide counter. Every other main content block remains fixed.

## 5. Fixed content standards

Write for `{{AUDIENCE}}` in `{{LANGUAGE}}`, using `{{BRAND_VOICE}}`.

- Lead with an actual situation or problem the reader recognises. Use short, familiar words and a clear headline.
- Explain a practical fix or useful next step. Describe how `{{BRAND_NAME}}` helps in words the audience understands.
- Keep small labels, artwork captions, post captions and CTAs as clear as the headline. Avoid technical terms unless the audience understands them and they add meaning.
- Make the visual show the same problem or solution as the copy. Do not use an attractive scene that changes the message.
- Use one relevant CTA. Make every carousel slide add a distinct point or next step.
- Use `{{APPROVED_PROOF}}` only when supplied and relevant. Keep projects, clients, results and time periods distinct; do not invent statistics, promises or testimonials.
- Use relevant hashtags without padding the list or forcing unrelated software or industry names into it.

## 6. Copy-paste master prompt

Fill the variables above, then use the following prompt:

```text
Create {{POST_FORMAT}} content and designs for {{BRAND_NAME}} on {{TOPIC}}.

BRAND
Audience: {{AUDIENCE}}
Language: {{LANGUAGE}}
Voice: {{BRAND_VOICE}}
Visual style: {{VISUAL_STYLE}}
Accent: {{ACCENT_COLOR}}
Light background / text: {{LIGHT_BACKGROUND}} / {{TEXT_ON_LIGHT}}
Dark background / text: {{DARK_BACKGROUND}} / {{TEXT_ON_DARK}}
Supporting artwork colours: {{SUPPORTING_COLORS}}
Headline and CTA font: {{HEADLINE_FONT}}
Body font: {{BODY_FONT}}
Labels, counters and footer font: {{LABEL_FONT}}
Brand logo mode / asset: {{BRAND_LOGO_MODE}} / {{BRAND_LOGO_ASSET}}
Partner logo mode: {{PARTNER_LOGO_MODE}}
Partner 1 name / asset: {{PARTNER_1_NAME}} / {{PARTNER_1_ASSET}}
Partner 2 name / asset: {{PARTNER_2_NAME}} / {{PARTNER_2_ASSET}}
Contact: {{CONTACT_TEXT}}
Regular footer: {{FOOTER_TEXT}}
Verified proof, if any: {{APPROVED_PROOF}}

CONTENT
Static theme: {{POST_THEME}}
Carousel slide count: {{SLIDE_COUNT}}
For each slide, use its assigned {{SLIDE_NUMBER}}, {{SECTION_LABEL}},
{{HEADLINE}}, {{BODY_COPY}}, {{HIGHLIGHT_PHRASE}}, {{VISUAL_BRIEF}},
{{VISUAL_CAPTION}} and {{CTA}}.
Write or use the approved {{POST_CAPTION}} and {{HASHTAGS}} separately
from the image. Optional empty variables must not appear as placeholders.

LOCKED LAYOUT
Export each image at exactly 1080 × 1350, portrait 4:5, opaque RGB PNG.
Use fixed side edges x64–1016, width 952. All main copy is left-aligned.
Protect the top header y0–195. Brand-logo safe area: x640,y48,w376,h120.
Contain the complete approved logo within x662,y72,maximum width 330,maximum height 72.
With reserve_only, the entire header stays empty in the slide background.
With place_approved, only the supplied logo may occupy this header.
Section label: x64,y196,w952,h32,baseline 220,font 24,tracking 1.5.
Headline: x64,y252,w952,h231,bold 70,baselines 308 / 385 / 462,
77 px line spacing,max 3 lines,tracking −1.3.
Body: x64,y482,w952,h117,font 31,baselines 514 / 553 / 592,
39 px line spacing,max 3 lines.
Artwork: x64,y618,w952,h442; fit complete objects proportionally.
Optional artwork caption: x64,baseline 1090,font 20,one short line.
Accent separator: x64,y1134,w88,h4.
CTA: x64,y1164,w952,h76,bold 30,baselines 1192 / 1230,
38 px line spacing,max 2 lines.
Regular footer: x64,baseline 1262,font 20,one short line.
Carousel counter: right1016,baseline 1290,font 24,two-digit current/total.
Static and final-carousel contact: x704,baseline 1262,font 20,maximum width 312.
On every static and final carousel slide, protect the partner band
x64,y1248,w620,h80. Partner 1 slot: x64,y1256,w280,h64.
Partner 2 slot: x376,y1256,w280,h64.
With reserve_only, this entire band must be pure slide background.
With place_approved, use only the supplied approved partner artwork,
contained within each slot. No other text, shadow or artwork may enter.
Use the right contact anchor instead of the regular left footer on these
slides. Keep the carousel counter at its usual anchor. Statics have no counter.

FIXED STRUCTURE AND CONTENT
Carousel odd slides are dark; even slides are light. Statics use POST_THEME.
Use the same anchors, fonts, font sizes, margins and line spacing on covers,
middle slides and closing slides. Reserve each block even when its copy is
shorter. Never shift a number or move the next block to follow short copy.
Use a clear, recognisable problem, practical response and relevant CTA.
Make the artwork represent the copy. Keep language understandable to the
specified audience. Use verified claims only and 5–7 relevant hashtags.
Typeset all exact text and numbers on the fixed layout; keep generated
artwork free of accidental text, logos, charts or certification badges.
Rephrase draft copy to fit; preserve approved copy exactly in the export.
Never resize one slide's text, change its layout or crop content to fit.

DELIVER
Complete PNGs in slide order, the full post caption, relevant hashtags
and CTA. Check exact wording, dimensions, colour consistency, complete
objects, empty reserved areas and identical anchors across all slides.
```

## 7. Reformiqo example — brand settings only

These are the current approved brand settings, not hardcoded rules for every brand:

```text
BRAND_NAME = Reformiqo
ACCENT_COLOR = #3687C8
LIGHT_BACKGROUND = #FFFFFF
DARK_BACKGROUND = #2D2E30
TEXT_ON_LIGHT = #2D2E30
TEXT_ON_DARK = #FFFFFF
SUPPORTING_COLORS = approved blues, greys and white
HEADLINE_FONT = Poppins Bold
BODY_FONT = IBM Plex Sans
LABEL_FONT = IBM Plex Mono
BRAND_LOGO_MODE = reserve_only
BRAND_LOGO_ASSET = empty
PARTNER_LOGO_MODE = reserve_only
PARTNER_1_NAME = Zoho Certified Partner
PARTNER_2_NAME = ERPNext Certified Partner
PARTNER_1_ASSET = empty
PARTNER_2_ASSET = empty
CONTACT_TEXT = connect@reformiqo.com
FOOTER_TEXT = Your Vision, Our Execution.
AUDIENCE = busy manufacturing and trading-business owners
BRAND_VOICE = clear, practical, calm and professional
LANGUAGE = English
VISUAL_STYLE = clean 3D illustrations using the approved palette
APPROVED_PROOF = optional; include only supplied, verified facts
```

## 8. Final checks

- All brand and post variables are filled or intentionally empty.
- Every export is exactly 1080 × 1350 and decodes completely.
- Text fits its assigned boxes with the fixed sizes and line counts.
- Numbers and shared text blocks line up when slides are viewed side by side.
- No accidental logos, misspellings, clipped objects or stretched artwork.
- Reserved logo areas follow the selected mode; the partner band appears on every static and final carousel slide.
- Static counters are omitted; carousel counters match the actual slide order and total.
- Caption, hashtags and CTA match the content and intended audience.
