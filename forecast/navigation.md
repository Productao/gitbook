---
description: Navigating the Forecast interface and tools
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/FQHYLeH687WAkUobefnf/forecast/forecast-navigation
---

# 🧭 Orientation & Navigation

> **\[Screenshot placeholder: Forecast view showing the full interface layout with toolbar, table, and time periods]**

## Accessing Forecast

From Main Org or any scenario: click the module dropdown at the top > select **Forecast**. Configuration (aggregator, time period, etc.) is retained when you switch between contexts.

## Interface Layout

**Top bar (left to right):**

* **Row Aggregator dropdown** — How to group data (Department, Location, Employee Type, Pay Grade, custom fields, or People for individual rows)
* **Headcount/Cost toggle** — Switch metric
* **Monetary Fields** — Add Bonus, Stock, Allowances alongside Salary
* **Filter button** — Narrow to a subset
* **Search button** — Find specific positions or employees
* **Time Period dropdown** — Monthly, Quarterly, or Yearly
* **Year selector** — Which year to display (Monthly/Quarterly only)
* **Export button** — CSV download

**Forecast table** — Rows = aggregator groups, Columns = time periods, Values = headcount or cost.

## Key Controls

**Row Aggregator** — Department for budget planning, Location for geographic analysis, Pay Grade for compensation analysis, People for individual review, any custom field for business unit or cost center views.

**Headcount vs. Cost** — Headcount = count of positions per period (a 2026 hire persists into 2027 unless terminated). Cost = salary ÷ 12 per month, ÷ 4 per quarter, full year for yearly view.

**Time periods:**

* **Monthly** — Precise timing for when hires start or changes take effect; annual salary divided by 12
* **Quarterly** — Standard for budget planning and board reporting
* **Yearly** — Shows up to 5 years; annual cost per year; best for multi-year strategic planning

**Before / After / Changes (scenarios only):**

* **Show Before** — Main Org baseline
* **Show After** — Scenario final state
* **Show Changes** — Delta between before and after (+/- per row)

## Common Navigation Workflows

**Quarterly budget review** — Aggregator = Department > Quarterly > Cost > Salary + Bonus > Export CSV.

**Hiring plan tracking** — Aggregator = Department > Monthly > Headcount > Show Changes (in scenario) > see which months headcount grows.

**Multi-year planning** — Aggregator = Department > Yearly (see all 5 years) > Cost > Export for executive presentation.

**Geographic cost analysis** — Aggregator = Location or Country > Yearly > Cost.

## Troubleshooting

<table><thead><tr><th width="324.609375">Problem</th><th>Solution</th></tr></thead><tbody><tr><td>Future months show zero headcount</td><td>Positions need hire dates to appear in future periods</td></tr><tr><td>Costs don't match expectations</td><td>Check monthly ÷ 12; verify all monetary fields are selected</td></tr><tr><td>Filters not working</td><td>Check if existing filters are active; clear all and start fresh</td></tr><tr><td>Before/After/Changes options missing</td><td>Only available in scenarios, not Main Org</td></tr><tr><td>Export missing data</td><td>Check active filters; verify correct time period is selected</td></tr></tbody></table>

## Related Resources

* [Forecast Overview](overview.md)
* [Building Headcount Forecasts](building-headcount-forecasts.md)
* [Forecast vs Scenarios](/broken/pages/MKRiiU8DK4L0RAbqG70N)
* [Forecast Reports & Exports](reports-exports.md)
