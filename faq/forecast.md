---
description: Forecast and budget planning questions
---

# 📈 Forecast FAQs

Common questions about using Forecast to view headcount projections, analyze workforce costs over time, and build budget plans. Learn how to navigate Forecast and integrate it with your scenarios.

***

## Understanding Forecast

### When should I use Forecast vs Scenarios?

**Answer:** Use Scenarios to make structural changes (add positions, close roles, move people, reorganize teams). Use Forecast to visualize headcount or cost over time after making those changes. They work together—create a scenario, then view it in Forecast to see the impact over time.

**Learn more:** [Forecast Overview](../forecast/overview.md)

### Is Forecast where I input headcount plans?

**Answer:** No. Forecast is purely a visualization mode—you're not inputting data here. To add positions with hire dates or model changes, use Scenarios. Forecast then displays those changes over time.

**Learn more:** [Forecast Overview](../forecast/overview.md)

### What's the difference between "Before", "After", and "Changes" views?

**Answer:** Before shows Main Org (current state), After shows your scenario's final state with all changes, and Changes shows the delta (additions and reductions). Use Changes view for impact reports showing what's different.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### Why does "Show Before" always reference Main Org?

**Answer:** Before view establishes your baseline by showing current state from Main Org, not the scenario's starting point. This ensures you're always comparing scenarios to the same consistent baseline.

**Learn more:** [Forecast Overview](../forecast/overview.md)

***

## Time Periods & Dates

### What's the difference between Monthly, Quarterly, and Yearly views?

**Answer:** Monthly divides annual salaries by 12 for precise month-by-month projections. Quarterly shows Q1-Q4 cost for a selected year. Yearly shows up to 5 years at once with full annual cost per year. Use monthly for detailed planning, quarterly for board reports, yearly for strategic planning.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### How do hire dates affect what I see in Forecast?

**Answer:** Positions with hire dates appear in Forecast starting from their hire date. For example, a position with hire date June 2026 appears starting Q2 2026. Without hire dates, positions only appear in current/past periods.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### What are effective dates and how do they work in Forecast?

**Answer:** Effective dates control when non-hire changes take effect (department transfers, salary changes, reorganizations). Assign an effective date to changes in a scenario, and they appear in Forecast starting from that date—allowing phased organizational changes over time.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### Do headcount numbers persist across years?

**Answer:** Yes. Headcount doesn't divide by 12—a position in 2026 stays in 2027 unless it has a termination date. Cost divides by time period (monthly cost = annual salary ÷ 12), but headcount persists.

**Learn more:** [Forecast Overview](../forecast/overview.md)

***

## Aggregation & Analysis

### What's a Group by and how do I use it?

**Answer:** Group by determines how data is grouped—one row per department, location, employee type, pay grade, etc. Choose Department for budget planning by team, Location for geographic analysis, or People for individual-level detail.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### How do I see cost by department over time?

**Answer:** Select Department as the Group by field, toggle to Cost view, select time period (Quarterly or Yearly), and optionally add monetary fields like Salary + Bonus. Export to CSV for presentations or budget tools.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### Can I view multiple pay components at once?

**Answer:** Yes! Click the monetary fields dropdown and select additional pay components (Salary, Bonus, Stock, Allowances). Each appears as separate columns, with a Total column automatically calculated.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### How do filters work in Forecast?

**Answer:** Filters apply globally across Directory, Org Chart, and Forecast. Apply filters once and they persist across all views. Use filters to narrow to specific departments, locations, or employee types before exporting or analyzing.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

***

## Building Forecasts

### How do I create a headcount forecast for future quarters?

**Answer:** Create a scenario, add positions with hire dates based on your hiring timeline (Q1 hires get January-March dates, Q2 get April-June, etc.), view the scenario in Forecast, select Quarterly time period, and toggle to Headcount view to see phased growth.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### How do I model attrition or planned departures?

**Answer:** In a scenario, close positions that will terminate using the Close button, assign termination dates, then view in Forecast with Show Changes selected. You'll see negative headcount changes in quarters when positions close and workforce cost decreases accordingly.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### Can I model both hiring and attrition in the same forecast?

**Answer:** Yes! Add growth positions with hire dates (net growth) and close positions with termination dates (expected turnover). Forecast → Show Changes view displays net impact by quarter, showing the combined effect of hires and departures.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### Why does Forecast show zero headcount in future months?

**Answer:** Positions need hire dates to appear in future periods. Check if your positions have hire dates configured. In scenarios, add hire dates to show phased hiring across quarters.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

***

## Exporting & Sharing

### How do I export forecast data?

**Answer:** Configure your forecast view (aggregator, time period, filters), click the Export button (right side of top bar), select Export to CSV.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### What's included when I export?

**Answer:** All visible rows and columns from your current view, respecting filters and aggregator selection, including headcount or cost (depending on toggle state), and all selected monetary fields. Use Show Changes view to create impact reports.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### Can I create multi-year forecasts?

**Answer:** Yes! Select Yearly as time period to see up to 5 years at once (2024, 2025, 2026, 2027, 2028). Add positions with hire dates spanning multiple years, then view in Forecast to see long-term workforce projections.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

***

## Troubleshooting

### My costs don't match my calculations. Why?

**Answer:** Verify you're viewing the correct time period (monthly divides by 12, quarterly shows quarter cost, yearly shows full annual). Check if all relevant monetary fields are selected, and ensure your data includes the compensation fields you expect.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### I added 10 positions but Forecast only shows 5. Why?

**Answer:** Check hire dates. Only positions with hire dates in the displayed time period appear. If you're viewing Q1 but hire dates are in Q2, they won't show in Q1. Verify positions have hire dates assigned.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### I can't see Before/After/Changes options. Why?

**Answer:** These options are only available when viewing a scenario in Forecast, not Main Org. In Main Org, you only see current state (equivalent to "Before"). Create or open a scenario to access these views.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### My hiring plan shows big spikes in certain quarters. How do I smooth it?

**Answer:** Spread hire dates more evenly throughout quarters. Instead of 20 hires on July 1, stagger them: 7 in July, 7 in August, 6 in September. This creates more realistic ramp and avoids lumpy projections.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

***

## Next Steps

* [**Forecast Overview**](../forecast/overview.md) - Complete introduction to Forecast
* [**Forecast Navigation**](../forecast/navigation.md) - Master the Forecast interface
* [**Building Headcount Forecasts**](../forecast/building-headcount-forecasts.md) - Create workforce projections
* [**Scenarios FAQs**](scenarios.md) - Scenario planning questions
* [**Data & Import FAQs**](data-import.md) - Data management questions
