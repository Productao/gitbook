---
description: Introduction to Forecast and headcount planning
icon: chart-mixed
---

# Forecast Overview

Forecast is Agentnoon's pivot table-style visualization tool for analyzing headcount and workforce costs over time. It provides flexible ways to view and aggregate data from your Main Org or Scenarios — by department, location, time period, and more.

**Key principle** — Forecast shows you what's already in your data. To model changes (adding positions, closing roles, moving people), use Scenarios. To see those changes projected over time, use Forecast.

## Forecast vs. Scenarios

Forecast and Scenario work together — Create a scenario with your planned changes, then view that scenario in Forecast to see the financial and headcount impact over time.

| I need to…                                           | Use                        |
| ---------------------------------------------------- | -------------------------- |
| Make structural changes (reorgs, RIFs, hiring)       | Scenario                   |
| Add or close positions                               | Scenario                   |
| Move people between teams                            | Scenario                   |
| Create "what-if" alternatives                        | Scenario                   |
| Submit changes for approval                          | Scenario                   |
| Compare multiple budget cut options                  | Scenarios + Forecast       |
| Visualize headcount or cost over time                | Forecast                   |
| Aggregate data by department, location, or dimension | Forecast                   |
| Analyze monthly, quarterly, or annual trends         | Forecast                   |
| Report headcount by quarter to the board             | Forecast                   |
| Export workforce cost for Finance                    | Forecast                   |
| See cost impact of a restructure over time           | Forecast (of the scenario) |
| See monthly hire ramp from new positions             | Forecast (of the scenario) |

## Accessing Forecast

From Main Org or any scenario: click the module dropdown at the top > select **Forecast**.

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

## How Forecast Works

Forecast functions like a pivot table with three key components:

**Row Aggregator** — Defines each row. Choose how to group your data:

* People — one row per person
* Department — one row per department
* Location — one row per location/country
* Employee Type — one row per employee type
* Any custom field — group by pay grade, business unit, etc.

**Columns** — What appears across the top:

* Time periods: Monthly, Quarterly, or Yearly
* Monetary fields: Salary, bonuses, allowances, or other compensation components
* Multiple pay components can be shown simultaneously (e.g., salary + bonus)

**Values** — What's measured. Toggle between:

* Headcount — number of positions/employees
* Cost — workforce cost (salary and configured compensation)

## Understanding Forecast Data

**Headcount view:**

* Current headcount reflects positions that exist today
* Future headcount appears based on hire dates in your data
* If a position has a hire date in Q3, that headcount appears starting in Q3
* Headcount doesn't divide by 12 — a position in 2026 persists into 2027 unless it has a termination date

**Example:** You have 100 employees today and 10 positions with hire dates in Q2 2026. Forecast will show:

* Q1 2026: 100 headcount
* Q2 2026: 110 headcount (10 new hires added)
* Q3 2026: 110 headcount (no terminations, headcount persists)

**Cost view:**

* Annual salaries are what's stored in Agentnoon
* Monthly view divides annual salary by 12
* Quarterly view shows salary for that quarter
* Yearly view shows full annual cost
* Cost increases when positions with hire dates become active

**Note:** Agentnoon supports annualizable compensation. One-time payments (signing bonuses, spot bonuses) are not currently supported in Forecast.

## Key Forecast Capabilities

**Flexible aggregation** — View your workforce from any angle:

* Aggregate by department to see total departmental costs
* Aggregate by location to understand geographic distribution
* Aggregate by employee type to distinguish contractors vs. full-time

**Time-based analysis:**

* **Monthly** — Precise month-by-month projections; annual cost divided by 12
* **Quarterly** — Standard for budget planning and board reporting
* **Yearly** — Best for annual budget planning; shows full annual cost per year; up to 5 years

<figure><img src="../.gitbook/assets/Screenshot 2026-03-05 at 3.08.11 PM.png" alt=""><figcaption></figcaption></figure>

**Before / After / Changes (scenarios only):**

* **Show Before** — Main Org baseline (current state)
* **Show After** — Scenario final state
* **Show Changes** — Delta between before and after

<figure><img src="../.gitbook/assets/Screenshot 2026-03-05 at 3.09.32 PM.png" alt=""><figcaption></figcaption></figure>

**Example:** You move 5 people from Network Ops to Operations & Logistics:

* After view — shows all 5 people in Operations & Logistics
* Changes view — shows -5 in Network Ops, +5 in Operations & Logistics

**Note:** "Show Before" always references your Main Org, not the starting state of a scenario or any other scenario.

**Filtering and search** — Apply filters and search for specific positions or employees. Filters apply globally across Directory, Forecast, and Workforce Hub.

**Export** — Download forecast data to CSV for further analysis in Excel or presentations.

## Forecast Limitations

| Forecast is NOT for                                  | Use this instead |
| ---------------------------------------------------- | ---------------- |
| Data input — you can't add positions or make changes | Scenarios        |
| Budget targets or goals                              | Coming soon      |
| Approval workflows                                   | Scenarios        |
| Tracking actuals vs. budget variance over time       | Your FP\&A tool  |

## Common Use Cases

**Quarterly headcount planning** — Aggregate by Department > view Quarterly > Headcount > see headcount growth projections based on hire dates.

**Annual budget planning** — Aggregate by Department or Cost Center > view Yearly > switch to Cost > see total annual workforce cost by department.

**Multi-year strategic planning** — Create a scenario with phased hiring (hire dates in 2026, 2027, 2028) > view Yearly in Forecast > see headcount and cost ramp over 3 years > aggregate by Department to see where growth is concentrated.

**RIF or budget cut impact** — Create a scenario closing positions with effective dates > view Monthly or Quarterly > see exactly when cost reductions take effect > aggregate by Department to show department-specific impact.

## Forecast and Effective Dates

Beyond hire and termination dates, you can use effective dates to model changes over time.

1. In a scenario, make a change (move someone to a new department, change their salary)
2. Assign an effective date to that change (e.g., January 2027)
3. In Forecast, that change appears starting in the effective date period

**Example:** 5 people currently in Network Operations are planned to move to Operations & Logistics in 2027. Change their department field and set effective date to January 2027. In Forecast, they appear in Network Ops through 2026, then shift to Operations & Logistics from January 2027.

**Alternative approach for headcount tracking:**

* Close 5 positions in Network Ops (with effective date)
* Add 5 positions in Operations & Logistics (with hire date)
* This shows a clear -5 / +5 split in Changes view

## Getting Started with Forecast

**Step 1: Understand your current state**

* Go to Main Org > **Forecast**
* Aggregate by Department > view Yearly
* This shows your current workforce cost by department

**Step 2: Model future changes in a scenario**

* Create a new scenario
* Add positions with hire dates for future quarters
* Close positions with termination dates if modeling attrition
* Assign effective dates to changes you want phased over time

**Step 3: View your scenario in Forecast**

* Open your scenario > switch to **Forecast**
* Toggle between Before, After, and Changes
* Adjust time granularity (Monthly, Quarterly, Yearly)
* Aggregate by the dimension that matters (Department, Location, etc.)

**Step 4: Export and share**

* Export to CSV
* Share projections with Finance, HR leadership, or executives
* Use exported data in presentations or budget planning tools

## Next Steps

* [**Forecast Navigation**](navigation.md) - Master the Forecast interface and controls
* [**Building Headcount Forecasts**](building-headcount-forecasts.md) - Create your first forecast
* [**Budget Planning & Tracking**](/broken/pages/i8Gakir7OiTeqKZMK86R) - Align forecasts with budgets
* [**Forecast vs Scenarios**](/broken/pages/MKRiiU8DK4L0RAbqG70N) - Detailed comparison of the two modules
* [**Multi-Year Planning**](multi-year-planning.md) - Long-term workforce projections
