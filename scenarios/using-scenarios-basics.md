---
description: Core scenario actions and workflows
icon: play
hidden: false
---

# Using Scenarios - Basics

Once you've created a scenario, you're ready to model organizational changes. This section covers the core actions and workflows you'll use day-to-day when working with scenarios.

## Overview

Using scenarios involves a cycle of actions:

1. **Make changes** - Add, edit, move, or close positions
2. **Review impact** - Check the Change Tracker for cost and headcount effects
3. **Refine** - Adjust your changes based on what you see
4. **Share** - Collaborate with stakeholders
5. **Approve** - Get sign-off through approval workflows
6. **Implement** - Execute approved changes in your HRIS

This guide introduces the fundamental actions available in scenarios. For detailed step-by-step instructions, see the specific guides linked throughout.

---

## The Scenario Workspace

When you open a scenario, you see:

**Top Bar:**
- **Scenario name** - Dropdown to switch between scenarios
- **Effective date** - Target implementation date (if set)
- **Budget indicator** - Shows if you're over/under budget (if set)
- **Taskbar** - Access to filters, exports, approvals, and more

**Main Canvas:**
- **Org chart view** - Visual representation of your org structure
- **Position cards** - Hover to reveal action buttons
- **Reporting lines** - Solid lines for direct reports, dotted for matrix

**Right Side:**
- **Change Tracker** - Real-time cost and headcount impact
- **Details panel** - Position/employee information when selected

---

## Core Actions at a Glance

### Position Actions

**What you can do with positions:**

| Action | Purpose | When to Use |
|--------|---------|-------------|
| **Add** | Create new positions | Modeling growth, backfills, new roles |
| **Edit** | Modify position details | Update salary, title, department, etc. |
| **Move** | Change reporting relationships | Reorganizations, transfers |
| **Close** | Mark position as closed/RIF | Budget cuts, role elimination |
| **Duplicate** | Create multiple identical positions | Scaling teams quickly |
| **Delete** | Permanently remove position | Cleanup mistakes (not for real RIFs) |

**Learn more:** [Making Position Changes](making-position-changes.md)

---

### People Actions

**What you can do with employees:**

| Action | Purpose | When to Use |
|--------|---------|-------------|
| **Assign** | Attach employee to position | Filling vacancies, transfers |
| **Detach** | Remove employee from position | Departures, freeing for reassignment |
| **Move** | Transfer employee between positions | Internal mobility, promotions |
| **Move to Bench** | Remove from org chart temporarily | Holding during restructuring |

**Learn more:** [Working with People](working-with-people.md)

---

### Bulk Actions

**What you can do with multiple positions at once:**

| Action | Purpose | When to Use |
|--------|---------|-------------|
| **Select multiple** | Choose many positions | Preparing for bulk edits |
| **Bulk edit** | Update attributes across positions | Changing departments, locations |
| **Bulk move** | Reassign many positions to new manager | Large reorganizations |
| **Bulk close** | Close multiple positions at once | Significant downsizing |

**Learn more:** [Bulk Operations](bulk-operations.md)

---

## Understanding the Change Tracker

The **Change Tracker** is your constant companion when working in scenarios. It shows the real-time impact of your changes.

**What it tracks:**

**Additions (+):**
- New positions added
- Cost increase
- Headcount increase

**Closures (-):**
- Positions closed/RIF'd
- Cost savings
- Headcount reduction

**Moves (neutral):**
- Positions reassigned to different managers
- No cost or headcount change
- Organizational restructuring

**Net Impact:**
- Total headcount change (+/- X positions)
- Total cost change (+/- $X)
- Final scenario totals

**How to use it:**
1. Make a change (add, close, move)
2. Check Change Tracker immediately
3. Verify the impact matches expectations
4. Adjust if needed
5. Continue modeling

**Learn more:** [Scenario Tracking & Analysis](tracking-analysis.md)

---

## Common Workflows

### Workflow 1: Planning a Reorganization

**Goal:** Restructure a department with new reporting relationships.

**Steps:**
1. **Create scenario** - Use Partial Org focused on the department
2. **Review current state** - Understand existing structure
3. **Move positions** - Drag teams to new managers
4. **Verify structure** - Check reporting relationships
5. **Review Change Tracker** - Confirm neutral cost (moves only)
6. **Share with stakeholders** - Get feedback
7. **Submit for approval** - Route through workflow

**Learn more:** [Planning a Reorganization](../use-case-tutorials/planning-reorganization.md)

---

### Workflow 2: Modeling Headcount Growth

**Goal:** Add 15 new positions for Q2 expansion.

**Steps:**
1. **Create scenario** - Use Partial Org or Full Org depending on scope
2. **Add positions** - Create new roles under appropriate managers
3. **Use duplicate** - Quickly add multiple similar roles
4. **Set salaries** - Assign compensation for each
5. **Leave vacant** - Don't assign employees yet (model the plan)
6. **Set effective dates** - Schedule Q2 start dates
7. **Review Change Tracker** - Verify cost impact fits budget
8. **Submit for approval**

**Learn more:** [Building an Annual Hiring Plan](../use-case-tutorials/annual-hiring-plan.md)

---

### Workflow 3: Modeling Budget Cuts

**Goal:** Reduce department cost by 10%.

**Steps:**
1. **Create scenario** - Use Partial Org for affected area
2. **Identify positions** - Review roles and cost
3. **Close positions** - Use ❌ Close button, select "Layoff (RIF)"
4. **Review Change Tracker** - Check savings vs target
5. **Verify structure** - Ensure remaining org still functions
6. **Test alternatives** - Create Scenario B, C with different approaches
7. **Compare scenarios** - Choose least disruptive option
8. **Submit for approval**

**Learn more:** [Modeling Budget Cuts](../use-case-tutorials/budget-cuts.md)

---

### Workflow 4: Succession Planning

**Goal:** Model leadership transitions and test potential successors.

**Steps:**
1. **Create scenario** - "VP Engineering Succession - Candidate A"
2. **Find leadership position** - Locate role with potential transition
3. **Add backfill** - Create replacement position
4. **Assign successor** - Attach candidate to new position
5. **Review impact** - Check team structure
6. **Create alternatives** - Scenario B with different candidate
7. **Compare scenarios** - Evaluate options side-by-side
8. **Choose best option**

**Learn more:** [Succession Planning](../use-case-tutorials/succession-planning.md)

---

## Working with Time

Scenarios support **time-based planning** to model when changes will happen.

**Effective dates** let you:
- Schedule position additions for specific quarters
- Model phased hiring (5 in Q1, 3 in Q2, etc.)
- Plan reorganizations for specific implementation dates
- Track when costs will hit

**How to use:**
1. When adding/editing positions, set **Effective Date**
2. View timeline to see when changes occur
3. Track cost impact by quarter
4. Export timeline for financial planning

**Learn more:** [Time-Based Planning](time-based-planning.md)

---

## Collaboration Features

Scenarios are built for teamwork.

**Comments:**
- Add comments to positions
- @mention collaborators
- Discuss changes inline
- Track conversation history

**Sharing:**
- Share scenarios with stakeholders
- Control view vs edit access
- Present to leadership
- Export for external review

**Approval Workflows:**
- Submit scenarios for review
- Route through approval chains
- Track approval status
- Get sign-off before implementation

**Learn more:** [Scenario Collaboration](collaboration.md)

---

## Comparing Scenarios

Create multiple versions to evaluate alternatives.

**Why compare:**
- Test different reorganization approaches
- Evaluate budget cut options
- Compare succession candidates
- Choose the best path forward

**How to compare:**
1. Create Scenario A, B, C
2. Model different approaches in each
3. Use comparison view to see side-by-side
4. Compare cost, headcount, structure
5. Choose optimal scenario

**Learn more:** [Scenario Comparisons](comparisons.md)

---

## Scenario States

Scenarios move through states:

**Draft:**
- Actively being edited
- Not yet ready for review
- Full editing capability

**Submitted:**
- Sent for approval
- Limited editing (depends on settings)
- In approval workflow

**Approved:**
- Sign-off received
- Ready for implementation
- Typically locked from further edits

**Implemented:**
- Changes executed in HRIS
- Historical record
- Usually read-only

---

## Best Practices

1. **Start small** - Don't try to model everything at once
2. **Check Change Tracker frequently** - Catch unintended impacts early
3. **Name scenarios clearly** - Include date, department, purpose
4. **Create multiple versions** - Test alternatives before committing
5. **Comment liberally** - Explain your reasoning
6. **Save often** - Changes auto-save, but verify
7. **Share early** - Get feedback before finalizing
8. **Use effective dates** - Model timing, not just what changes

---

## Common Mistakes to Avoid

❌ **Making too many changes at once** - Hard to track what changed and why

❌ **Ignoring Change Tracker** - Missing cost impacts

❌ **Using Delete instead of Close** - Loses tracking for real RIFs

❌ **Not testing alternatives** - Choosing first idea without comparison

❌ **Forgetting to share** - Surprises during review

❌ **Not setting effective dates** - Losing timeline visibility

---

## Keyboard Shortcuts

Speed up your work with shortcuts:

- **Cmd/Ctrl + K** - Quick search
- **Cmd/Ctrl + Z** - Undo
- **Cmd/Ctrl + Y** - Redo
- **Cmd/Ctrl + Click** - Multi-select positions
- **Cmd/Ctrl + S** - Save (auto-saves already)

---

## Next Steps

Now that you understand the basics, explore specific actions:

**Core Actions:**
- [Making Position Changes](making-position-changes.md) - Add, edit, move, close positions
- [Working with People](working-with-people.md) - Assign, detach, transfer employees
- [Bulk Operations](bulk-operations.md) - Edit multiple positions at once

**Advanced Features:**
- [Time-Based Planning](time-based-planning.md) - Schedule changes over time
- [Scenario Tracking & Analysis](tracking-analysis.md) - Deep dive into Change Tracker
- [Scenario Comparisons](comparisons.md) - Evaluate multiple options
- [Scenario Approvals](approvals.md) - Submit for stakeholder review

**Practical Tutorials:**
- [Planning a Reorganization](../use-case-tutorials/planning-reorganization.md)
- [Building an Annual Hiring Plan](../use-case-tutorials/annual-hiring-plan.md)
- [Modeling Budget Cuts](../use-case-tutorials/budget-cuts.md)
- [Succession Planning](../use-case-tutorials/succession-planning.md)



