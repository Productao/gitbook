---
description: Budget planning and cost tracking in Forecast
hidden: false
---

# Budget Planning & Tracking

Agentnoon's budget planning capabilities help you set workforce cost targets and track progress toward those goals. While not a full FP&A tool, Agentnoon provides essential budget management for workforce planning scenarios.

## Understanding Budget in Agentnoon

**What budget tracking means in Agentnoon:**
- Set a target budget when creating scenarios
- Track how scenario changes affect your budget (+/- cost)
- See real-time progress toward budget goals
- Understand whether you're over or under budget

**What Agentnoon does NOT do (today):**
- Track actuals vs. budget over time
- Provide variance analysis against historical spend
- Support budget targets in Forecast module (coming soon)
- Multi-level budget approvals with budget limits

**Current functionality:** Budget tracking exists at the **scenario level**, not in Forecast itself.

---

## Setting a Budget When Creating a Scenario

### Step 1: Create a New Scenario
1. Click "Create Scenario"
2. Name your scenario (e.g., "2026 Q2 Budget Planning")
3. Before clicking Create, look for **"Scenario Budget"** field

### Step 2: Enter Your Budget Target
**Options:**
- **Positive budget** (e.g., +$500,000): You have this much to spend on new headcount
- **Negative budget** (e.g., -$10,000,000): You need to cut costs by this amount
- **Zero budget**: Neutral planning, no specific target

**Example scenarios:**
- "Growth Scenario": Budget = +$2,000,000 (plan to add $2M in new hires)
- "Cost Reduction Scenario": Budget = -$5,000,000 (reduce workforce cost by $5M)
- "Reorg Scenario": Budget = $0 (cost-neutral reorganization)

### Step 3: Create the Scenario
Click Create. The scenario now has a budget target.

---

## The OpEx Panel (Scenario Impacts and Changes)

Once you're in a scenario with a budget, the **OpEx Panel** (also called "Scenario Impacts and Changes" panel) shows your budget status.

### Accessing the OpEx Panel
- It appears as a right sidebar in scenarios
- If hidden, click the panel icon to expand it
- Shows real-time updates as you make changes

> **[Screenshot placeholder: OpEx panel showing budget status and change tracking]**

### What the OpEx Panel Shows

**Budget section (top):**
- **Target Budget:** The budget you set when creating the scenario
- **Current Impact:** Net cost change from your modifications
- **Remaining Budget:** How much budget you have left (or how far over you are)

**Example display:**
```
Target Budget: -$10,000,000 (cut $10M)
Current Impact: -$7,500,000 (cut $7.5M so far)
Remaining: -$2,500,000 (need to cut $2.5M more)
```

**Changes section (below):**
- **Additions:** New positions added (shows count and cost)
- **Reductions:** Positions closed (shows count and cost saved)
- **Modifications:** Existing positions changed (shows net cost impact)
- **Net Headcount Change:** Total headcount +/-
- **Net Cost Change:** Total cost +/-

---

## Budget Planning Workflows

### Workflow 1: Growth Planning with a Budget

**Scenario:** You have $3M to add new headcount in 2026.

**Steps:**
1. Create scenario with budget: +$3,000,000
2. Add positions for planned hires:
   - 10 Software Engineers @ $150K each = $1,500,000
   - 5 Product Managers @ $180K each = $900,000
   - 8 Sales Reps @ $120K each = $960,000
3. Check OpEx Panel:
   - Current Impact: +$3,360,000
   - Remaining: -$360,000 (over budget!)
4. Adjust:
   - Remove 3 positions
   - Or reduce salaries on some positions
   - Or accept the overage and document the need

**Key insight:** The OpEx Panel updates in real-time, so you always know if you're within budget.

### Workflow 2: Cost Reduction Planning (RIF)

**Scenario:** You need to reduce workforce cost by $5M.

**Steps:**
1. Create scenario with budget: -$5,000,000
2. Identify positions to close:
   - Use Directory view with sorting by salary
   - Filter by department if cuts are targeted
   - Consider span of control and organizational impact
3. Close positions until budget target is met:
   - Close 25 positions averaging $200K = -$5,000,000
4. OpEx Panel shows:
   - Current Impact: -$5,000,000
   - Remaining: $0 (budget target met)
5. Review organizational structure in Org Chart to ensure no broken hierarchies

### Workflow 3: Cost-Neutral Reorganization

**Scenario:** Reorganize teams without changing total budget.

**Steps:**
1. Create scenario with budget: $0
2. Make organizational changes:
   - Move people between teams (no cost impact)
   - Close some positions (-$1M)
   - Add equivalent positions (+$1M)
3. OpEx Panel should show:
   - Current Impact: ~$0 (slight variance is okay)
   - Headcount: May change even if cost is neutral

**Pro tip:** Moving existing employees between departments doesn't change cost. Only adding/closing positions or changing salaries affects budget.

---

## Budget Management Tips

### Set Realistic Budgets
- Base budget targets on board approvals or finance guidance
- Account for fully-loaded costs (salary + benefits + taxes) if relevant
- Consider geographical cost differences

### Monitor Budget Throughout Planning
- Check OpEx Panel frequently as you make changes
- Don't wait until the end to see if you're over/under
- Adjust incrementally rather than overhauling at the end

### Adjust Budget Mid-Planning if Needed
You can update the scenario budget after creation:
1. Go to OpEx Panel settings (gear icon)
2. Update budget target
3. New target applies immediately

**When to adjust:**
- Finance provides revised budget guidance
- You realize initial budget was based on wrong assumptions
- Strategic priorities shift mid-planning

### Document Budget Decisions
When submitting scenarios for approval, include:
- Rationale for budget target
- Explanation of any budget overages
- Trade-offs made to stay within budget
- Alternatives considered

---

## Budget and Forecast Integration

**Current state:** Budgets live in Scenarios, not in Forecast.

**How to use them together:**
1. Create a scenario with a budget target
2. Make changes to meet that budget
3. View the scenario in Forecast to see timing:
   - When do cost savings start (based on termination/effective dates)
   - When do new hires add cost (based on hire dates)
   - Quarterly or monthly budget impact

**Example:**
- Budget target: Cut $2M annually
- Close 10 positions with staggered termination dates:
   - Q1: Close 3 positions (-$600K)
   - Q2: Close 4 positions (-$800K)
   - Q3: Close 3 positions (-$600K)
- View in Forecast:
   - See cost reduction phased across quarters
   - Show partial-year savings vs. full-year run rate

---

## Compensation and Rate Cards in Budget Planning

**How rate cards help with budgeting:**

When adding new positions, rate cards auto-populate salaries based on:
- Pay grade
- Job family
- Location
- Other configured criteria

**Benefit for budgeting:**
- Consistent, realistic salary estimates
- No need to guess market rates
- Automatically accounts for geographic differences

**Example:**
- You need to add 10 Software Engineer II positions
- Rate card: SE II in SF = $170K, SE II in Austin = $140K
- Add 5 in SF + 5 in Austin = ($170K × 5) + ($140K × 5) = $1,550,000
- Budget impact is automatically calculated

---

## Reporting Budget Status

### Internal Reporting
Export from OpEx Panel:
- Budget target vs. actual changes
- Net headcount change
- Department-by-department breakdown

### External Reporting (Finance, Leadership)
1. Take screenshot of OpEx Panel showing budget status
2. Export Forecast view showing cost impact over time
3. Create summary slide:
   - Budget target: $X
   - Current plan: $Y
   - Variance: $Z
   - Explanation of any variance

### Scenario Comparison for Budget Options
Create multiple scenarios with different budget approaches:
- "Aggressive Cut": -$10M
- "Moderate Cut": -$5M
- "Minimum Cut": -$2M

Compare side-by-side to show trade-offs and recommend one.

---

## Limitations and Future Enhancements

**Current limitations:**
- No budget targets in Forecast module itself (only in Scenarios)
- No automatic budget alerts or warnings
- No actuals vs. budget variance tracking over time
- No department-level budget limits (only scenario-level)

**Planned enhancements (coming soon):**
- Budget targets in Forecast
- Multi-level budget approvals with limits
- Percentage-based budget targets (e.g., "Cut 10%")
- Better budget reporting and dashboards

**Workaround today:**
- Use Scenario budgets for planning
- Export Forecast data to Excel for detailed variance tracking
- Manually calculate department-level budget allocation

---

## Common Questions

**Q: Can I set different budgets for different departments?**
A: Not directly. The budget is scenario-wide. Workaround: Create separate scenarios per department (e.g., "Engineering Budget Scenario", "Sales Budget Scenario").

**Q: What if I'm slightly over budget?**
A: Document the rationale. Small overages (<5%) are often acceptable if justified by strategic priorities. Alternatively, make small adjustments to stay within budget.

**Q: How do I know if my actual spend matches my forecast?**
A: Agentnoon doesn't track actuals vs. forecast automatically. You'll need to compare your HRIS payroll data against your Agentnoon forecast manually or in Excel.

**Q: Can I model a hiring freeze?**
A: Yes. Don't add any new positions with future hire dates. If modeling a freeze mid-year, close any open positions (those without employees assigned).

**Q: How does fully-loaded cost work?**
A: If you track fully-loaded cost (salary + benefits + taxes), configure those as additional compensation fields in your data. Include them in Forecast monetary fields selection. Rate cards can populate fully-loaded costs too.

---

## Next Steps

- **[Building Headcount Forecasts](building-headcount-forecasts.md)** - Create forecasts aligned with your budget
- **[Forecast Reports & Exports](reports-exports.md)** - Share budget status with stakeholders
- **[IPR Modeling Budget Cuts](../use-case-tutorials/modeling-budget-cuts.md)** - Step-by-step RIF planning tutorial
