---
description: Exporting data and visuals from Main Org
icon: download
---

# 📤 Exporting Data

You can export organizational data and visuals from Main Org for reporting, analysis, and presentations.

Exports reflect your current view, including active filters and visible columns.

## Export Formats

#### Visual Exports

* **JPEG** — screenshot of the current org chart view
* **PowerPoint** — A structured org chart with configurable depth and layout

#### Data Exports

* **CSV** — Raw position and employee data
* **Excel** — Formatted spreadsheet export
* **EIB File** — Workday Enterprise Interface Builder format (admin only)
* **Template Exports** — Admin-configured export templates

## How to Export

1. Navigate to Main Org.
2. Apply filters if you want to export a subset of data.
3. Click **Export**.
4. Select your preferred format.
5. Configure export options (if applicable).
6. Download the file.

<figure><img src="../.gitbook/assets/Screenshot 2026-02-27 at 2.14.25 AM.png" alt=""><figcaption></figcaption></figure>

### PowerPoint Configuration

When exporting to PowerPoint, you can configure:

* Filters (department, location, etc.)
* Hierarchy depth
* Layout (vertical, horizontal, compact)
* Slide depth (layers per slide)
* Card content (titles only or full details)

Each manager with direct reports appears on a separate slide.

### Exporting from Directory&#x20;

For structured data control:

1. Switch to **Directory** view.
2. Select which columns to display.
3. Reorder columns if needed.
4. Apply filters.
5. Click **Export** and choose CSV or Excel.

<figure><img src="../.gitbook/assets/Screenshot 2026-02-27 at 2.15.49 AM.png" alt=""><figcaption></figcaption></figure>

Exports include visible columns and respect active filters.

**Saved Reports:** After configuring columns and order, click **Save Report** to save this configuration. Access saved reports from the Reports dropdown for consistent recurring exports.

> **Note:** Directory exports are less commonly used. Most users prefer PowerPoint org charts or Workforce Hub analytics for stakeholder presentations.

### Exporting from Forecast&#x20;

In Forecast view, you can export projection tables:

1. Configure the row aggregator, time period (Monthly, Quarterly, or Yearly), and metric (Headcount or Cost).
2. Click **Export**.
3. Download the table showing projected headcount or cost by time period.

<figure><img src="../.gitbook/assets/Screenshot 2026-02-27 at 2.17.19 AM.png" alt=""><figcaption></figcaption></figure>

Forecast exports reflect effective dates and hire dates used in scenarios.

**Learn more:** [Forecast Reports & Exports](../forecast/reports-exports.md)

### Exporting from Workforce Hub&#x20;

From Workforce Hub, you can export charts and underlying data:

* **PNG** — Export the chart as an image.
* **PowerPoint** — Export the chart as an editable slide.
* **CSV** — Export the underlying chart data (via table view).

For multi-chart presentations, use Slide Packs to generate a PowerPoint with multiple charts

**Learn more:** [Slide Packs](../hub/packs.md)

<figure><img src="../.gitbook/assets/Screenshot 2026-02-27 at 2.19.25 AM.png" alt=""><figcaption></figcaption></figure>

## Permissions

Exports respect your assigned Access Group.

You can only export data that you have permission to view. Fields restricted by your access scope will not appear in exported files. EIB exports are typically restricted to admins and HRIS teams.

## Troubleshooting

<table><thead><tr><th width="332.578125">Problem</th><th>Solution</th></tr></thead><tbody><tr><td>Export button unavailable</td><td>Verify export permissions with your administrator.</td></tr><tr><td>Empty file</td><td>Remove restrictive filters and try again.</td></tr><tr><td>Slow export</td><td>Filter to a smaller subset before exporting.</td></tr><tr><td>Missing columns</td><td>Confirm columns are visible before exporting. </td></tr></tbody></table>

**More help:** [Export & Integration Issues](../troubleshooting/export-integration-issues.md)

## Related Articles

* [Directory Exporting & Reporting](../directory/exporting-reporting.md)
* [Forecast Reports & Exports](../forecast/reports-exports.md)
* [Scenario Exporting](../scenarios/exporting.md)
