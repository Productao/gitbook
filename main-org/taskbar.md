---
description: Actions available in the Main Org taskbar
hidden: false
---

# Taskbar (Main Org)

The taskbar provides view controls and analysis tools. All Main Org actions are **view-only** — to make changes, create a Scenario.

## Available Tools

**Search (🔍)** — Find employees or positions by name or title. Click to navigate to that position in the org chart. Shortcut: Cmd/Ctrl+K or `/`.

**Filter** — Show only positions matching specific criteria (Department, Location, Pay Grade, etc.). Enable **Manager Filtering** to preserve hierarchy context — filtered positions show with their managers above. Filters persist across org chart, directory, and forecast views.

**Tree View** — Display org structure as an indented hierarchical list. Useful for browsing deep hierarchies without expanding cards.

**Highlight** — Color-code cards by any attribute (Department, Location, Pay Grade, custom fields). Toggle between fill color and outline color; show legend for reference. Use both fill and outline together to highlight two attributes simultaneously.

**Card Content** — Control which fields appear on each position card (standard fields, custom fields, calculated FX fields like SOC and Layer). Drag to reorder fields; changes apply immediately.

**Spotlight** — Dim non-matching positions to focus attention. Select a rule (e.g., Direct SOC = 1–2) to highlight only positions meeting that criteria while graying out others. Use for presentations and structural analysis.

**Presets (Saved Views)** — Save and recall filter/highlight/card content configurations. Configure your view > Presets > Save Current View > name it. Available to other users based on permissions.

**Export** — Export in JPEG (screenshot of current view), PowerPoint (one slide per manager, configurable depth and layout), or CSV (raw data, respects active filters and visible columns).

**Layout** — Switch between Vertical, Horizontal, and Compact layouts. Control visible levels (1, 2, or 3 levels expanded). Fit to screen and zoom controls.

**Directory Toggle** — Switch to spreadsheet/table view for sorting, filtering, and exporting data in tabular format.

## What's NOT Available in Main Org

Add, Edit, Move, Close positions; Assign employees; Bulk operations; Change Tracker; Comments.

To do any of these: create a Scenario.

## Main Org vs Scenario Taskbar

| Tool | Main Org | Scenarios |
|------|----------|-----------|
| Search, Filter, Highlight, Spotlight, Card Content, Export, Layout | ✅ | ✅ |
| Add/Edit/Move/Close positions | ❌ | ✅ |
| Bulk Operations | ❌ | ✅ |
| Change Tracker (👀) | ❌ | ✅ |
| Comments | ❌ | ✅ |
| Approvals | ❌ | ✅ |

## Keyboard Shortcuts

`1` = Main Org, `3` = Org Chart, `5` = Directory, Cmd/Ctrl+K or `/` = Search, Esc = Close panels

## Related Articles

- [Navigation](navigation.md)
- [Directory View](directory-view.md)
- [Metrics & Insights](metrics-insights.md)
- [Creating a Scenario](../scenarios/creating-scenarios.md)
