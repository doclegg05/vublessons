#!/usr/bin/env python3
"""Build the Week 1 class file "Community Supper Flyer.docx" (Mission 1C) with the standard library only.

Mission 1C teaches: in Word's print preview the flyer shows "1 of 2" with Normal margins (only the last line on
page 2); choosing Narrow margins makes it "1 of 1". The text mirrors the Unit C demo in os/demos/week-01.js.

Every paragraph is one short line with EXACT line spacing (w:lineRule="exact", w:before="0"), so the page math does
not depend on the font Word finds, and nothing wraps (the widest line, the title, is ~406pt in Arial at 44pt bold;
the text column is 468pt at Normal margins and 540pt at Narrow).

Letter page, 11in = 792pt tall. Normal margins (1in) leave 792 - 72 - 72 = 648pt of body; Narrow (0.5in) leave
792 - 36 - 36 = 720pt.

  title      line 56 + after 16 =  72    running   72
  date       line 22 + after  8 =  30    running  102
  dots       line 20 + after 28 =  48    running  150
  8 lines    (line 30 + after 30) x 8   running  630   (the 8th line ends at 600, 48pt above the page end)
  last line  line 34               ->   630 to 664

Normal: the last line would end at 664 > 648, so Word moves exactly that one line to page 2 ("1 of 2").
Narrow: everything ends at 664 <= 720, with 56pt to spare ("1 of 1").

Run from the repository root:  python3 docs/digital-literacy-2/class-files/make-community-supper-flyer.py
"""
import os
import zipfile
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(ROOT, "courses", "digital-literacy-2", "weeks", "week-01", "files", "Community Supper Flyer.docx")

NAVY, GOLD, GOLD_DARK, INK = "1B365D", "C9A227", "8A6D12", "15213A"
LINES = [
    "Free supper for veterans and families",
    "Roast chicken, green beans, potatoes",
    "Apple pie, coffee and sweet tea",
    "Doors open at 5:00 PM",
    "Bring a friend or a neighbor",
    "Rides: sign up at the front desk",
    "Tell a volunteer about food allergies",
    "Hosted by the Community Skills Desk",
]
# (text, font pt, line pt, after pt, bold, color)
PARAS = (
    [("Community Supper", 44, 56, 16, True, NAVY),
     ("Thursday, October 8 · 5:30 PM · Grace Fellowship Hall", 14, 22, 8, True, GOLD_DARK),
     ("•     •     •", 14, 20, 28, False, GOLD)]
    + [(t, 20, 30, 30, False, INK) for t in LINES]
    + [("Questions? Call (555) 010-0148", 22, 34, 0, True, NAVY)]
)
BODY_NORMAL, BODY_NARROW = 648, 720


def check_layout():
    """Fail loudly if an edit breaks the Mission 1C page math."""
    y, starts = 0, []
    for i, (_, _, line, after, _, _) in enumerate(PARAS):
        if y and y + line > BODY_NORMAL:
            starts.append(i)
            y = 0
        y += line + after
    total = sum(p[2] + p[3] for p in PARAS) - PARAS[-1][3]
    assert starts == [len(PARAS) - 1], f"Normal margins must spill only the last line, got page starts {starts}"
    assert total <= BODY_NARROW - 40, f"Narrow margins must fit with room to spare, total {total}pt"
    return total


def paragraph(text, size, line, after, bold, color):
    rpr = ('<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>' + ("<w:b/>" if bold else "")
           + f'<w:color w:val="{color}"/><w:sz w:val="{size * 2}"/><w:szCs w:val="{size * 2}"/></w:rPr>')
    # Schema order inside w:pPr matters to Word: spacing, then jc, then the paragraph-mark rPr.
    return (f'<w:p><w:pPr><w:spacing w:before="0" w:after="{after * 20}" '
            f'w:line="{line * 20}" w:lineRule="exact"/><w:jc w:val="center"/>{rpr}</w:pPr>'
            f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>')


W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
DOCUMENT = (
    f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:document {W}><w:body>'
    + "".join(paragraph(*p) for p in PARAS)
    + '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
      '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>'
      '<w:cols w:space="720"/></w:sectPr></w:body></w:document>'
)
STYLES = (
    f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:styles {W}>'
    '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:eastAsia="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>'
    '<w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="en-US"/></w:rPr></w:rPrDefault>'
    '<w:pPrDefault><w:pPr><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
    '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>'
    '</w:styles>'
)
SETTINGS = (
    f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:settings {W}><w:zoom w:percent="100"/>'
    '<w:defaultTabStop w:val="720"/><w:characterSpacingControl w:val="doNotCompress"/>'
    '<w:compat><w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat>'
    '</w:settings>'
)
CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
    '<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
    '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
    '</Types>'
)
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PACKAGE_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    f'<Relationship Id="rId1" Type="{REL}/officeDocument" Target="word/document.xml"/>'
    '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
    '</Relationships>'
)
DOCUMENT_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    f'<Relationship Id="rId1" Type="{REL}/styles" Target="styles.xml"/>'
    f'<Relationship Id="rId2" Type="{REL}/settings" Target="settings.xml"/>'
    '</Relationships>'
)
CORE = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
    'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
    'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
    '<dc:title>Community Supper Flyer</dc:title><dc:creator>VUB Digital Literacy Level 2 (practice file)</dc:creator>'
    '<dcterms:created xsi:type="dcterms:W3CDTF">2026-09-28T00:00:00Z</dcterms:created>'
    '<dcterms:modified xsi:type="dcterms:W3CDTF">2026-09-28T00:00:00Z</dcterms:modified>'
    '</cp:coreProperties>'
)
PARTS = [
    ("[Content_Types].xml", CONTENT_TYPES), ("_rels/.rels", PACKAGE_RELS), ("docProps/core.xml", CORE),
    ("word/document.xml", DOCUMENT), ("word/_rels/document.xml.rels", DOCUMENT_RELS),
    ("word/styles.xml", STYLES), ("word/settings.xml", SETTINGS),
]


def main():
    total = check_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for name, xml in PARTS:
            info = zipfile.ZipInfo(name, date_time=(2026, 9, 28, 0, 0, 0))  # fixed time: byte-identical rebuilds
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, xml.encode("utf-8"))
    print(f"wrote {os.path.relpath(OUT, ROOT)}: {total}pt of lines; Normal body {BODY_NORMAL}pt, Narrow {BODY_NARROW}pt")


if __name__ == "__main__":
    main()
