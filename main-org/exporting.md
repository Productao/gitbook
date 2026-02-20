---
description: Exporting data and visuals from Main Org
icon: download
---

# Main Org Exporting

Export org data and visuals for reporting, analysis, presentations, and HRIS integration.

## Export Formats

**Visual exports:**
- **JPEG** — Screenshot of current org chart view (what you see is what you export)
- **PowerPoint** — Full org chart as structured slides with configurable depth, layout, and card content

**Data exports:**
- **CSV** — Raw position/employee data; respects active filters and column visibility
- **Excel** — Same as CSV with pre-formatted columns, bold headers, and correct cell types
- **EIB File** — Workday Enterprise Interface Builder format for direct HRIS import (admin only)
- **Template exports** — Admin-configured exports with preset columns and formatting

## How to Export

1. Navigate to Main Org (any view)
2. Apply filters if you want a subset of the data
3. Click **Export**
4. Select format and configure options
5. Click **Download**

## PowerPoint Configuration

When exporting as PowerPoint:
- **Filters:** Export only specific departments, locations, or business units
- **Hierarchy depth:** Full org, top 3 layers, top 5 layers, or custom
- **Layout:** Vertical (top-down), Horizontal (left-to-right), or Compact
- **Slide depth:** How many layers per slide (1–2 for clarity, 3–4 for balance, 5+ for density)
- **Card content:** Titles only, or full card content (department, level, compensation, etc.)

Each manager with direct reports gets their own slide.

## Directory View Exports

For precise column control:
1. Switch to **Directory** view
2. Apply filters and customize visible columns (show/hide, reorder)
3. Click Export — the file includes only visible columns in displayed order

## Forecast View Exports

In Forecast view, export the headcount/cost projection table:
1. Configure time period (monthly/quarterly/yearly), aggregation, and metric
2. Click Export to download the table with rows per department/location and columns per time period

**Learn more:** [Forecast Reports & Exports](../forecast/reports-exports.md)

## Workforce Hub Exports

From Workforce Hub, export charts as PNG images (for presentations) or the underlying data as CSV/Excel (for further analysis or BI tools).

## Permissions

Exports respect your access scope — you can only export data you can see. Sensitive attributes hidden by your access group are excluded from exports. EIB exports are typically restricted to admins and HRIS teams.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Export button grayed out | Check export permissions with admin |
| File is empty | Filters may be too restrictive; try removing them |
| Takes a long time | Filter to a smaller subset or export by department |
| Columns missing | Check column visibility in Directory view; some may be permission-restricted |

**More help:** [Export & Integration Issues](../troubleshooting/export-integration-issues.md)

## Related Articles

- [Directory Exporting & Reporting](../directory/exporting-reporting.md)
- [Forecast Reports & Exports](../forecast/reports-exports.md)
- [Scenario Exporting](../scenarios/exporting.md)
