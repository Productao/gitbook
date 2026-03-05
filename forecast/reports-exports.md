---
description: Generating reports and exporting forecast data
icon: calendar-lines-pen
---

# Exporting Data from Forecast

Export Forecast data to share workforce projections with Finance, HR, leadership, and board.

## Export Formats

* **CSV** — All visible rows and columns in the current Forecast view. Best for Excel analysis, budget tools, and financial systems.
* **PowerPoint** — Org chart visual with position card content and highlights. Best for executive presentations. Note: PowerPoint export uses the org chart view, not the Forecast table — for Forecast table exports, use CSV and build charts in PowerPoint.
* **Image (PNG)** — Static snapshot of the current view. Best for embedding in documents or sharing via Slack or email.

## How to Export

1. Configure the Forecast view: row aggregator (Department, Location, Employee Type), time period (Monthly/Quarterly/Yearly), year, and metric (Headcount or Cost)
2. Apply any filters for targeted reports
3. Select Before/After/Changes mode — use **Show Changes** for scenario impact reports
4. Click **Export** (top-right) and select format

<figure><img src="../.gitbook/assets/Screenshot 2026-03-05 at 3.16.25 PM.png" alt=""><figcaption></figcaption></figure>

## Common Report Configurations

**Quarterly headcount report (HR/Recruiting)** — Aggregator = Department, Time Period = Quarterly, Metric = Headcount, View = Show After.

**Annual budget report (Finance/CFO)** — Aggregator = Department, Time Period = Yearly, Metric = Cost. Add Bonus/Stock if needed.

**Geographic cost distribution (COO/Finance)** — Aggregator = Location or Country, Yearly, Cost.

**Scenario impact report (approvers)** — Open scenario, Aggregator = Department, Time Period = Quarterly, View = Show Changes (+/- deltas). Export Cost and Headcount separately.

**5-year strategic plan (CEO/Board)** — Aggregator = Department, Yearly (shows all 5 years automatically), Cost.

**Hiring plan (Recruiting)** — Open scenario with new positions and hire dates, Monthly, Headcount, Show Changes. Filter positive changes in Excel for the new-hire timeline.

## Working with Exported CSV Data in Excel

* **Pivot tables** — Import CSV > Insert > Pivot Table > drag Departments to rows, time periods to columns, cost to values
* **Budget comparison** — Add a "Budget Target" column, create a "Variance" column (=Forecast - Budget), use conditional formatting for over/under
* **Multi-scenario comparison** — Export each scenario to separate CSVs, place side-by-side in Excel, create comparison charts

## Troubleshooting

| Problem                        | Solution                                                                                             |
| ------------------------------ | ---------------------------------------------------------------------------------------------------- |
| CSV export is empty            | Check if filters are hiding all data; verify the time period has data (future years need hire dates) |
| Too much data in export        | Apply department/location filters first; export one year at a time                                   |
| Excel can't open CSV           | Try Google Sheets first, then save as Excel; check for special characters                            |
| PowerPoint export looks blurry | Zoom to level 2–3 in org chart before exporting; reduce card content fields                          |

## Related Resources

* [Forecast Overview](overview.md)
* [Forecast Navigation](navigation.md)
* [Building Headcount Forecasts](building-headcount-forecasts.md)
