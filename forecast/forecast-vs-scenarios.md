---
description: Understanding when to use Forecast vs Scenarios
icon: git-compare
hidden: false
---

# Forecast vs Scenarios

Forecast and Scenarios are two powerful modules in Agentnoon that work together but serve different purposes. Understanding when to use each will help you plan more effectively and avoid confusion.

## The Core Difference

### Forecast: Visualization & Reporting
**Forecast is a view-only module** for visualizing workforce data over time.

**What Forecast does:**
- Displays data as a pivot table (rows × columns × values)
- Shows headcount and cost projections over time
- Aggregates data by department, location, employee type, etc.
- Provides time-based views (monthly, quarterly, yearly)
- Exports projections for reporting and budgeting

**What Forecast does NOT do:**
- Create or modify positions
- Make organizational changes
- Input new data
- Approve changes
- Set targets or goals (coming soon)

### Scenarios: Planning & Modeling
**Scenarios are workspaces** for making organizational changes and testing "what-if" alternatives.

**What Scenarios do:**
- Create, modify, and close positions
- Move positions between departments
- Change reporting relationships
- Assign employees to positions
- Model reorganizations and RIFs
- Track before/after states and impacts
- Submit changes for approval

**What Scenarios do NOT do:**
- Directly create time-based projections (you view those in Forecast)
- Replace the Main Org data (they're sandboxes)
- Aggregate data as flexibly as Forecast

---

## How They Work Together

Forecast and Scenarios are complementary tools:

```
1. Create a Scenario
   ↓
2. Make organizational changes (add positions, move people, close roles)
   ↓
3. Assign hire dates and effective dates to changes
   ↓
4. View the Scenario in Forecast
   ↓
5. See time-based projections of your changes
   ↓
6. Export forecast data for stakeholder presentations
```

**Example workflow:**
1. You create a scenario called "2026 Engineering Hiring Plan"
2. In the scenario, you add 20 new engineering positions with hire dates staggered across Q1-Q4
3. You view the scenario in Forecast (monthly view, grouped by department)
4. Forecast shows you exactly when each hire starts and the monthly cost ramp-up
5. You export the forecast to CSV and share with Finance for budget approval

---

## When to Use Forecast

### Annual Budget Planning
**Use Forecast when:**
- You need to see total workforce cost by department over the next year
- You're preparing budget presentations for leadership
- You want to understand how hiring plans impact monthly/quarterly budgets
- You need to aggregate cost across multiple dimensions (location, department, pay grade)

**Why Forecast:**
- Pivot table functionality lets you slice data by any aggregator
- Time-based views show exactly when costs increase
- Export to CSV for use in budget tools and presentations
- Quickly compare before/after and changes views

**Example:**
You have 3 scenarios (Engineering Hiring Plan, Sales Expansion, Operations Efficiency). You view each in Forecast (yearly view, grouped by department) to see which plan fits within your $50M workforce budget.

### Headcount Projections & Reporting
**Use Forecast when:**
- You need to report headcount growth by quarter to the board
- You're tracking how many positions will be filled by year-end
- You want to see geographic distribution of workforce over time
- You need to export headcount by department for HR planning

**Why Forecast:**
- Headcount persists over time (a 2026 hire stays in 2027 unless terminated)
- Hire dates control when positions appear in projections
- Easy to toggle between headcount and cost views
- Filters let you narrow to specific populations

**Example:**
Your board asks: "What's our headcount growth by quarter in 2026?" You use Forecast (quarterly view, grouped by department, headcount toggle) to show Q1: 500, Q2: 520, Q3: 545, Q4: 560.

### Multi-Year Strategic Planning
**Use Forecast when:**
- You're modeling 3-5 year workforce growth
- You need to understand long-term cost trajectory
- You're planning phased expansions over multiple years
- You want to compare different multi-year growth scenarios

**Why Forecast:**
- Yearly view shows up to 5 years at once
- Effective dates and hire dates extend years into the future
- Scenarios can model phased growth (2026 hires, 2027 hires, 2028 hires)
- Export multi-year projections for strategic planning presentations

**Example:**
You create 3 scenarios (Conservative Growth, Moderate Growth, Aggressive Growth) with different hiring plans across 2026-2028. You view each in Forecast (yearly view, 5-year horizon) to understand long-term cost implications.

### Comparing Multiple Scenarios
**Use Forecast when:**
- You have 3 reorg options and need to compare their cost impact
- You want to see which hiring plan fits the budget best
- You're evaluating different budget cut scenarios side-by-side
- You need to present scenario comparisons to stakeholders

**Why Forecast:**
- Open each scenario in Forecast, export to CSV, compare in Excel
- Consistent aggregation across scenarios for apples-to-apples comparison
- Show Changes view highlights deltas from Main Org
- Quickly toggle between scenarios to see differences

**Example:**
You have "Reorg Option A", "Reorg Option B", and "Reorg Option C" scenarios. You view each in Forecast (Show Changes, grouped by department) to see which option has the lowest cost impact while achieving restructuring goals.

---

## When to Use Scenarios

### Organizational Restructuring
**Use Scenarios when:**
- You're reorganizing departments or teams
- You're changing reporting relationships
- You're moving positions between business units
- You need to model a reorg before implementing

**Why Scenarios:**
- Org chart view shows the reporting structure clearly
- Change Tracker shows exactly what changed (moves, adds, closes)
- Before/after comparison helps stakeholders visualize the new structure
- Approval workflows ensure proper review before implementation

**Example:**
You're merging Network Operations into Operations & Logistics. You create a scenario, move 15 positions from Network Ops to Ops & Logistics, reassign reporting relationships, submit for approval.

### Hiring Plans & Workforce Expansion
**Use Scenarios when:**
- You're adding new positions to your organization
- You need to specify which roles to hire and when
- You're planning who reports to whom in the new structure
- You need stakeholder approval for new positions

**Why Scenarios:**
- Add positions with full details (title, department, manager, salary, hire date)
- Use rate cards to auto-populate salaries for new roles
- Track budget impact in real-time with OpEx Panel
- Submit hiring plan for approval before moving forward

**Example:**
You create "Q2 2026 Sales Hiring" scenario, add 10 new Account Executive positions with hire dates in April-June, assign them to 3 different sales managers, set salaries using rate card, submit for CFO approval.

### Modeling Budget Cuts or RIFs
**Use Scenarios when:**
- You need to identify which positions to close to meet budget targets
- You're modeling layoffs or workforce reductions
- You need to see the organizational impact of position closures
- You want approval on which positions to eliminate

**Why Scenarios:**
- Close positions one at a time or in bulk
- Change Tracker shows exact cost savings from closures
- Org chart view shows holes in the organization after closures
- Effective dates control when cost reductions take effect
- Approval workflows ensure proper governance

**Example:**
You're asked to reduce workforce cost by $5M. You create "Budget Reduction Scenario", close 50 positions strategically, use Change Tracker to confirm $5M savings, submit for executive approval.

### Position-Level Changes
**Use Scenarios when:**
- You're changing a specific person's salary or title
- You're promoting someone and need to update their position details
- You're moving an employee from one team to another
- You're backfilling a vacant position

**Why Scenarios:**
- Edit individual position details (salary, title, manager, department)
- Attach employees to open positions or detach from closed positions
- Effective dates allow you to schedule changes for future dates
- Change Tracker logs every modification for audit purposes

**Example:**
Sarah Chen is being promoted from Senior Engineer to Engineering Manager. You create a scenario, change her title, increase her salary, reassign 5 engineers to report to her, set effective date of January 1, 2026.

### Testing "What-If" Alternatives
**Use Scenarios when:**
- You want to explore multiple options without committing
- You need to compare different approaches (Scenario A vs B vs C)
- You're unsure which organizational design is best
- You want to experiment without affecting Main Org

**Why Scenarios:**
- Create unlimited scenarios to test different approaches
- Scenarios don't modify Main Org (they're sandboxes)
- Compare scenarios side-by-side using Scenario Comparisons
- Delete scenarios that don't work out—no harm done

**Example:**
You're unsure whether to centralize or decentralize IT. You create "Centralized IT" scenario and "Decentralized IT" scenario, model both structures, compare cost/headcount impacts, present both to leadership for decision.

---

## Choosing the Right Tool

### Use This Decision Tree

**Question 1:** Do you need to make organizational changes (add/close/move positions)?
- **Yes** → Use Scenarios
- **No** → Go to Question 2

**Question 2:** Do you need to see time-based projections (monthly, quarterly, yearly)?
- **Yes** → Use Forecast
- **No** → Go to Question 3

**Question 3:** Do you need to report aggregated data (by department, location, etc.)?
- **Yes** → Use Forecast
- **No** → Go to Question 4

**Question 4:** Do you need approval for changes before implementation?
- **Yes** → Use Scenarios
- **No** → Use either (or both)

---

## Common Use Cases: Which Tool?

| Use Case | Tool | Why |
|---|---|---|
| **Annual budget planning** | Forecast | Need time-based cost projections by department |
| **Creating a reorg plan** | Scenarios | Need to restructure org and track changes |
| **Viewing reorg budget impact** | Forecast (of the scenario) | Need to see cost/headcount over time |
| **Adding 20 new positions** | Scenarios | Need to input new positions with details |
| **Seeing when those 20 positions start** | Forecast (of the scenario) | Need to see monthly hire date projections |
| **Reporting headcount by quarter** | Forecast | Need time-based aggregated view |
| **Closing positions for budget cuts** | Scenarios | Need to make org changes and track savings |
| **Comparing 3 budget cut options** | Scenarios (3 of them) + Forecast | Model in scenarios, compare projections in Forecast |
| **Moving someone to new department** | Scenarios | Need to make position-level change |
| **Exporting workforce cost for CFO** | Forecast | Need aggregated cost data export |
| **Submitting hiring plan for approval** | Scenarios | Need approval workflow for new positions |
| **Multi-year growth projections** | Forecast (of scenarios with future hires) | Need 5-year time-based view |

---

## Integrated Workflow: Scenarios + Forecast

Here's how Forecast and Scenarios work together in a typical workforce planning cycle:

### Phase 1: Planning (Scenarios)
1. Create a new scenario (e.g., "2026 Annual Plan")
2. Add new positions with hire dates for phased hiring
3. Close positions to reflect attrition or budget cuts
4. Move positions between departments to reflect reorg
5. Assign effective dates to changes that happen mid-year
6. Use Change Tracker to monitor budget impact in real-time

### Phase 2: Projection (Forecast)
7. Switch to Forecast view within your scenario
8. Configure aggregator (e.g., Department) and time period (e.g., Quarterly)
9. Toggle between headcount and cost to understand full impact
10. Use Show Changes to see deltas from current state
11. Export to CSV for budget presentations

### Phase 3: Approval (Scenarios)
12. Return to scenario org chart view
13. Review all changes in Change Tracker
14. Submit scenario for approval via OpEx Panel
15. Approvers review and approve/reject
16. If approved, scenario is ready for implementation

### Phase 4: Reporting (Forecast)
17. Once approved, generate final forecast reports
18. Export by department, location, or other dimensions
19. Share with Finance, HR, and leadership
20. Use forecasts to monitor actual vs. planned throughout the year

---

## Can You Use Both Simultaneously?

**Yes!** In fact, you should.

**Typical workflow:**
1. **Work in Scenarios** to make organizational changes
2. **Switch to Forecast** (within the same scenario) to see time-based projections
3. **Toggle back to Scenarios** to refine your changes based on forecast insights
4. **Return to Forecast** to generate final reports for stakeholders

**You don't have to choose one or the other**—they're two views of the same data, each optimized for different tasks.

---

## Key Takeaways

### Forecast Strengths
✅ Time-based projections (monthly, quarterly, yearly)
✅ Flexible aggregation (department, location, pay grade, etc.)
✅ Multi-year strategic planning (up to 5 years)
✅ Quick exports for reporting and budgeting
✅ Pivot table-style slicing and dicing

### Scenario Strengths
✅ Making organizational changes (add, close, move positions)
✅ Modeling "what-if" alternatives in sandbox environments
✅ Detailed position-level editing (salary, title, manager, etc.)
✅ Change tracking and approval workflows
✅ Before/after comparison with impact analysis

### Together They Enable
✅ **Strategic workforce planning** - Model changes in scenarios, project impact in Forecast
✅ **Budget planning** - Add positions in scenarios, see cost ramp-up in Forecast
✅ **Scenario comparison** - Create multiple scenarios, compare forecasts side-by-side
✅ **Stakeholder communication** - Build plans in scenarios, present forecasts to leadership
✅ **Governance** - Approve scenarios, use Forecast to monitor implementation

---

## Next Steps

- **[Forecast Overview](overview.md)** - Deep dive into Forecast capabilities
- **[Scenarios Overview](../scenarios/overview.md)** - Deep dive into Scenario capabilities
- **[Building Headcount Forecasts](building-headcount-forecasts.md)** - Step-by-step forecasting guide
- **[Creating Scenarios](../scenarios/creating-scenarios.md)** - Step-by-step scenario guide
- **[Budget Planning & Tracking](budget-planning-tracking.md)** - Align scenarios and forecasts with budgets
