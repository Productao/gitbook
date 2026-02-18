---
description: Creating and managing headcount forecasts
hidden: false
---

# Building Headcount Forecasts

Building a headcount forecast in Agentnoon means creating a Scenario with planned changes, then viewing that Scenario in Forecast mode to see projections over time. This guide walks you through the complete process.

## Understanding the Forecast Workflow

**Key principle:** Forecasts are views of your data, not separate documents. You build forecasts by:
1. Creating Scenarios with planned changes
2. Using hire dates and effective dates to phase changes over time
3. Viewing those Scenarios in Forecast mode

**What you need:**
- A Scenario (or use Main Org for current state forecast)
- Positions with hire dates for future headcount
- Termination dates if modeling attrition
- Effective dates for phased organizational changes

---

## Method 1: Forecast Current State (No Changes)

**Use case:** Report current workforce size and cost

**Steps:**
1. Go to Main Org
2. Click Forecast at the top
3. Aggregator: Choose Department, Location, or desired dimension
4. Toggle: Headcount
5. Time period: Yearly, Quarterly, or Monthly
6. Export or analyze

**What you'll see:** Current headcount distributed across your chosen aggregation, projected forward (headcount persists unless termination dates exist)

---

## Method 2: Forecast with Hire Dates (Phased Hiring Plan)

**Use case:** Plan staggered hiring across quarters

### Step 1: Create a Scenario
1. Click "Create Scenario"
2. Name it descriptively (e.g., "2026 Engineering Hiring Plan")
3. Select scenario type (usually Full Org)
4. Click Create

### Step 2: Add Positions with Hire Dates
1. In your scenario, navigate to the department where you'll add positions
2. Click "+ Add Position" or use bulk add
3. Fill in position details:
   - Title
   - Department
   - Manager (reporting relationship)
   - Salary
   - **Hire Date** - THIS IS CRITICAL for forecasting
4. Set hire dates based on your hiring timeline:
   - Q1 hires: January, February, or March dates
   - Q2 hires: April, May, or June dates
   - Q3 hires: July, August, or September dates
   - Q4 hires: October, November, or December dates

**Example:**
- Add 3 Software Engineers, hire date: March 15, 2026
- Add 2 Product Managers, hire date: June 1, 2026
- Add 5 Sales Reps, hire date: September 1, 2026

### Step 3: View in Forecast
1. Stay in your scenario
2. Click Forecast at the top
3. Aggregator: Department (or desired dimension)
4. Toggle: Headcount
5. Time period: Quarterly
6. Year: 2026
7. View: Show After

**What you'll see:**
- Q1 2026: Current headcount + 3 (March hires)
- Q2 2026: Previous + 2 (June hires)
- Q3 2026: Previous + 5 (September hires)
- Q4 2026: Same as Q3 (no new hires)

### Step 4: Analyze Cost Impact
1. Toggle: Switch to Cost
2. Monetary fields: Select Salary (or add Bonus, etc.)
3. View the workforce cost increase by quarter

**What you'll see:** Total salary cost increases as new hires join

---

## Method 3: Forecast with Effective Dates (Organizational Changes Over Time)

**Use case:** Model a reorganization or departmental transfer happening in the future

### Step 1: Make Organizational Changes
1. In a scenario, select positions to move (e.g., 5 people moving from Network Ops to Operations & Logistics)
2. Change their department field to the new department
3. **Assign an effective date** to all these changes (e.g., January 1, 2027)

### Step 2: View in Forecast
1. Click Forecast
2. Aggregator: Department
3. Toggle: Headcount or Cost
4. Time period: Quarterly or Yearly
5. Select years spanning the effective date (2026 and 2027)

**What you'll see:**
- Through Q4 2026: People remain in Network Ops
- Starting Q1 2027: People appear in Operations & Logistics
- **Show Changes view:** -5 Network Ops, +5 Operations & Logistics starting Q1 2027

---

## Method 4: Model Attrition with Termination Dates

**Use case:** Plan for expected attrition or retirements

### Step 1: Identify Positions Closing
1. In a scenario, find positions that will close due to retirement, planned departures, or budget cuts
2. Close those positions
3. Assign termination dates

### Step 2: View in Forecast
1. Forecast mode
2. Aggregator: Department
3. Toggle: Headcount
4. Time period: Quarterly
5. View: Show Changes

**What you'll see:**
- Negative headcount changes (-1, -2, etc.) in quarters when positions close
- Workforce cost decreases accordingly

---

## Method 5: Combined Hiring and Attrition Forecast

**Use case:** Model realistic workforce dynamics with both hiring and departures

### Step 1: Add Growth Positions with Hire Dates
- Add new positions with future hire dates (net growth)

### Step 2: Close Positions with Termination Dates
- Model expected turnover or planned departures

### Step 3: View Net Impact
1. Forecast → Show Changes view
2. Aggregator: Department
3. Time period: Quarterly

**Example scenario:**
- Q1: +10 hires, -3 departures = +7 net headcount
- Q2: +5 hires, -2 departures = +3 net headcount
- Q3: +8 hires, -4 departures = +4 net headcount
- Q4: +2 hires, -1 departure = +1 net headcount
- **Annual net growth:** +15 headcount

---

## Multi-Department Hiring Plan

**Use case:** Coordinate hiring across multiple departments

### Step 1: Create Department-Specific Targets
In your scenario, add positions for each department:
- Engineering: 15 positions across Q1-Q4
- Sales: 10 positions in Q2-Q3
- Marketing: 5 positions in Q1
- Product: 8 positions across all quarters

### Step 2: Stagger Hire Dates
Distribute hire dates realistically:
- Don't hire everyone on quarter start dates
- Spread hires throughout the quarter
- Consider ramp-up time (new hires may start mid-quarter)

### Step 3: Analyze Aggregated Impact
1. Forecast → Show After
2. Aggregator: Department
3. Toggle: Headcount
4. Time period: Quarterly
5. Review hiring ramp by department

### Step 4: Check Budget Impact
1. Toggle: Cost
2. View total salary increase by quarter
3. Ensure it aligns with budget approvals

---

## Best Practices for Headcount Forecasting

### Use Realistic Hire Dates
- Don't cluster all hires on Jan 1, Apr 1, Jul 1, Oct 1
- Spread hires throughout quarters
- Factor in recruiting timelines (don't plan 50 hires in one month)

### Plan for Ramp Time
- New hires take time to onboard and reach full productivity
- Consider staggered starts to avoid overwhelming managers
- Budget for overlapping periods if backfilling departing employees

### Model Attrition Realistically
- Historical attrition rate (e.g., 10% annually)
- Known retirements or planned departures
- Seasonal fluctuations (higher turnover in Q1, lower in Q4)

### Coordinate with Budget Cycles
- Align hire dates with budget availability
- Match quarterly hiring to quarterly budget releases
- Plan for budget cuts or freezes

### Use Effective Dates for Non-Hire Changes
- Promotions with future effective dates
- Department transfers
- Salary adjustments planned for later

### Keep Scenarios Organized
- Name scenarios clearly: "2026 Q2-Q4 Hiring Plan"
- Add descriptions explaining assumptions
- Tag scenarios by purpose (e.g., "Approved Plan", "Stretch Goal", "Conservative")

---

## Common Challenges and Solutions

**Challenge:** "I added 10 positions but Forecast only shows +5"
- **Solution:** Check hire dates. Only positions with hire dates in the displayed time period appear. If you're viewing Q1 but hire dates are in Q2, they won't show in Q1.

**Challenge:** "Forecast shows headcount growth but my budget didn't increase"
- **Solution:** Adding positions without closing others increases net headcount and cost. To stay budget-neutral, close equivalent positions or adjust salaries.

**Challenge:** "I can't see quarterly progression, just annual totals"
- **Solution:** Change Time Period selector from "Yearly" to "Quarterly", then select the year you want to view.

**Challenge:** "My hiring plan looks lumpy (big spikes in certain quarters)"
- **Solution:** Spread hire dates more evenly. Instead of 20 hires on July 1, stagger them: 7 in July, 7 in August, 6 in September.

**Challenge:** "I need to forecast for 2+ years but only see one year"
- **Solution:** For multi-year view, switch Time Period to "Yearly". You'll see columns for 2024, 2025, 2026, 2027, 2028.

---

## Exporting and Sharing Your Forecast

Once you've built your forecast:

1. **Configure the view:**
   - Set aggregator, time period, headcount/cost toggle
   - Apply any filters (e.g., only certain divisions)

2. **Export to CSV:**
   - Click Export button
   - Open in Excel
   - Format for presentations or financial planning tools

3. **Share with stakeholders:**
   - Export separate views for different audiences:
     - Finance: Department aggregation, Cost view, Quarterly
     - HR: Department aggregation, Headcount view, Monthly
     - Executives: High-level aggregation, Yearly, Both Headcount and Cost

4. **Present the changes:**
   - Use "Show Changes" view to highlight net impact
   - Explain which departments are growing vs. shrinking
   - Tie to strategic priorities

---

## Next Steps

- **[Budget Planning & Tracking](budget-planning-tracking.md)** - Align forecasts with budget constraints
- **[Forecast Reports & Exports](reports-exports.md)** - Advanced reporting techniques
- **[Multi-Year Planning](multi-year-planning.md)** - Long-term strategic workforce planning
- **[Time-Based Planning](../scenarios/time-based-planning.md)** - More on effective dates and phasing
