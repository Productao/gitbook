---
description: Getting data out of Directory for analysis, presentations, and reports
---

# 📤 Exporting Data from Directory

Export organizational data from Directory, Org Chart, and Workforce Hub for analysis, presentations, and reports.

## Export Formats

**CSV** — Raw data from the current view; respects active filters and visible columns. Best for Excel/Sheets analysis, BI tools, and importing into other systems.

**PowerPoint** — Org chart structured as slides (one slide per manager). Best for executive presentations and leadership reviews.

**JPEG/PNG** — Screenshot of the current org chart view. Best for quick sharing, email, or embedding in documents.

## Exporting from Directory

1. Apply filters to narrow data
2. Customize visible columns (show/hide, reorder) — exports include only visible columns
3. Sort as desired
4. Click **Export** > **CSV**

**Admin export templates:** Admins can configure standardized export templates with preset columns and filters for one-click exports used across the team.

## Exporting from Org Chart

**JPEG:** Apply highlights and adjust zoom/layout, then Export > JPEG.

**PowerPoint:** Export > PowerPoint — configure scope (full org or filtered), hierarchy depth, layout, slide depth, and card content.

**CSV from org chart:** Apply filters, then Export > CSV — includes all visible positions with their attributes.

## Exporting from Workforce Hub

**PNG:** Configure chart > Download icon > PNG. High-resolution for presentations.

**PowerPoint:** Download icon > PowerPoint — editable chart object, not just an image.

**CSV (underlying data):** Click **Show Table** first > Download icon > CSV. Use for deeper analysis in Excel or BI tools.

## Common Export Workflows

**Department roster:** Directory > Filter by Department > show Name, Title, Manager, Email, Location > Export CSV.

**Org chart for executive presentation:** Main Org > Filter to top 3 layers > apply Department highlighting > Export PowerPoint.

**Compensation analysis:** Directory > show Department, Pay Grade, Salary, Title > sort > Export CSV.

**Open positions / vacancy report:** Directory > filter Employee Name = (empty) > show Job Title, Department, Manager, Pay Grade > Export CSV for recruiting.

**Span of control report:** Directory > filter Direct SOC = 1–2 > show Name, Title, Department, Direct SOC, Pay Grade > Export CSV.

## Best Practices

* Filter and customize columns **before** exporting — don't export everything and filter in Excel
* Include export date in filenames: `Engineering-Roster-2026-02-20.csv`
* Handle salary and personal data according to your organization's data security policies

## Troubleshooting

| Problem                               | Solution                                                 |
| ------------------------------------- | -------------------------------------------------------- |
| Columns missing                       | Check column settings; visible columns only are exported |
| Too much data                         | Apply filters before exporting                           |
| Org chart looks different than screen | Use "Fit to Screen" first; adjust layout before export   |
| PowerPoint has too many slides        | Filter to a smaller scope (one department or top layers) |
| Missing people                        | Check active filters; clear them and try again           |

## Related Articles

* [Directory Filtering & Sorting](filtering-sorting.md)
* [Main Org Exporting](../main-org/exporting.md)
* [Scenario Exporting](../scenarios/exporting.md)
