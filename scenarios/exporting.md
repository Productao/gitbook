---
description: Exporting scenario data and visuals
icon: download
---

# 📤 Exporting Scenario Data

## Exporting Scenario Data

Export scenario data, visuals, and analytics for stakeholder presentations, approval documentation, and analysis.

## Export Formats Available

**Visual:** JPEG (org chart screenshot), PowerPoint (full hierarchical slides), PNG (Workforce Hub charts)

**Data:** CSV, Excel, Change Summary, Forecast projections

## How to Export

All exports follow the same pattern:

1. Open the scenario
2. Switch to the relevant module (Org Chart, Directory, Forecast, or Workforce Hub)
3. Set the view mode (Before / After / Changes)
4. Apply any filters
5. Click **Export** and select a format

**Note:** Exports respect your current view mode, active filters, and access permissions.

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 3.49.21 PM.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 3.49.55 PM.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 3.49.44 PM.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 3.50.09 PM.png" alt=""><figcaption></figcaption></figure>

## Org Chart Exports

**JPEG** - Screenshot of the current framed view. Good for quick visual updates in email or Slack.

**PowerPoint** - Full org chart as structured slides. Configure:

* Filters (department, location)
* Hierarchy depth (top 3 layers, full org, or custom)
* Layout (Vertical, Horizontal, Compact)
* Slide depth (layers per slide)
* Card content (Titles only or full details)

Best for executive and board presentations. Each manager with direct reports gets their own slide.

**Tip:** Export in "Main org" and "Scenario" orgchart separately to create side-by-side comparison slides.

**Note:** If the report contains a large volume of data, the export may not generate immediately. In such cases, you will see a notification (as shown in the screenshots) indicating that the file is being processed. Once the PowerPoint file is ready, you will receive an email with access to download the exported file.

<figure><img src="../.gitbook/assets/image (92).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (93).png" alt=""><figcaption></figcaption></figure>

## Data Exports

**CSV / Excel (Directory)** - Export position data in CSV. Click on Download CSV from your side panel:

1. Click on Download CSV from your side panel
2. Click the column selector in export to choose which fields to include
3. Select columns to include
4. Apply filters to limit which positions export
5. Click **Download**

**Saved Reports** - After configuring columns and order, click **Save Report** to save the configuration for future use. Access saved reports from the **Download CSV** dropdown.

Note: CSV exports are less commonly used. Most users prefer org chart PowerPoint or change summaries for stakeholder communication.

**Comparison CSV** - Comparison CSV directly form the side panel inside a scenario. Includes every changed position with change type, before/after values, cost impact, and effective date.

**Forecast export** - From Forecast view, configure time period, aggregation, and metric, then export the projection table. Shows headcount and cost by department over time, phased by effective dates.

**Workforce Hub** - Export individual charts as PNG, or create slide packs with multiple charts. See [Hub Packs](../hub/packs.md) for creating PowerPoint presentations with multiple analytics charts.

## Export by Use Case

**For approval submission** - Comparison CSV (Excel) + Org chart PowerPoint ("Show After") + Forecast cost projection

**For stakeholder communication** - JPEG or filtered PowerPoint + Comparison CSV filtered to the relevant department

**For implementation planning** - Full change list (CSV) + positions sorted by effective date

**For financial analysis** - Forecast export (cost by quarter) + Comparison CSV (cost per change) + Excel of all positions with salaries

## Troubleshooting

| Problem                             | Solution                                                        |
| ----------------------------------- | --------------------------------------------------------------- |
| Export button grayed out            | Verify your role has export access — contact the scenario owner |
| Exported data doesn't match screen  | Check the active view mode (Before/After/Changes) and filters   |
| Effective dates missing from export | Export from Forecast view or use the Comparison CSV export      |

## Related Articles

* [Main Org Exporting](../main-org/exporting.md)
* [Scenario Comparisons](comparisons.md)
* [Forecast Reports & Exports](../forecast/overview.md)
