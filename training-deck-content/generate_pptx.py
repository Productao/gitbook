"""
Agentnoon Training Deck — PowerPoint Generator

Reads slide content from the markdown files in training-deck-content/
and generates a branded .pptx using the company slide master.

Color scheme:
  - Color "3" (prefix 3_) for section dividers (H1 — Part transitions)
  - Color "2" (prefix 2_) for content slides within sections (H2 — individual slides)

Layout mapping:
  - Title slide:              3_Title_Slide_1  (layout idx 2)
  - Section dividers:         3_Section_Title_1 (layout idx 34) — color "3"
  - Content + screenshot:     Picture_Copy_1    (layout idx 67) — no prefix (default)
  - Content + screenshot alt: 2_Picture_Copy_2  (layout idx 68) — color "2"
  - Full-width content:       Header, Copy, Pattern (layout idx 55) — no prefix
  - Full-width content alt:   2_Header, Copy, Pattern (layout idx 57) — color "2"
  - Thank you:                Thank you 5       (layout idx 101)
"""

import os
import re
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN

# ── Paths ────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
TEMPLATE = BASE_DIR / "slide-master.pptx"
ASSETS_DIR = BASE_DIR.parent / ".gitbook" / "assets"
OUTPUT = BASE_DIR / "Agentnoon_Training_Deck.pptx"

# ── Layout indices (from template inspection) ────────────────────────────
LAYOUT_TITLE_SLIDE = 2         # 3_Title_Slide_1
LAYOUT_SECTION_DIVIDER = 34    # 3_Section_Title_1 (color 3)
LAYOUT_PICTURE_COPY = 67       # Picture_Copy_1 (default color)
LAYOUT_PICTURE_COPY_ALT = 68   # 2_Picture_Copy_2 (color 2)
LAYOUT_FULL_CONTENT = 55       # Header, Copy, Pattern (default)
LAYOUT_FULL_CONTENT_ALT = 57   # 2_Header, Copy, Pattern (color 2)
LAYOUT_THANK_YOU = 101         # Thank you 5

# ── Screenshot mapping ───────────────────────────────────────────────────
# Maps slide filenames to screenshot assets (from .gitbook/assets/)
# Only include confident mappings referenced explicitly in the docs.
SCREENSHOT_MAP = {
    # Part 1
    "slide-03-what-is-agentnoon.md": "Screenshot 2026-02-24 at 2.08.16 PM.png",
    "slide-06-logging-in.md": "Screenshot 2026-02-24 at 2.08.16 PM.png",
    # Part 2
    "slide-07-positions-vs-people.md": "Screenshot 2026-02-26 at 9.33.39 AM.png",
    "slide-09-cards-org-chart.md": "Screenshot 2026-02-26 at 9.57.10 AM.png",
    "slide-10-fields-attributes.md": "Screenshot 2026-02-27 at 1.55.20 AM.png",
    "slide-11-spans-layers.md": "Screenshot 2026-02-26 at 9.59.43 AM.png",
    "slide-12-views-org-directory.md": "Screenshot 2026-02-26 at 9.38.48 AM.png",
    # Part 3
    "slide-14-entering-main-org.md": "Screenshot 2026-02-24 at 1.02.21 PM.png",
    "slide-15-navigating-org-chart.md": "Screenshot 2026-02-24 at 1.02.21 PM.png",
    "slide-17-filtering-highlighting.md": "Screenshot 2026-02-24 at 1.38.23 PM.png",
    "slide-18-card-content.md": "Screenshot 2026-02-27 at 1.50.36 AM.png",
    "slide-19-spotlight-saved-views.md": "Screenshot 2026-02-24 at 2.28.32 PM.png",
    # Part 4
    "slide-22-creating-a-scenario.md": "Screenshot 2026-02-24 at 1.24.21 PM.png",
    "slide-24-adding-a-position.md": "Screenshot 2026-02-24 at 3.57.01 PM.png",
    "slide-25-editing-a-position.md": "Screenshot 2026-02-24 at 4.03.19 PM.png",
    "slide-26-moving-a-position.md": "Screenshot 2026-02-24 at 4.58.33 PM.png",
    # Part 5
    "slide-35-forecast-impact.md": "Screenshot 2026-02-26 at 9.04.29 AM.png",
    "slide-37-workforce-hub-validation.md": "Screenshot 2026-02-26 at 10.27.52 AM.png",
    # Part 7
    "slide-46-exporting-charts.md": "Screenshot 2026-02-26 at 9.13.06 AM.png",
}

# ── Section definitions (for divider slides) ─────────────────────────────
SECTIONS = {
    "01-part-1-welcome": ("01", "Welcome & Orientation"),
    "02-part-2-key-concepts": ("02", "Key Concepts"),
    "03-part-3-main-org": ("03", "Navigating Main Org"),
    "04-part-4-your-first-scenario": ("04", "Your First Scenario"),
    "05-part-5-reviewing-impact": ("05", "Reviewing Impact"),
    "06-part-6-collaboration-approvals": ("06", "Collaboration & Approvals"),
    "07-part-7-exporting": ("07", "Exporting & Communicating"),
    "08-part-8-wrap-up": ("08", "Wrap-Up"),
    "09-appendix-a-feature-briefings": ("A", "Appendix A: Feature Briefings"),
    "10-appendix-b-admin-capabilities": ("B", "Appendix B: Admin Capabilities"),
    "11-appendix-c-quick-reference": ("C", "Appendix C: Quick Reference"),
    "12-appendix-u-use-cases": ("U", "Appendix U: Use Case Quick References"),
}

# Slides that should use full-width layout (no screenshot)
FULL_WIDTH_SLIDES = {
    "slide-01-title.md",      # uses title slide layout instead
    "slide-02-how-to-use.md",
    "slide-05-modules-work-together.md",
    "slide-20-main-org-takeaways.md",
    "slide-32-scenario-recap.md",
    "slide-38-impact-review-takeaways.md",
    "slide-50-getting-help.md",  # uses thank you layout instead
    "slide-C01-keyboard-shortcuts.md",
    "slide-C02-glossary.md",
}


def parse_slide_md(filepath):
    """Parse a slide markdown file and extract structured content."""
    text = filepath.read_text(encoding="utf-8")

    title = ""
    leadline = ""
    bullets = []
    speaker_notes = ""

    # Extract title (first ## Title section)
    m = re.search(r"^## Title\s*\n(.+?)$", text, re.MULTILINE)
    if m:
        title = m.group(1).strip()

    # Extract lead-line
    m = re.search(r"^## Lead-line\s*\n(.+?)$", text, re.MULTILINE)
    if m:
        leadline = m.group(1).strip()

    # Extract key details / content bullets
    # Look for ## Key Details or ## What Is It? sections
    details_match = re.search(
        r"^## (?:Key Details|What Is It\?|How to Set It Up|Step-by-Step Workflow)\s*\n(.*?)(?=\n## |\Z)",
        text, re.MULTILINE | re.DOTALL
    )
    if not details_match:
        details_match = re.search(
            r"^## Key Details\s*\n(.*?)(?=\n## |\Z)",
            text, re.MULTILINE | re.DOTALL
        )

    if details_match:
        raw = details_match.group(1).strip()
        # Extract top-level bullets (lines starting with -)
        for line in raw.split("\n"):
            line = line.strip()
            if line.startswith("- **") or line.startswith("- "):
                # Clean markdown formatting for pptx
                bullet = line.lstrip("- ").strip()
                # Remove bold markers but keep the text
                bullet = re.sub(r"\*\*(.+?)\*\*", r"\1", bullet)
                bullets.append(bullet)

    # For appendix slides, also grab "How to Use It" bullets
    use_match = re.search(
        r"^## How to Use It\s*\n(.*?)(?=\n## |\Z)",
        text, re.MULTILINE | re.DOTALL
    )
    if use_match and not bullets:
        raw = use_match.group(1).strip()
        for line in raw.split("\n"):
            line = line.strip()
            if line.startswith("- ") or re.match(r"^\d+\.", line):
                bullet = re.sub(r"^\d+\.\s*", "", line.lstrip("- ").strip())
                bullet = re.sub(r"\*\*(.+?)\*\*", r"\1", bullet)
                bullets.append(bullet)

    # Extract speaker notes
    notes_match = re.search(
        r"^## Speaker Notes\s*\n(.*?)(?=\n## |\Z)",
        text, re.MULTILINE | re.DOTALL
    )
    if notes_match:
        speaker_notes = notes_match.group(1).strip()

    return {
        "title": title,
        "leadline": leadline,
        "bullets": bullets[:6],  # Cap at 6 bullets to avoid overflow
        "speaker_notes": speaker_notes,
    }


def add_title_slide(prs, data):
    """Add the branded title slide (slide 1)."""
    layout = prs.slide_masters[0].slide_layouts[LAYOUT_TITLE_SLIDE]
    slide = prs.slides.add_slide(layout)

    for ph in slide.placeholders:
        idx = ph.placeholder_format.idx
        if idx == 0:  # Title
            ph.text = data["title"]
        elif idx == 1:  # Subtitle
            ph.text = data["leadline"]
        elif idx == 13:  # Footer text
            ph.text = "Confidential — Internal Use Only"

    if data["speaker_notes"]:
        slide.notes_slide.notes_text_frame.text = data["speaker_notes"]

    return slide


def add_section_divider(prs, number, section_title):
    """Add a section divider slide."""
    layout = prs.slide_masters[0].slide_layouts[LAYOUT_SECTION_DIVIDER]
    slide = prs.slides.add_slide(layout)

    for ph in slide.placeholders:
        idx = ph.placeholder_format.idx
        if idx == 0:  # Title
            ph.text = section_title
        elif idx == 10:  # Section number
            ph.text = number

    return slide


def add_content_slide_with_picture(prs, data, image_path=None, use_alt_color=False):
    """Add a content slide with bullets left and picture right."""
    layout_idx = LAYOUT_PICTURE_COPY_ALT if use_alt_color else LAYOUT_PICTURE_COPY
    layout = prs.slide_masters[0].slide_layouts[layout_idx]
    slide = prs.slides.add_slide(layout)

    # Build the body text: lead-line + bullets
    body_parts = []
    if data["leadline"]:
        body_parts.append(data["leadline"])
        body_parts.append("")  # blank line separator
    for b in data["bullets"]:
        body_parts.append(f"• {b}")

    body_text = "\n".join(body_parts)

    for ph in slide.placeholders:
        idx = ph.placeholder_format.idx
        if idx == 0:  # Title
            ph.text = data["title"]
        elif idx in (1, 36):  # Content/Object (body) — idx differs between layouts
            tf = ph.text_frame
            tf.clear()
            # Add lead-line as first paragraph (slightly different style)
            if data["leadline"]:
                p = tf.paragraphs[0]
                run = p.add_run()
                run.text = data["leadline"]
                run.font.italic = True
                run.font.size = Pt(12)
            # Add bullets
            for bullet in data["bullets"]:
                p = tf.add_paragraph()
                run = p.add_run()
                run.text = f"• {bullet}"
                run.font.size = Pt(11)

    # Insert screenshot if available
    if image_path and os.path.exists(image_path):
        for ph in slide.placeholders:
            if ph.placeholder_format.idx in (35, 37):  # Picture placeholder
                ph.insert_picture(str(image_path))
                break

    if data["speaker_notes"]:
        slide.notes_slide.notes_text_frame.text = data["speaker_notes"]

    return slide


def add_full_width_slide(prs, data, use_alt_color=False):
    """Add a full-width content slide (no picture)."""
    layout_idx = LAYOUT_FULL_CONTENT_ALT if use_alt_color else LAYOUT_FULL_CONTENT
    layout = prs.slide_masters[0].slide_layouts[layout_idx]
    slide = prs.slides.add_slide(layout)

    for ph in slide.placeholders:
        idx = ph.placeholder_format.idx
        if idx == 0:  # Title
            ph.text = data["title"]
        elif idx == 36:  # Content/Object (body)
            tf = ph.text_frame
            tf.clear()
            if data["leadline"]:
                p = tf.paragraphs[0]
                run = p.add_run()
                run.text = data["leadline"]
                run.font.italic = True
                run.font.size = Pt(14)
                p = tf.add_paragraph()  # blank line
            for bullet in data["bullets"]:
                p = tf.add_paragraph()
                run = p.add_run()
                run.text = f"• {bullet}"
                run.font.size = Pt(12)

    if data["speaker_notes"]:
        slide.notes_slide.notes_text_frame.text = data["speaker_notes"]

    return slide


def add_thank_you_slide(prs, data):
    """Add the closing/thank you slide."""
    layout = prs.slide_masters[0].slide_layouts[LAYOUT_THANK_YOU]
    slide = prs.slides.add_slide(layout)

    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:  # Title
            ph.text = data["title"]

    if data["speaker_notes"]:
        slide.notes_slide.notes_text_frame.text = data["speaker_notes"]

    return slide


def generate_deck(sections_to_include=None):
    """
    Generate the training deck.

    Args:
        sections_to_include: List of section folder names to include,
                             or None for all sections.
    """
    prs = Presentation(str(TEMPLATE))

    # Remove existing example slides using XML manipulation
    sldIdLst = prs.slides._sldIdLst
    for sldId in list(sldIdLst):
        rId = sldId.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        if rId is None:
            rId = sldId.get("r:id")
        if rId:
            prs.part.drop_rel(rId)
        sldIdLst.remove(sldId)

    # Get all section directories in order
    section_dirs = sorted([
        d for d in BASE_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    ])

    if sections_to_include:
        section_dirs = [d for d in section_dirs if d.name in sections_to_include]

    for section_dir in section_dirs:
        section_key = section_dir.name
        if section_key not in SECTIONS:
            continue

        sec_number, sec_title = SECTIONS[section_key]

        # Get slide files in order
        slide_files = sorted([
            f for f in section_dir.iterdir()
            if f.suffix == ".md" and f.name.startswith("slide-")
        ])

        if not slide_files:
            continue

        # Add section divider (except for Part 1 where the title slide serves this purpose)
        if section_key != "01-part-1-welcome":
            add_section_divider(prs, sec_number, sec_title)

        # Add each slide
        for slide_file in slide_files:
            data = parse_slide_md(slide_file)
            if not data["title"]:
                continue

            fname = slide_file.name

            # Determine screenshot path
            screenshot = SCREENSHOT_MAP.get(fname)
            image_path = ASSETS_DIR / screenshot if screenshot else None

            # Route to correct slide type
            if fname == "slide-01-title.md":
                add_title_slide(prs, data)
            elif fname == "slide-50-getting-help.md":
                add_thank_you_slide(prs, data)
            elif fname in FULL_WIDTH_SLIDES:
                add_full_width_slide(prs, data, use_alt_color=False)
            elif screenshot and image_path and image_path.exists():
                # Has a screenshot → picture + copy layout
                add_content_slide_with_picture(prs, data, image_path, use_alt_color=False)
            else:
                # No screenshot available → picture layout with empty placeholder
                add_content_slide_with_picture(prs, data, image_path=None, use_alt_color=False)

    prs.save(str(OUTPUT))
    print(f"Generated: {OUTPUT}")
    print(f"Total slides: {len(prs.slides)}")


if __name__ == "__main__":
    # Generate just the first few sections as a test
    generate_deck(sections_to_include=[
        "01-part-1-welcome",
        "02-part-2-key-concepts",
        "03-part-3-main-org",
    ])
