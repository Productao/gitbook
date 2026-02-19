---
description: Viewing forecast projections within scenarios
icon: chart-line
---

# Scenario Forecast

The Scenario Forecast view allows you to see time-phased projections of your scenario changes across months, quarters, and years. This powerful view helps you understand when changes take effect, track headcount and cost impacts over time, and model phased organizational changes.

## Overview

When you switch to Forecast view within a scenario, you're viewing a pivot-table-style projection that shows how your organizational changes unfold over time. This is particularly valuable when you've used effective dates, hire dates, or termination dates to model changes that happen at specific points in the future.

> **[Screenshot placeholder: Scenario with Forecast view selected from dropdown, showing quarterly headcount projection by department]**

**Key capabilities:**
- View headcount or cost projections over time (monthly, quarterly, or yearly)
- See when changes take effect based on effective dates
- Track phased hiring plans across multiple periods
- Understand departmental impacts across time horizons
- Model budget implications of reorganizations
- Compare before vs after states across time periods

## Accessing Scenario Forecast

To access the Forecast view within a scenario:

1. Open any scenario
2. Click the view dropdown at the top (default shows "Directory")
3. Select "Forecast"
4. The view switches to show time-based projections

> **[Screenshot placeholder: View dropdown menu showing Directory, Forecast, and Workforce Hub options with Forecast highlighted]**

The Forecast view is available in all scenarios and automatically incorporates any effective dates, hire dates, or termination dates you've configured.

## Forecast Configuration Options

### Row Aggregation

Choose what dimension to aggregate by in rows:

- **Department**: See each department as a row
- **Location**: View by office or geographic location
- **Country**: Aggregate by country
- **Employee Type**: View by full-time, part-time, contractor, etc.
- **Job Title**: Aggregate by role
- **Manager**: View by reporting relationship
- **Custom Fields**: Aggregate by any custom field in your org

> **[Screenshot placeholder: Row aggregation dropdown showing Department, Location, Country, Employee Type options]**

**Example use case:** Select "Department" to see how headcount in each department changes quarter-by-quarter as your reorganization takes effect.

### Metric Selection: Headcount vs Cost

Toggle between two primary metrics:

**Headcount**: Shows the count of positions in each row
- Use this to track hiring plans
- Monitor departmental growth or reduction
- Understand span of control changes over time

**Cost**: Shows monetary projections based on selected fields
- View salary expenses by period
- Track budget impact of organizational changes
- Model total compensation trends

> **[Screenshot placeholder: Headcount/Cost toggle button with Headcount selected]**

### Monetary Fields (Cost View)

When viewing Cost, select which compensation components to include:

- Base Salary
- Bonuses
- Allowances
- Stock Compensation
- Benefits
- Other custom monetary fields

You can select multiple fields to see total compensation impact.

> **[Screenshot placeholder: Monetary fields selector with Base Salary, Bonuses, and Allowances checked]**

### Time Aggregation

Choose your time granularity:

**Monthly**: See month-by-month changes
- Useful for detailed hiring plans
- Track specific start dates
- Monitor cash flow impact

**Quarterly**: View by fiscal or calendar quarter
- Most common view for workforce planning
- Aligns with business planning cycles
- Balances detail with readability

**Yearly**: Annual projections
- High-level multi-year planning
- Strategic headcount forecasting
- Long-term budget modeling

> **[Screenshot placeholder: Time aggregation selector showing Monthly, Quarterly, Yearly options with Quarterly selected]**

### Year Selection

When viewing Monthly or Quarterly aggregations, select which year to display (up to 5 years in the future).

> **[Screenshot placeholder: Year selector dropdown showing 2026, 2027, 2028, 2029, 2030]**

## Understanding Before, After, and Changes Views

Scenario Forecast works seamlessly with the Before/After/Changes toggle:

### Show Before

Displays forecast based on your **Main Org** (current reality, before scenario changes).

**When to use:**
- Establish your baseline projection
- See current state extended into the future
- Compare against proposed changes

> **[Screenshot placeholder: Forecast in "Show Before" mode showing current departmental headcount extended across quarters]**

### Show After

Displays forecast with **all scenario changes applied** (proposed future state).

**When to use:**
- See the full impact of your proposed changes
- View final state after all modifications
- Validate your scenario's end result

> **[Screenshot placeholder: Forecast in "Show After" mode showing modified departmental headcount across quarters]**

### Show Changes

Displays the **delta** between Before and After (increases/decreases).

**When to use:**
- Highlight exactly what's changing and when
- Show departmental gains (+) and losses (-)
- Communicate impact to stakeholders

> **[Screenshot placeholder: Forecast in "Show Changes" mode showing +5 and -5 changes by department in Q3 2026]**

**Example interpretation:**

| Department | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 |
|---|---|---|---|---|
| Network Operations | 0 | 0 | -5 | -5 |
| Operations & Logistics | 0 | 0 | +5 | +5 |

This Shows Changes view reveals that 5 positions move from Network Operations to Operations & Logistics starting in Q3 2026.

## How Effective Dates Work in Forecast

Effective dates create powerful time-based transitions in your forecast:

### The Core Concept

When you change a position's attributes and assign an effective date:
- The position keeps its **original state** until the effective date
- On the effective date, the position transitions to its **modified state**
- In Forecast, the position appears in its "before" location until the effective date, then moves to its "after" location

> **[Screenshot placeholder: Timeline diagram showing position in Department A through Q2, then in Department B from Q3 forward]**

### Example: Moving a Team with Effective Date

**Scenario:** You change 5 positions from "Network Operations" department to "Operations & Logistics" department with an effective date of July 1, 2026 (Q3).

**Forecast Result (Quarterly view, Show After mode):**

| Department | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 |
|---|---|---|---|---|
| Network Operations | 25 | 25 | 20 | 20 |
| Operations & Logistics | 30 | 30 | 35 | 35 |

The 5 positions appear in Network Operations through Q2, then in Operations & Logistics starting Q3.

### Forecast Without Effective Dates

If you make the same department change but **don't set an effective date**:
- The change is considered immediate
- The positions appear in Operations & Logistics for **all** time periods
- The forecast shows the final state throughout the entire projection

This is why effective dates are critical for modeling phased changes accurately.

## Practical Use Cases

### Multi-Year Hiring Plan

**Goal:** Model planned hiring across 2026-2028

**Approach:**
1. Create positions for planned roles
2. Set hire dates spread across the timeline
3. View Forecast in Monthly or Quarterly mode
4. Toggle to Cost view to see budget impact

**Result:** See exactly when headcount increases and corresponding cost impact by period.

> **[Screenshot placeholder: Forecast showing phased hiring plan with increasing headcount bars across 24 months]**

### Phased Reorganization

**Goal:** Model a reorganization happening in stages

**Approach:**
1. Move Team A to new department with Q2 2026 effective date
2. Move Team B with Q3 2026 effective date
3. Move Team C with Q4 2026 effective date
4. View Forecast in Quarterly mode, Show Changes

**Result:** See the gradual transition of teams across quarters, showing +/- impacts by period.

### Budget Impact Analysis

**Goal:** Understand cost impact of proposed changes

**Approach:**
1. Make organizational changes (promotions, new hires, transfers)
2. Switch to Forecast view in Cost mode
3. Select Base Salary + Bonuses + Allowances
4. View Quarterly or Yearly
5. Toggle Show Changes to see cost delta

**Result:** Clear visibility into when and where budget increases/decreases occur.

> **[Screenshot placeholder: Cost forecast showing departmental budget changes over 4 quarters with +/- dollar amounts]**

## Comparing Scenarios with Forecast

You can use Forecast view to compare different scenarios:

1. Open Scenario A, switch to Forecast view, note the projections
2. Open Scenario B, switch to Forecast view
3. Compare the different timing or magnitude of changes

This helps you evaluate different approaches to the same organizational goal.

## Tips for Effective Forecast Planning

**Use effective dates thoughtfully**
- Align effective dates to fiscal quarters or key business milestones
- Use effective dates for transfers and reorganizations
- Use hire dates for new positions being filled
- Use termination dates for position eliminations

**Choose appropriate time aggregation**
- Use Monthly for detailed hiring plans and cash flow
- Use Quarterly for most workforce planning scenarios
- Use Yearly for long-term strategic planning

**Leverage Show Changes view**
- This is often the most powerful view for communicating impact
- Clearly shows what's growing vs shrinking
- Makes it easy to see exactly when impacts occur

**Export forecast data**
- Use the export function to pull forecast projections into Excel
- Create custom charts and reports
- Share with budget owners and stakeholders

**Validate your projections**
- Always review forecasts in both Show Before and Show After modes
- Verify effective dates are correct
- Check that changes appear in the expected time periods

## Common Questions

**Why do my changes appear in all time periods even though I set an effective date?**

You might be viewing the org chart or directory view, which shows the "after" state. Switch to Forecast view to see time-phased transitions. In Forecast, the effective date controls when the position transitions between states.

**Can I have different effective dates for different positions in the same scenario?**

Yes. Each position can have its own effective date, allowing you to model complex phased changes across multiple time periods.

**How far into the future can I forecast?**

The Forecast module shows up to 5 years into the future from the current date.

**Do effective dates work for all field types?**

Yes. Effective dates work with any position attribute changes - department, location, manager, job title, salary, or custom fields.

**What's the difference between effective date and hire date in Forecast?**

- **Hire dates** represent when someone starts (position appears in headcount starting that period)
- **Effective dates** represent when a change to an existing position takes effect (position moves from one state to another)

For new positions being filled, use hire dates. For reorganizations and transfers, use effective dates.

---

## Related Articles

- [Time-Based Planning](time-based-planning.md) - Comprehensive guide to effective dates
- [Creating Scenarios](creating-scenarios.md)
- [Forecast Overview](../forecast/overview.md) - Forecast at the Main Org level
