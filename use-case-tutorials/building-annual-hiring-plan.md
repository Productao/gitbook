---
description: Annual planning workflow and best practices
hidden: false
---

# Building an Annual Hiring Plan

Model your hiring plan in Agentnoon to phase headcount growth over time, analyze budget impact, and present options to leadership for approval.

## Step 1: Gather Inputs Before Starting

Collect from department heads:
- How many new positions are needed, by role and level
- Target quarter for each hire (Q1–Q4)
- Critical hires (must-have) vs. nice-to-have hires

Define 2–3 scenarios to model: Conservative (critical roles only), Target (aligned to business plan), Aggressive (proactive/front-loaded).

## Step 2: Create the Scenario

1. Homepage > **New Scenario** > Full Org (company-wide) or Partial Org (department-focused)
2. Name it: "2026 Annual Hiring Plan - Target Growth"

## Step 3: Add Positions with Hire Dates

1. Navigate to the hiring manager's card
2. Click **Add Position** (+)
3. Fill in: Job Title, Department, Manager, **Hire Date** (e.g., April 1, 2026), Salary, Location
4. Save

The hire date controls when the position appears in Forecast — a Q2 hire date means the position doesn't count toward Q1 headcount or cost.

**Adding multiple identical positions:** After saving the first, click **Duplicate Position** and enter the quantity. Edit hire dates individually if they should start in different quarters.

**Staggering across quarters:** For 12 CSRs hired 3 per quarter, add 3 positions per quarter with corresponding hire dates (Jan 15, Apr 15, Jul 15, Oct 15).

## Step 4: Use Rate Cards for Consistent Salaries

If rate cards are configured, enable them when adding a position: select Level (e.g., IC4) and Location (e.g., San Francisco) and the salary auto-populates from your compensation bands.

Rate cards ensure consistency, reduce bias, and save time looking up salary ranges. Admins configure them in Settings > Compensation Cards.

## Step 5: View the Hiring Plan in Forecast

1. Switch to **Forecast** view in the scenario
2. Set: Aggregator = Department, Metric = Headcount, Time Period = Quarterly, Year = 2026
3. Toggle to **Show Changes** to see only new hires (not total headcount)

This shows your hiring velocity by quarter and department — e.g., +8 Engineering in Q1, +10 in Q2, etc.

Switch the metric to **Cost** and Time Period to **Yearly** for the budget impact view most useful for CFO conversations.

> Note: A position with a Q2 hire date incurs only 9 months of cost in 2026. Agentnoon prorates costs automatically, so your 2026 budget projection will be lower than the annual salary total.

## Step 6: Build Alternative Scenarios

Duplicate your Target scenario and adjust for Conservative (remove or delay lower-priority roles) and Aggressive (add stretch roles or pull hires earlier). Use **Scenario Comparisons** (homepage > select scenarios > Compare) to view side-by-side headcount, cost, and structure.

Create a summary table for leadership:

| Metric | Conservative | Target | Aggressive |
|--------|-------------|--------|------------|
| New positions | 34 | 52 | 68 |
| 2026 budget impact | $2.7M | $4.2M | $5.6M |
| Revenue growth supported | 20% | 30% | 40%+ |

## Step 7: Submit for Approval

1. Open the approved scenario > **OpEx Panel** > **Configure Submission**
2. Review approvers (Level 1: HR/Finance; Level 2: CFO/CEO)
3. Write a justification: include position count, budget impact, phasing rationale, and connection to business goals
4. Click **Submit**

## Step 8: Operationalize

After approval:
1. Export from Directory view as CSV and share with recruiting teams
2. Create job requisitions in your ATS linked to each approved position
3. Each quarter, compare actual hires to the plan — adjust hire dates or add/remove positions if business conditions change

## Key Best Practices

- Use rate cards for every new position — inconsistent salaries cause budget overruns and equity issues
- Phase hiring across quarters — don't try to hire 20 engineers in Q1 if your team fills 5 per quarter
- Account for partial-year costs — a Q3 hire at $120K costs $60K in year 1, not $120K
- Track actuals quarterly and update the scenario — hiring plans are living documents

## Related Resources

- [Planning a Reorganization](planning-reorganization.md)
- [Multi-Year Planning](../forecast/multi-year-planning.md)
- [Time-Based Planning](../scenarios/time-based-planning.md)
- [Compensation Cards](../admin/rate-cards.md)
- [Scenario Approvals](../scenarios/approvals.md)
