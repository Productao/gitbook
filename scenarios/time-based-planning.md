---
description: Using effective dates for phased changes
hidden: false
---

# Time-Based Planning

Time-based planning in Agent Noon allows you to model organizational changes that occur at different points in time, enabling you to see how your workforce structure and costs evolve across months, quarters, and years. By using effective dates, hire dates, and termination dates, you can create sophisticated forecasts that reflect the true timing of organizational changes.

## Understanding Time-Based Fields

Agent Noon uses three different types of date fields to control when changes take effect in your forecasts. Understanding the difference between these fields is critical to modeling your workforce plans accurately.

### Hire Dates

**Hire dates** indicate when a person starts in a position. This field is typically used to represent when a new employee joins your organization or when a vacant approved position will be filled.

Use hire dates when:
- Modeling the hiring of new employees into existing or new positions
- Planning future hiring to fill approved vacancies
- Showing when headcount will increase

In the Forecast module, positions with future hire dates will appear in your headcount and cost projections starting from the month of the hire date forward.

### Termination Dates

**Termination dates** indicate when a person leaves a position. This field represents when an employee departs your organization and their position becomes vacant (or is eliminated).

Use termination dates when:
- Modeling employee departures or layoffs
- Planning position eliminations
- Showing when headcount will decrease

In the Forecast module, positions with termination dates will no longer appear in headcount counts after the termination month, and their associated costs will be removed from cost projections.

### Effective Dates

**Effective dates** indicate when a change to an existing position takes effect, without involving hiring or termination. This is a powerful feature that allows you to model organizational changes that happen at a future point in time.

Use effective dates when:
- Moving employees or positions between departments, teams, or locations
- Changing reporting relationships at a future date
- Reorganizing teams with a planned implementation date
- Modeling phased organizational changes
- Planning internal transfers or promotions that occur in the future

Effective dates are the key to modeling complex reorganizations where people stay employed but their organizational attributes change at specific points in time.

## How Effective Dates Work

Effective dates create a "before" and "after" state for positions, with the change occurring at the specified date.

### The Core Concept

When you modify a position that exists in your main organizational chart and assign an effective date to those changes:

- The position keeps its original ("before") state until the effective date
- On the effective date, the position transitions to the modified ("after") state
- In Forecast views, the position appears in its "before" location until the effective date, then appears in its "after" location from the effective date forward

{% hint style="info" %}
**Screenshot Placeholder:** Timeline visualization showing a position in "Department A" before an effective date of Q3 2026, then moving to "Department B" starting Q3 2026 and forward
{% endhint %}

### Important: Before and After States in Scenarios

Understanding "before" and "after" states is crucial when working with scenarios:

**For Existing Positions:**
- **Before state**: The position's attributes as they exist in the main organizational chart
- **After state**: The position's attributes after you've made changes in the scenario

**For New Positions:**
- **Before state**: Empty (the position didn't exist)
- **After state**: The new position's attributes as created in the scenario

This distinction is important because it affects how changes appear in forecasts and reports.

{% hint style="warning" %}
**Important:** The "before" state in a scenario always references the main organizational chart, not the start of the scenario, and not any other scenario. When you view "Show Before" in a scenario, you're seeing the current state from your main org data.
{% endhint %}

## Using Effective Dates for Organizational Changes

Let's walk through practical examples of how to use effective dates for time-based planning.

### Example 1: Moving a Team Between Departments

**Scenario:** You want to move a 5-person Network Operations team to the Operations and Logistics department, but the move won't happen until Q1 2027.

**Using Effective Dates:**

1. Create or open a scenario
2. Find the 5 positions in the Network Operations team
3. Select all 5 positions (use Select Team or multi-select)
4. Edit the Department field to change from "Network Operations" to "Operations and Logistics"
5. Add an Effective Date of January 1, 2027 (or your Q1 start date)
6. Save the changes

**What Happens:**

- In org chart views, you'll immediately see these positions in Operations and Logistics (the "after" state)
- In the Forecast module, these 5 positions will appear under Network Operations through December 2026
- Starting January 2027, these 5 positions will appear under Operations and Logistics
- The headcount for Network Operations will show -5 starting January 2027
- The headcount for Operations and Logistics will show +5 starting January 2027

{% hint style="info" %}
**Screenshot Placeholder:** Forecast view showing headcount by department over time, with Network Operations decreasing from 25 to 20 in Q1 2027, and Operations and Logistics increasing from 30 to 35 in Q1 2027
{% endhint %}

### Example 2: Phased Reorganization

**Scenario:** You're planning a major reorganization where multiple teams will move to new departments over the course of three quarters.

**Using Effective Dates:**

1. Create a scenario for the full reorganization
2. For teams moving in Q2 2026, set effective date to April 1, 2026
3. For teams moving in Q3 2026, set effective date to July 1, 2026
4. For teams moving in Q4 2026, set effective date to October 1, 2026

**What Happens:**

- Your forecast will show the gradual transition of teams
- Budget owners can see the phased impact on departmental headcount and costs
- You can model the change implementation plan and see its effects over time

### Example 3: Future Internal Transfer

**Scenario:** An employee is being promoted from an IC role in Sales to a manager role in Marketing, effective next month.

**Using Effective Dates:**

1. In a scenario, find the employee's current position
2. Change their Department to "Marketing"
3. Change their Job Title to the new manager title
4. Change their Manager to their new reporting relationship
5. Set an Effective Date for next month
6. Save the changes

**What Happens:**

- The org chart view will show the employee in their new position
- The Forecast will show them in Sales this month, then in Marketing starting next month
- Sales headcount decreases by 1 next month, Marketing increases by 1

## Viewing Effective Dates in Forecast

The Forecast module is where effective dates truly come to life, allowing you to see time-phased changes across your organization.

### Accessing Forecast

1. From the main navigation or org chart view, click the dropdown that says "Directory"
2. Select "Forecast"
3. You'll see a pivot-table-style view with aggregation options

{% hint style="info" %}
**Screenshot Placeholder:** Navigation dropdown showing Directory, Forecast, Workforce Hub, and Productivity options, with Forecast highlighted
{% endhint %}

### Forecast Configuration

The Forecast module has several key controls:

**Row Aggregation:** Choose what to aggregate by (People, Department, Location, Country, Employee Type, etc.)
- Example: Select "Department" to see each department as a row

**Metric Selection:** Choose "Headcount" or "Cost"
- Headcount shows the count of positions
- Cost shows salary and other monetary fields

**Monetary Fields:** When viewing Cost, select which salary components to include (Base Salary, Bonuses, Allowances, etc.)

**Time Aggregation:** Choose Monthly, Quarterly, or Yearly views
- Monthly: See changes month-by-month
- Quarterly: See changes by quarter
- Yearly: See annual projections

**Year Selection:** When viewing Monthly or Quarterly, choose which of the next 5 years to display

{% hint style="info" %}
**Screenshot Placeholder:** Forecast toolbar showing aggregation dropdown (Department selected), Headcount/Cost toggle, time period selector (Quarterly selected), and year dropdown (2026 selected)
{% endhint %}

### Interpreting Forecast with Effective Dates

When you have effective dates in your scenario:

- **Before the effective date:** The position appears in its original location (before state)
- **After the effective date:** The position appears in its new location (after state)
- **Headcount changes:** Shows as increase (+) in destination department, decrease (-) in origin department
- **Cost changes:** Cost moves from one department to another on the effective date

For example, if you view a departmental forecast by quarter:

| Department | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 |
|---|---|---|---|---|
| Network Operations | 25 | 25 | 20 | 20 |
| Operations & Logistics | 30 | 30 | 35 | 35 |

This shows that 5 positions moved from Network Operations to Operations & Logistics in Q3 2026.

## Effective Dates vs. Hire/Termination Dates

Choosing the right date field depends on what you're trying to model:

### When to Use Hire Dates and Termination Dates

Use this approach when you want to show positions being **created and eliminated**, not just moved:

**Scenario:** Moving 5 people from Network Operations to Operations & Logistics using hire/termination dates.

**Method:**
1. Set termination dates on the 5 positions in Network Operations
2. Create 5 new positions in Operations & Logistics
3. Set hire dates on the new positions to match the termination dates

**Result in Forecast:**
- Network Operations shows -5 positions
- Operations & Logistics shows +5 positions
- This approach shows the positions as being eliminated and recreated rather than transferred

**When to use this approach:**
- Modeling actual layoffs or position eliminations
- Creating entirely new roles that didn't previously exist
- Planning new hiring to fill vacancies
- When you want to show distinct "close" and "open" actions

### When to Use Effective Dates

Use this approach when you want to show positions **changing attributes** but continuing to exist:

**Scenario:** Moving 5 people from Network Operations to Operations & Logistics using effective dates.

**Method:**
1. Select the 5 positions in Network Operations
2. Change their Department field to "Operations & Logistics"
3. Set an effective date for when the change occurs

**Result in Forecast:**
- Network Operations shows -5 positions starting on the effective date
- Operations & Logistics shows +5 positions starting on the effective date
- The same 5 positions are simply changing location

**When to use this approach:**
- Internal transfers or reorganizations
- Changing reporting structures
- Moving teams between departments
- Any change where the position continues to exist but with different attributes

### The Key Difference

**Effective dates** preserve position continuity - the same position just changes attributes at a point in time.

**Hire and termination dates** show positions being eliminated and new positions being created.

For most reorganization scenarios, effective dates are the cleaner and more accurate approach.

## Special Considerations for New Positions

When you create a brand new position in a scenario (one that doesn't exist in the main org), the behavior is different:

**Before state:** Empty (the position didn't exist)
**After state:** The position as you created it

**In Forecast:**
- The position only appears in its "after" state location
- It doesn't show as moving from anywhere
- It shows as +1 headcount in its assigned department

**Example:**
- You create a new "Senior Manager, Marketing" position in a scenario
- You assign it to the Marketing department
- Even if you set an effective date, the position only ever shows in Marketing
- It appears as +1 in Marketing starting from the effective date (or immediately if no effective date is set)

{% hint style="info" %}
**Key Insight:** For new positions, effective dates control **when** the position appears in forecasts, but not **where** it moves from, because there is no "before" state.
{% endhint %}

## Working with Before, After, and Changes Views

Scenarios have three view modes that help you understand the impact of changes:

### Show Before

Displays the state of the organization as it exists in the main org (current reality, before any scenario changes).

{% hint style="warning" %}
**Remember:** "Show Before" always references the main org, not the start of the scenario. It's the baseline from which all changes are measured.
{% endhint %}

### Show After

Displays the state of the organization with all scenario changes applied (the proposed future state).

### Show Changes

Displays the delta between Before and After - what's increasing, decreasing, or changing.

**In Forecast, Show Changes reveals:**
- Which departments are gaining headcount (+) and when
- Which departments are losing headcount (-) and when
- The cost impact of changes over time

{% hint style="info" %}
**Screenshot Placeholder:** Scenario dropdown showing "Show Before," "Show After," and "Show Changes" options with "Show Changes" selected
{% endhint %}

### Using Changes View with Effective Dates

When viewing "Show Changes" in Forecast with effective dates configured:

- You'll see **no change** in the periods before the effective date
- You'll see **+/- changes** starting from the effective date forward
- This clearly shows when and where organizational impacts occur

**Example:**

| Department | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 |
|---|---|---|---|---|
| Network Operations | 0 | 0 | -5 | -5 |
| Operations & Logistics | 0 | 0 | +5 | +5 |

This Changes view shows that the reorganization impact begins in Q3 2026.

## Practical Applications for Business Planning

### Multi-Year Workforce Planning

Use effective dates to model hiring plans across multiple years:

1. Create positions for planned 2026 hiring with hire dates throughout 2026
2. Create positions for planned 2027 hiring with hire dates throughout 2027
3. View the Forecast in yearly aggregation to see headcount growth over time
4. Switch to quarterly or monthly view to see detailed phased hiring plans

### Budget Planning with Phased Changes

Model the cost impact of reorganizations that happen mid-year:

1. Plan organizational changes with effective dates aligned to fiscal quarters
2. View the Forecast in quarterly cost view
3. See exactly when departmental budgets will be impacted
4. Share forecast views with budget owners to align on timing

### Scenario Comparison with Different Timing

Create multiple scenarios with the same changes but different effective dates:

- Scenario A: Reorganization effective Q2 2026
- Scenario B: Reorganization effective Q4 2026

Compare the cost and headcount impacts of different timing options to inform decision-making.

## Common Questions

**What happens if I don't set an effective date on a changed position?**

The change is considered to take effect immediately. In Forecast views, the position will appear in its "after" state for all time periods.

**Can I set different effective dates on different positions within the same scenario?**

Yes. You can have multiple effective dates throughout a single scenario, allowing you to model complex phased changes.

**How far into the future can I forecast?**

The Forecast module shows up to 5 years into the future from the current date.

**Do effective dates work for all field types?**

Yes, effective dates work with any position attribute changes - department, location, manager, job title, salary, or any custom fields.

**What's the difference between effective date and hire date?**

Hire dates represent when someone starts in a position (joining the organization or filling a vacancy). Effective dates represent when a change to an existing position takes effect (like a transfer or reorganization). Use hire dates for new employees, effective dates for organizational changes.

**If I move someone with an effective date, do they still show up in their old department in org chart views?**

No. In org chart views within the scenario, you'll see the "after" state - the person in their new department. The "before" state (their old department) is only visible if you select "Show Before" or when viewing the main org. However, in **Forecast views**, they'll appear in their old department until the effective date, then in their new department after.

---

## Related Articles

- [Understanding the Forecast Module](../forecast/overview.md)
- [Creating and Managing Scenarios](creating-scenarios.md)
- [Before, After, and Changes Views](before-after-changes.md)
