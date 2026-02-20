---
description: How to navigate and explore the org chart
hidden: false
---

# Orientation & Navigation

All navigation features are in the left toolbar. For actions available in Main Org vs Scenarios, see [Taskbar](taskbar.md).

## Left Toolbar Tools

**Search** — Find employees or positions by name or job title. Results navigate the org chart to that position. Works across your entire accessible scope. Shortcut: Cmd/Ctrl+K or `/`.

**Filter** — Show only positions matching specific criteria (Department, Location, Pay Grade, custom fields). Two modes:
- **Standard Filtering** — Shows only matching positions; may break visual hierarchy
- **Manager Filtering (recommended)** — Preserves hierarchy by showing managers above filtered positions even if they don't match the filter

Clear all filters: Filter icon > Clear All (or remove individual filter tags).

**Tree View** — Org structure as an indented list. Click any name to navigate to that position. Faster than expanding cards one-by-one for deep hierarchies.

**Highlight** — Color-code cards by any attribute. Use Fill Color for one attribute and Outline Color for another simultaneously to show two dimensions at once. Toggle the legend to see color meanings.

**Card Content** — Control which fields appear on position cards (standard fields, custom fields, calculated FX fields like SOC and Layer). Drag to reorder. Keep cards minimal — 3–5 fields for readability; add more only for specific analysis.

**Spotlight** — Dim non-matching positions to focus on criteria: Direct SOC = 1–2, pay grade range, location, etc. Blue = matching; gray = everything else. Combine with Highlight for powerful presentations.

**Presets (Saved Views)** — Save and reload configurations (filters + highlights + card content). Configure view > Presets > Save Current View > name it. Other users can access your presets based on permissions.

**Export** — JPEG (screenshot), PowerPoint (one slide per manager, configurable depth), CSV (all data), Template Builder (admin only).

**Layout** — Switch between Vertical (top-down), Horizontal (left-right), and Compact (two-column) layouts. Control expanded levels (1–3). Fit to screen; zoom in/out; pan by clicking and dragging.

## Keyboard Shortcuts

`1` = Main Org, `5` = Directory, `/` or Cmd/Ctrl+K = Search, Esc = Close panels

## Navigation Best Practices

- Use Search or Filter instead of manually browsing large orgs
- Use Manager Filtering to maintain hierarchy context when filtering
- Combine Highlight + Spotlight: Highlight by Department, Spotlight by SOC = 1–2
- Clear filters between sessions — they carry over to other modules
- Save Presets for recurring analysis (don't reconfigure the same view repeatedly)

## Common Workflows

**Find a specific person:** Search > type name > select.

**Analyze a department:** Filter > Department > enable Manager Filtering > Apply. Add Highlight by Location or Pay Grade.

**Identify compression:** Spotlight > Direct SOC = 1–2 > review blue-highlighted positions.

**Prepare a presentation:** Filter to relevant area > Highlight by attribute > Export PowerPoint.

## Related Articles

- [Taskbar (Main Org)](taskbar.md)
- [Directory View](directory-view.md)
- [Org Metrics & Insights](metrics-insights.md)
