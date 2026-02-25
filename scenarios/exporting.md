---
description: Exporting scenario data and visuals
icon: download
---

# 📤 Exporting Scenario Data

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

* Filters (department, location)
* Hierarchy depth (top 3 layers, full org, or custom)
* Layout (Vertical, Horizontal, Compact)
* Slide depth (layers per slide)
* Card content (Titles only or full details)

Best for executive and board presentations. Each manager with direct reports gets its own slide.

> Tip: Export in "Show Before" and "Show After" modes separately to create side-by-side comparison slides.

## Data Exports

**CSV / Excel (Directory)** — Export position data from Directory view:

1. Switch to **Directory** view
2. Click the **column selector** (top-right) to choose which fields to include
3. Drag columns to reorder them how you want
4. Apply filters to limit which positions export
5. Click **Export** > **CSV** or **Excel**

**Saved Reports:** After configuring columns and order, click **Save Report** to save this configuration for future use. Access saved reports from the Reports dropdown.

> **Note:** Directory exports are less commonly used. Most users prefer org chart PowerPoint or change summaries for stakeholder communication.

**Change Summary** — Exportable directly from the OpEx Panel panel. Includes every changed position with change type, before/after values, cost impact, and effective date.

**Forecast export** — From Forecast view: configure time period, aggregation, and metric, then export the projection table. Shows headcount/cost by department over time with phasing based on effective dates.

**Workforce Hub** — Export individual charts as PNG, or create slide packs with multiple charts. See [Hub Packs](../hub/packs.md) for creating PowerPoint presentations with multiple analytics charts.

## Export by Use Case

**For approval submission:** Change summary (Excel) + Org chart PowerPoint ("Show After") + Forecast cost projection

**For stakeholder communication:** JPEG or filtered PowerPoint + Change summary filtered to relevant department

**For implementation planning:** Full change list (CSV) + Positions sorted by effective date

**For financial analysis:** Forecast export (cost by quarter) + Change summary (cost per change) + Excel of all positions with salaries

## Comparison Exports

In Scenario Comparisons view, click **Export Comparison** to download a side-by-side summary of compared scenarios.

**Available formats:**

* **Excel** — Multi-sheet file with a Summary sheet (scenario names, net headcount/cost per scenario), Department Breakdown (headcount and cost by department per scenario), and Change Detail (all position changes with before/after values)
* **CSV** — Single file with one row per position/metric, columns for each compared scenario
* **PowerPoint** — Side-by-side org charts with a summary slide

Export before the decision point to capture the state at that moment. Filter before exporting to focus stakeholders on the relevant segment.

## Troubleshooting

| Problem                             | Solution                                                      |
| ----------------------------------- | ------------------------------------------------------------- |
| Export button grayed out            | Verify your role has export access; contact scenario owner    |
| Exported data doesn't match screen  | Check active view mode (Before/After/Changes) and filters     |
| Change summary is empty             | Scenario may have no changes; verify OpEx Panel shows changes |
| Effective dates missing from export | Export from Forecast view or use Change Summary export        |

## Related Articles

* [Main Org Exporting](../main-org/exporting.md)
* [Scenario Comparisons](comparisons.md)
* [Forecast Reports & Exports](../forecast/reports-exports.md)
