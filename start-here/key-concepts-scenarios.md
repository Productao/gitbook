---
description: Essential concepts for working with scenarios
hidden: false
---

# Key Concepts for Scenarios

Scenarios are where you model "what-if" changes to your organization. Understanding these concepts will help you plan reorganizations, hiring plans, budget cuts, and other workforce changes effectively.

---

## What is a Scenario?

A **scenario** is an editable copy of your Main Org where you can model future changes without affecting the current state.

**Think of scenarios as:**
- Sandboxes for experimentation
- Draft versions of future org states
- Planning workspaces for workforce changes

**Example workflow:**
1. Start with Main Org (500 employees, $50M cost)
2. Create Scenario "2026 Q2 Reorg"
3. Add 20 positions, close 10 positions, reassign 5 managers
4. Review cost impact (+$2M)
5. Submit for approval
6. Implement approved changes

---

## Change Types

When you modify scenarios, Agentnoon tracks changes and categorizes them:

### Addition (New Position)
- Creating a brand new position
- Increases headcount and cost
- Shows as **green** in Change Tracker

### Reduction (Position Closure)
- Closing an existing position
- Decreases headcount and cost
- Types: Layoff (RIF), Exit, Elimination
- Shows as **red** in Change Tracker

### Modification (Position Edit)
- Changing attributes of existing position
- Examples: title change, salary adjustment, department transfer, manager reassignment
- May increase or decrease cost
- Shows as **blue** in Change Tracker

### No Change
- Position exists in both Main Org and Scenario
- No attributes modified
- Shows as white/default in views

> **[Screenshot placeholder: Scenario showing positions with different change types - additions in green, reductions in red, modifications in blue]**

---

## Before, After, and Changes Views

Scenarios have three view modes to help you understand impact:

### Show Before
Displays the **Main Org** (current reality, before any scenario changes).

**When to use:**
- Establish your baseline
- See current state
- Compare against proposed changes

### Show After
Displays **all scenario changes applied** (proposed future state).

**When to use:**
- See the full impact of your changes
- View final state after modifications
- Validate your scenario's end result

### Show Changes
Displays the **delta** between Before and After (increases/decreases).

**When to use:**
- Highlight exactly what's changing
- Show departmental gains (+) and losses (-)
- Communicate impact to stakeholders

> **[Screenshot placeholder: Toggle showing Show Before, Show After, Show Changes options]**

---

## The Bench

The "bench" is a special holding area for employees who are detached from positions but still in your organization.

**When to use the bench:**
- Planning internal transfers (move employee to bench, then assign to new position)
- Modeling RIFs where employee leaves but position stays open
- Temporary holding during reorganizations

**How it works:**
1. Detach employee from Position A → employee moves to bench
2. Position A is now open
3. Assign employee to Position B → employee leaves bench
4. Position B is now filled

**Important:** The bench is for planning only. In real implementation, employees transition directly.

---

## Effective Dates

The date when a planned change takes effect.

**Use cases:**
- Stagger hires across quarters (Q1: 10 positions, Q2: 15 positions)
- Model multi-phase reorganizations
- Plan budget changes by fiscal period

**How it works:**
- Each position change can have a different effective date
- Forecast view shows when changes take effect
- Allows time-phased planning

**Example scenario:**
- Jan 15, 2026: Close 20 positions (RIF)
- Apr 1, 2026: Add 10 positions (new hiring)
- Jul 1, 2026: Promote 5 managers (structure change)

**Learn more:** [Time-Based Planning](../scenarios/time-based-planning.md)

---

## Change Tracker

Real-time panel showing the impact of all changes in a scenario.

**What it tracks:**
- Headcount changes (additions, reductions)
- Cost impact (total dollar change)
- Department-by-department breakdown
- Before/after comparisons

**Use Change Tracker to:**
- Validate you're hitting budget targets
- Understand net headcount change
- Review department-specific impact
- Communicate financial effect

**Example readout:**
- +20 additions ($2.5M)
- -15 reductions (-$1.8M)
- +5 net headcount
- +$700K total cost impact

> **[Screenshot placeholder: Change Tracker panel showing headcount and cost impact summary]**

---

## Scenario Approvals

Workflow process for reviewing and signing off on scenario changes.

**Typical approval flow:**
1. Planner creates scenario
2. Submit for review
3. Manager/VP approves (Level 0/1)
4. Finance approves (Level 2)
5. Final sign-off (Level 3)
6. HRBP/Admin implements

**Approval states:**
- **Draft** (editable)
- **Pending Approval** (locked)
- **Approved** (locked)
- **Rejected** (editable)

**Important:** Once approved, scenarios typically lock to preserve the approved state.

**Learn more:** [Scenario Approvals](../scenarios/approvals.md)

---

## Scenario Views: Directory, Forecast, Workforce Hub

Scenarios can be viewed in three different modules:

### Directory View
Table view of all positions for bulk analysis and editing.

**Best for:**
- Making multiple position changes
- Filtering and bulk operations
- Reviewing change lists

### Forecast View
Time-phased projections showing when changes take effect.

**Best for:**
- Understanding timing of changes
- Viewing headcount/cost by quarter
- Multi-year planning

**Learn more:** [Scenario Forecast](../scenarios/scenario-forecast.md)

### Workforce Hub View
Analytics and charts for org structure analysis.

**Best for:**
- Analyzing span of control
- Visualizing headcount distribution
- Validating org health

**Learn more:** [Scenario Workforce Hub](../scenarios/scenario-workforce-hub.md)

---

## Projects (Optional Feature)

Group related scenarios together for larger initiatives.

**Example project:** "2026 Company-Wide Restructuring"
- Scenario 1: Engineering Reorg
- Scenario 2: Sales Team Consolidation
- Scenario 3: G&A Cost Reduction

**Use projects when:**
- Multiple teams are planning changes simultaneously
- You want to track overall impact across related scenarios
- Cross-functional initiative requires coordination

---

## Tags & Symbols

### Tags
Labels you can apply to scenarios for organization and filtering.

**Common tags:**
- "Q1 2026"
- "Budget Cut"
- "Hiring Plan"
- "High Priority"
- "Draft"

**How to use tags:**
- Organize scenarios by quarter or initiative
- Filter scenario lists
- Quickly identify scenario purpose

### Symbols
Visual indicators for quick scenario identification.

**Common symbols:**
- ⚡ High Priority
- 💰 Budget-Related
- 👥 Hiring Plan
- ❌ RIF/Layoff
- 🔄 Reorganization
- ✅ Approved
- 🚧 Work in Progress

> **[Screenshot placeholder: Scenario list showing scenarios with various tags and symbols]**

---

## Collaboration Features

### Real-Time Co-Editing
Multiple users can edit scenarios simultaneously with live updates.

### Comments & @Mentions
- Add comments to positions or scenarios
- Tag colleagues with @mention for notifications
- Threaded discussions for context

### Sharing
- Share scenarios with specific users or groups
- Control edit vs view permissions
- Collaborate across departments

**Learn more:** [Scenario Collaboration](../scenarios/collaboration.md)

---

## Scenario Comparisons

Compare multiple scenarios side-by-side to evaluate different approaches.

**What you can compare:**
- Headcount changes between scenarios
- Cost impact differences
- Different organizational structures
- Alternative timing approaches

**Use scenario comparisons to:**
- Evaluate multiple reorganization options
- Choose between budget cut approaches
- Present alternatives to leadership

**Learn more:** [Scenario Comparisons](../scenarios/comparisons.md)

---

## Scenario Refresh (Advanced)

Update scenarios with latest Main Org data while preserving your changes.

**When to use:**
- Main Org data has changed significantly since scenario creation
- You want to rebase your changes on current reality
- New employees joined who should be included in your scenario

**Important:** Scenario refresh is an advanced feature. Scenarios are snapshots and don't automatically update when Main Org changes.

**Learn more:** [Scenario Refresh](../scenarios/refresh.md)

---

## Next Steps

Now that you understand scenario concepts:

- **Create your first scenario:** [Creating Scenarios](../scenarios/creating-scenarios.md)
- **Learn scenario operations:** [Making Position Changes](../scenarios/making-position-changes.md)
- **Explore use cases:** [Planning a Reorganization](../use-case-tutorials/planning-reorganization.md)
- **Master time-based planning:** [Time-Based Planning](../scenarios/time-based-planning.md)

**Related concepts:**
- [Key Concepts](concepts.md) - Core Agentnoon concepts
- [Key Concepts for Main Org](key-concepts-main-org.md) - Main Org specific concepts
- [Scenarios Fundamentals](scenarios-fundamentals.md) - Deep dive on scenarios
