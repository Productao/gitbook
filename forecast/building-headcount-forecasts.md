---
description: Creating and managing headcount forecasts
---

# 📊 Building Headcount Forecasts

Let me pull the full section first.---

## Building Headcount Forecasts

Building a headcount forecast means creating a Scenario with planned changes, then viewing that Scenario in Forecast mode to see projections over time.

**Key principle** — Forecasts are views of your data, not separate documents. You build forecasts by creating Scenarios with planned changes, using hire and effective dates to phase changes over time, then viewing those Scenarios in Forecast mode.

**What you need:**

* A Scenario (or use Main Org for a current state forecast)
* Positions with hire dates for future headcount
* Termination dates if modeling attrition
* Effective dates for phased organizational changes

### Method 1: Forecast Current State

**Use for:** Reporting current workforce size and cost — no scenario needed.

1. Go to Main Org > **Forecast**
2. Aggregator: choose Department, Location, or desired dimension
3. Toggle: Headcount
4. Time period: Yearly, Quarterly, or Monthly
5. Export or analyze

**What you'll see:** Current headcount distributed across your chosen aggregation, projected forward. Headcount persists unless termination dates exist.

### Method 2: Forecast with Hire Dates (Phased Hiring Plan)

**Use for:** Planning staggered hiring across quarters.

**Step 1: Create a scenario**

1. Click **Create Scenario**
2. Name it descriptively (e.g., "2026 Engineering Hiring Plan")
3. Select scenario type (usually Full Org)
4. Click **Create**

**Step 2: Add positions with hire dates**

1. Navigate to the department where you'll add positions
2. Click **+ Add Position** or use bulk add
3. Fill in position details: Title, Department, Manager, Salary
4. Set the Hire Date — this is required for the position to appear in Forecast

Set hire dates based on your hiring timeline:

* Q1 hires: January, February, or March
* Q2 hires: April, May, or June
* Q3 hires: July, August, or September
* Q4 hires: October, November, or December

**Example:**

* 3 Software Engineers — hire date: March 15, 2026
* 2 Product Managers — hire date: June 1, 2026
* 5 Sales Reps — hire date: September 1, 2026

**Step 3: View in Forecast**

1. Stay in your scenario > click **Forecast**
2. Aggregator: Department
3. Toggle: Headcount
4. Time period: Quarterly, Year: 2026
5. View: Show After

**What you'll see:**

* Q1 2026: Current headcount + 3 (March hires)
* Q2 2026: Previous + 2 (June hires)
* Q3 2026: Previous + 5 (September hires)
* Q4 2026: Same as Q3 (no new hires)

**Step 4: Analyze cost impact**

1. Toggle to Cost
2. Monetary fields: select Salary (or add Bonus, etc.)

**What you'll see:** Total salary cost increases as new hires join.

### Method 3: Forecast with Effective Dates (Organizational Changes Over Time)

**Use for:** Modeling a reorganization or departmental transfer happening in the future.

**Step 1: Make organizational changes**

1. In a scenario, select positions to move (e.g., 5 people from Network Ops to Operations & Logistics)
2. Change their department field to the new department
3. Assign an effective date to all changes (e.g., January 1, 2027)

**Step 2: View in Forecast**

1. Click **Forecast** > Aggregator: Department
2. Toggle: Headcount or Cost
3. Time period: Quarterly or Yearly; select years spanning the effective date

**What you'll see:**

* Through Q4 2026: People remain in Network Ops
* Starting Q1 2027: People appear in Operations & Logistics
* Show Changes view: -5 Network Ops, +5 Operations & Logistics starting Q1 2027

### Method 4: Model Attrition with Termination Dates

**Use for:** Planning for expected attrition or retirements.

**Step 1: Identify positions closing**

1. In a scenario, find positions closing due to retirement, planned departures, or budget cuts
2. Close those positions and assign termination dates

**Step 2: View in Forecast**

1. Forecast > Aggregator: Department
2. Toggle: Headcount > Time period: Quarterly
3. View: Show Changes

**What you'll see:**

* Negative headcount changes (-1, -2, etc.) in quarters when positions close
* Workforce cost decreases accordingly

### Method 5: Combined Hiring and Attrition Forecast

**Use for:** Modeling realistic workforce dynamics with both hiring and departures.

1. Add new positions with future hire dates (net growth)
2. Close positions with termination dates (model turnover or planned departures)
3. Forecast > Show Changes > Aggregator: Department > Quarterly

**Example:**

* Q1: +10 hires, -3 departures = +7 net headcount
* Q2: +5 hires, -2 departures = +3 net headcount
* Q3: +8 hires, -4 departures = +4 net headcount
* Q4: +2 hires, -1 departure = +1 net headcount
* Annual net growth: +15 headcount

### Multi-Department Hiring Plan

**Use for:** Coordinating hiring across multiple departments.

**Step 1: Add positions by department**

* Engineering: 15 positions across Q1–Q4
* Sales: 10 positions in Q2–Q3
* Marketing: 5 positions in Q1
* Product: 8 positions across all quarters

**Step 2: Stagger hire dates** — Spread hires throughout the quarter. Don't cluster everyone on quarter start dates; factor in ramp-up time.

**Step 3: Analyze aggregated impact**

1. Forecast > Show After > Aggregator: Department
2. Toggle: Headcount > Time period: Quarterly
3. Review hiring ramp by department

**Step 4: Check budget impact**

1. Toggle to Cost
2. Verify total salary increase by quarter aligns with budget approvals

## Best Practices

* **Use realistic hire dates** — Don't cluster all hires on Jan 1, Apr 1, Jul 1, Oct 1. Spread hires throughout quarters and factor in recruiting timelines.
* **Plan for ramp time** — Stagger starts to avoid overwhelming managers; budget for overlapping periods when backfilling departing employees.
* **Model attrition realistically** — Use historical attrition rates, known retirements, and seasonal fluctuations.
* **Coordinate with budget cycles** — Align hire dates with budget availability and quarterly releases.
* **Use effective dates for non-hire changes** — Promotions, department transfers, and salary adjustments planned for future dates.
* **Keep scenarios organized** — Name clearly (e.g., "2026 Q2–Q4 Hiring Plan"), add descriptions explaining assumptions, and tag by purpose.

## Exporting and Sharing Your Forecast

1. Configure the view: set aggregator, time period, headcount/cost toggle, and any filters
2. Click **Export** > **CSV**
3. Share with stakeholders:
   * **Finance** — Department aggregation, Cost view, Quarterly
   * **HR** — Department aggregation, Headcount view, Monthly
   * **Executives** — High-level aggregation, Yearly, both Headcount and Cost
4. Use **Show Changes** view to highlight net impact and tie to strategic priorities

## Troubleshooting

| Issue                                                       | Solution                                                                                                                                        |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Added 10 positions but Forecast only shows +5               | Check hire dates — positions only appear in the period their hire date falls in                                                                 |
| Forecast shows headcount growth but budget didn't increase  | Adding positions without closing others increases net headcount and cost — close equivalent positions or adjust salaries to stay budget-neutral |
| Can't see quarterly progression, only annual totals         | Change Time Period from "Yearly" to "Quarterly", then select the year                                                                           |
| Hiring plan looks lumpy with big spikes in certain quarters | Spread hire dates more evenly — instead of 20 hires on July 1, stagger: 7 in July, 7 in August, 6 in September                                  |
| Need to forecast for 2+ years but only see one year         | Switch Time Period to "Yearly" to see columns for all 5 years                                                                                   |

## Next Steps

* [**Budget Planning & Tracking**](/broken/pages/i8Gakir7OiTeqKZMK86R) - Align forecasts with budget constraints
* [**Forecast Reports & Exports**](reports-exports.md) - Advanced reporting techniques
* [**Multi-Year Planning**](multi-year-planning.md) - Long-term strategic workforce planning
* [**Time-Based Planning**](../scenarios/time-based-planning.md) - More on effective dates and phasing
