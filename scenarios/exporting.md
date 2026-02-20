---
description: Exporting scenario data and visuals
icon: download
---

# Scenario Exporting

Export scenario data, visuals, and analytics for stakeholder presentations, approval documentation, and analysis.

## Export Formats Available

**Visual:** JPEG (org chart screenshot), PowerPoint (full hierarchical slides), PNG (Workforce Hub charts)

**Data:** CSV, Excel, Change Summary, Forecast projections

## How to Export

All exports follow the same pattern:
1. Open scenario
2. Switch to the relevant view (Org Chart, Directory, Forecast, or Workforce Hub)
3. Set view mode (Before / After / Changes)
4. Apply any filters
5. Click **Export** and select format

Exports respect your current view mode, active filters, and access permissions.

## Org Chart Exports

**JPEG** — Screenshot of the current framed view. Good for quick visual updates in email or Slack.

**PowerPoint** — Full org chart as structured slides. Configure:
- Filters (department, location)
- Hierarchy depth (top 3 layers, full org, or custom)
- Layout (Vertical, Horizontal, Compact)
- Slide depth (layers per slide)
- Card content (Titles only or full details)

Best for executive and board presentations. Each manager with direct reports gets its own slide.

> Tip: Export in "Show Before" and "Show After" modes separately to create side-by-side comparison slides.

## Data Exports

**CSV / Excel** — All positions from the "Show After" state (or whichever view mode is active), one row per position. Includes change indicators (added/removed/modified). Switch to Directory view, apply filters, then export to control exactly which columns and rows are included.

**Change Summary** — Exportable directly from the Change Tracker panel. Includes every changed position with change type, before/after values, cost impact, and effective date.

**Forecast export** — From Forecast view: configure time period, aggregation, and metric, then export the projection table. Shows headcount/cost by department over time with phasing based on effective dates.

**Workforce Hub** — Export charts as PNG for presentations, or underlying data as CSV/Excel for analysis.

## Export by Use Case

**For approval submission:** Change summary (Excel) + Org chart PowerPoint ("Show After") + Forecast cost projection

**For stakeholder communication:** JPEG or filtered PowerPoint + Change summary filtered to relevant department

**For implementation planning:** Full change list (CSV) + Positions sorted by effective date

**For financial analysis:** Forecast export (cost by quarter) + Change summary (cost per change) + Excel of all positions with salaries

## Comparison Exports

In Scenario Comparisons view, click **Export** to download a side-by-side summary (PDF for presentations, CSV/Excel for analysis) of all compared scenarios.

**Learn more:** [Scenario Comparison Exporting](comparison-exporting.md)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Export button grayed out | Verify your role has export access; contact scenario owner |
| Exported data doesn't match screen | Check active view mode (Before/After/Changes) and filters |
| Change summary is empty | Scenario may have no changes; verify Change Tracker shows changes |
| Effective dates missing from export | Export from Forecast view or use Change Summary export |
| Can't export comparison | Ensure multiple scenarios are selected in comparison view |

## Related Articles

- [Main Org Exporting](../main-org/exporting.md)
- [Scenario Comparisons](comparisons.md)
- [Forecast Reports & Exports](../forecast/reports-exports.md)
