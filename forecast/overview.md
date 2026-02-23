---
description: Introduction to Forecast and headcount planning
---

# 📈 Forecast Overview

Forecast is Agentnoon's pivot table-style visualization tool for analyzing headcount and workforce costs over time. Think of it as a powerful reporting and analysis module that helps you view your organizational data from different angles—by department, location, time period, and more.

## What is Forecast?

**Forecast is purely a visualization mode**—you're not inputting information here. Instead, Forecast provides flexible ways to view and aggregate the data from your Main Org or Scenarios.

**Key principle:** Forecast shows you what's already in your data. To model changes (adding positions, closing roles, moving people), you'll use Scenarios. To see those changes projected over time, you'll use Forecast.

***

## Forecast vs Scenarios: When to Use Each

### Use **Scenarios** when you need to:

* Make structural changes to your organization
* Add or close positions
* Move people between teams
* Model reorganizations, RIFs, or hiring plans
* Create "what-if" alternatives

\###Use **Forecast** when you need to:

* Visualize headcount or cost over time
* Aggregate data by department, location, or other dimensions
* Analyze monthly, quarterly, or annual trends
* Report on workforce projections
* Export aggregated data for leadership presentations

**They work together:** Create a scenario with your planned changes, then view that scenario in Forecast to see the financial and headcount impact over time.

***

## How Forecast Works: The Pivot Table Concept

Forecast functions like a pivot table with three key components:

### 1. **Row Aggregator** (What defines each row)

Choose how to group your data:

* **People** - One row per person
* **Department** - One row per department
* **Location** - One row per location/country
* **Employee Type** - One row per employee type
* **Any custom field** - Group by pay grade, business unit, etc.

### 2. **Columns** (What appears across the top)

* **Time periods:** Monthly, Quarterly, or Yearly
* **Monetary fields:** Salary, bonuses, allowances, or other compensation components
* You can see multiple pay components at once (e.g., salary + bonus columns)

### 3. **Values** (What's measured)

Toggle between:

* **Headcount** - Number of positions/employees
* **Cost** - Workforce cost (salary and configured compensation)

***

## Accessing Forecast

1. Click the **"Open Org"** button to enter your organizational view
2. Click the **Forecast** dropdown at the top of the screen (next to Directory, Workforce Hub, Productivity)
3. You're now in Forecast mode

> **\[Screenshot placeholder: Forecast dropdown menu location in top navigation bar]**

***

## Understanding Forecast Data

### Headcount View

When viewing headcount:

* **Current headcount** reflects positions that exist today
* **Future headcount** appears based on **hire dates** in your data
* If a position has a hire date in Q3, that headcount appears starting in Q3
* Headcount doesn't divide by 12—a position in 2026 stays in 2027 unless it has a termination date

**Example:** You have 100 employees today. Your data includes 10 positions with hire dates in Q2 2026. Forecast will show:

* Q1 2026: 100 headcount
* Q2 2026: 110 headcount (10 new hires added)
* Q3 2026: 110 headcount (no terminations, headcount persists)

### Cost View

When viewing cost:

* **Annual salaries** are what's stored in Agentnoon
* **Monthly view** divides annual salary by 12
* **Quarterly view** shows salary for that quarter
* **Yearly view** shows full annual cost
* Cost increases when positions with hire dates become active

**Important:** Agentnoon supports annualizable compensation. One-time payments (signing bonuses, spot bonuses) are not currently supported in Forecast.

***

## Key Forecast Capabilities

### Flexible Aggregation

View your workforce from any angle:

* Aggregate by department to see total departmental costs
* Aggregate by location to understand geographic distribution
* Aggregate by employee type to distinguish contractors vs. full-time

### Time-Based Analysis

* **Monthly:** See precise month-by-month projections (divides annual cost by 12)
* **Quarterly:** Useful for quarterly planning and reporting
* **Yearly:** Best for annual budget planning, shows full annual cost per year
* **Multi-year view:** See up to 5 years in the future

### Before, After, and Changes Views

When viewing a Scenario in Forecast:

* **Show Before:** References Main Org (current state)
* **Show After:** Shows the final state of your scenario
* **Show Changes:** Shows the delta between before and after

**Example:** You move 5 people from Network Ops to Operations & Logistics:

* **After view:** Shows all 5 people in Operations & Logistics
* **Changes view:** Shows -5 in Network Ops, +5 in Operations & Logistics

**Critical note:** "Show Before" always references your Main Org, not the starting state of a scenario or any other scenario.

### Filtering and Search

* Apply filters (same filters work across all modules)
* Search for specific positions or employees
* Filters apply globally across Directory, Forecast, Workforce Hub

### Export Capabilities

Export your forecast data to CSV for further analysis in Excel or presentations.

***

## Common Use Cases

### Quarterly Headcount Planning

**Scenario:** Plan Q2-Q4 hiring by department

* Aggregate by Department
* View quarterly
* See headcount growth projections based on hire dates

### Annual Budget Planning

**Scenario:** Create next year's workforce budget

* Aggregate by Department or Cost Center
* View yearly
* Switch to Cost view
* See total annual workforce cost by department

### Multi-Year Strategic Planning

**Scenario:** Model 3-year growth plan

* Create a scenario with phased hiring (hire dates in 2026, 2027, 2028)
* View in Forecast yearly
* See headcount and cost ramp over 3 years
* Aggregate by Department to see where growth is concentrated

### RIF or Budget Cut Impact

**Scenario:** Understand the timeline of cost savings

* Create a scenario closing positions with effective dates
* View in Forecast monthly or quarterly
* See exactly when cost reductions take effect
* Aggregate by Department to show department-specific impact

***

## Forecast and Effective Dates

Beyond hire and termination dates, you can use **effective dates** to model changes over time:

**How it works:**

1. In a scenario, make a change (move someone to a new department, change their salary)
2. Assign an **effective date** to that change (e.g., January 2027)
3. In Forecast, that change appears starting in the effective date period

**Example use case:**

* 5 people currently in Network Operations
* You plan to move them to Operations & Logistics in 2027
* Change their department field and mark all changes with effective date: January 2027
* In Forecast, they appear in Network Ops through 2026, then shift to Operations & Logistics starting January 2027

**Alternative approach for headcount tracking:**

* Close 5 positions in Network Ops (with effective date)
* Add 5 positions in Operations & Logistics (with hire date)
* This shows a clear -5 / +5 split in Changes view

***

## Forecast Limitations

### What Forecast Is NOT:

* **Not for data input:** You can't add positions or make changes in Forecast
* **Not for targets:** Forecast doesn't support budget targets or goals (coming soon)
* **Not for approvals:** Only scenarios have approval workflows, not forecasts themselves
* **Not real-time FPNA:** Forecast doesn't track actuals vs. budget variance over time

### What You'll Do in Scenarios Instead:

* All organizational changes (hiring, terminations, moves, new positions)
* Setting effective dates and hire dates
* Creating alternative "what-if" plans
* Submitting changes for approval

***

## Getting Started with Your First Forecast

**Step 1:** Understand your current state

* Go to Main Org → Forecast
* Aggregate by Department
* View yearly
* This shows your current workforce cost by department

**Step 2:** Model future changes in a Scenario

* Create a new scenario
* Add positions with hire dates for future quarters
* Close positions with termination dates if modeling attrition
* Assign effective dates to changes you want phased over time

**Step 3:** View your scenario in Forecast

* Open your scenario
* Switch to Forecast view
* Toggle between Before, After, and Changes
* Adjust time granularity (monthly, quarterly, yearly)
* Aggregate by the dimension that matters (Department, Location, etc.)

**Step 4:** Export and share

* Export to CSV
* Share projections with Finance, HR leadership, or executives
* Use exported data in presentations or budget planning tools

***

## Next Steps

* [**Forecast Navigation**](navigation.md) - Master the Forecast interface and controls
* [**Building Headcount Forecasts**](building-headcount-forecasts.md) - Create your first forecast
* [**Budget Planning & Tracking**](/broken/pages/i8Gakir7OiTeqKZMK86R) - Align forecasts with budgets
* [**Forecast vs Scenarios**](forecast-vs-scenarios.md) - Detailed comparison of the two modules
* [**Multi-Year Planning**](multi-year-planning.md) - Long-term workforce projections
