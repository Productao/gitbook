---
description: Exporting data from Directory to CSV
hidden: false
---

# Exporting from Directory

Export Directory data to CSV for offline analysis, reporting, and integration with Excel, Google Sheets, or BI tools.

## How to Export

1. Configure Directory view: apply filters, set visible columns, sort
2. Click **Export** > select CSV or Excel
3. File downloads with all visible rows and columns (hidden columns and filtered-out rows are excluded)

## Common Export Workflows

**Department roster:** Filter by Department > show Name, Title, Email, Manager, Location > sort by Name > Export CSV.

**Compensation analysis:** Show Name, Title, Department, Pay Grade, Salary > sort by Salary (high→low) > Export CSV > analyze in Excel.

**Vacancy list for recruiting:** Filter Employee Name = (empty) > show Position Title, Department, Manager, Pay Grade > Export CSV.

**Scenario change log:** Open scenario in Directory > show Name, Title, Change Type, Old Value, New Value, Department > sort by Change Type > Export CSV for approval package.

**Span of control review:** Filter Layer = 3–5 > show Name, Title, Department, Layer, Direct SOC, Total Org Size > sort by Direct SOC (high→low) > Export CSV.

## Export Templates

Some instances support admin-configured templates with preset column sets for recurring reports (e.g., "Compensation Report", "Headcount Roster"). Click Export > Template > select from list.

## Working with Exported Files

**Excel:** File > Open > select CSV. Format salary as currency (right-click > Format Cells); use pivot tables for summary views.

**Google Sheets:** File > Import > Upload > select CSV > Import data.

## Exporting from Different Modes

**Main Org Directory:** Current org data, department rosters, compensation summaries.

**Scenario Directory:** Scenario state with change indicators (Change Type, Old/New Value columns), impact analysis reports for approvers.

**Forecast Directory:** Time-based projections (quarterly/yearly headcount, budget projections).

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Export has too many columns | Hide unnecessary columns before exporting |
| Missing expected positions | Check active filters; clear filters and re-export |
| File won't open in Excel | Use Excel File > Open > CSV import, not double-click |
| Salary imports as text in Excel | Select column > Data > Text to Columns > Finish |
| Changes not reflected in export | Save the scenario, refresh Directory, then export |

## Related Articles

- [Column Customization](columns-customization.md)
- [Filtering & Sorting](filtering-sorting.md)
- [Exporting & Reporting](exporting-reporting.md)
