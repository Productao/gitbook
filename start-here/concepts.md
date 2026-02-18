---
description: Essential concepts and terminology for understanding Agentnoon
hidden: false
---

# Key Concepts

Understanding these core concepts will help you navigate Agentnoon more effectively and make the most of its workforce planning capabilities.

---

## Positions vs People

**Position:** A job role in your organization, whether filled or open. Positions have attributes like title, department, salary range, and reporting structure.

**Person/Employee:** The individual assigned to a position. One person can only fill one position at a time.

**Key insight:** Agentnoon is primarily position-based. You plan with positions first, then assign people to them. This allows you to model future org structures even before hiring.

**Example:**
- Position: "Senior Software Engineer, Platform Team"
- Person: Jane Smith (assigned to this position)

> **[Screenshot placeholder: Position card showing open position vs filled position with employee]**

---

## Main Org vs Scenarios

### Main Org

Your **current state** organization as it exists today. This is the source of truth imported from your HRIS or data file.

**Characteristics:**
- View-only (read-only)
- Reflects real-time data
- Updated via data imports
- Cannot be edited directly

**Use Main Org to:**
- Understand current structure
- Analyze existing metrics (span of control, cost)
- Export current state data
- Reference as baseline for scenarios

### Scenarios

**Future state** versions of your organization where you model changes. Think of scenarios as sandboxes where you can experiment with org design.

**Characteristics:**
- Editable copies of Main Org
- Support "what-if" planning
- Track all changes with Change Tracker
- Can be compared, shared, and approved

**Use Scenarios to:**
- Plan reorganizations
- Model budget cuts or hiring plans
- Test different org structures
- Build annual headcount forecasts
- Plan RIFs or internal transfers

**Example workflow:**
1. Start with Main Org (500 employees, $50M cost)
2. Create Scenario "2026 Q2 Reorg"
3. Add 20 positions, close 10 positions, reassign 5 managers
4. Review cost impact (+$2M)
5. Submit for approval

---

## Org Chart vs Directory

### Org Chart View

Visual, hierarchical tree showing reporting relationships.

**Best for:**
- Understanding reporting structure
- Visualizing management chains
- Presenting to stakeholders
- Dragging positions to new managers

### Directory View

Table/spreadsheet view of all positions with sortable columns.

**Best for:**
- Analyzing data in bulk
- Filtering and exporting
- Reviewing change lists
- Bulk selection and editing

**Pro tip:** Use both views. Switch between them with keyboard shortcuts (3 for Org Chart, 5 for Directory).

> **[Screenshot placeholder: Side-by-side comparison of Org Chart view vs Directory view]**

---

## Change Types

When you modify scenarios, Agentnoon tracks changes and categorizes them:

### Addition (New Position)
- Creating a brand new position
- Increases headcount and cost
- Shows as green in Change Tracker

### Reduction (Position Closure)
- Closing an existing position
- Decreases headcount and cost
- Types: Layoff (RIF), Exit, Elimination
- Shows as red in Change Tracker

### Modification (Position Edit)
- Changing attributes of existing position
- Examples: title change, salary adjustment, department transfer, manager reassignment
- May increase or decrease cost
- Shows as blue in Change Tracker

### No Change
- Position exists in both Main Org and Scenario
- No attributes modified
- Shows as white/default in views

---


> **[Screenshot placeholder: Scenario showing positions with different change types - additions in green, reductions in red, modifications in blue]**

## The Bench

The "bench" is a special holding area for employees who are detached from positions but still in your organization.

**When to use the bench:**
- Planning internal transfers (move employee to bench, then assign to new position)
- Modeling RIFs where employee leaves but position stays open
- Temporary holding during reorganizations

**How it works:**
1. Detach employee from Position A (employee moves to bench)
2. Position A is now open
3. Assign employee to Position B (employee leaves bench)
4. Position B is now filled

**Important:** The bench is for planning only. In real implementation, employees won't literally sit on a bench—they transition directly.

---

## Span of Control (SOC)

The number of direct reports a manager has.

**Healthy ranges (industry standard):**
- Individual Contributors: 0 direct reports
- First-Line Managers: 5-10 direct reports
- Mid-Level Managers: 5-8 direct reports
- Executives: 5-10 direct reports

**Why it matters:**
- Too few direct reports: Management overhead too high, unnecessary layers
- Too many direct reports: Manager can't provide adequate support

**How Agentnoon helps:**
- Visualizes SOC in org chart with color coding
- Flags managers with unhealthy SOC
- Scenario planning can test SOC improvements

---


> **[Screenshot placeholder: Org chart with span of control highlighting - color-coded managers by SOC health]**

## Layers

The number of management levels between an employee and the CEO.

**Example:**
- CEO: Layer 0
- VP reporting to CEO: Layer 1
- Director reporting to VP: Layer 2
- Manager reporting to Director: Layer 3
- Individual Contributor: Layer 4

**Why it matters:**
- More layers = slower decision-making
- Fewer layers = flatter, more agile organization
- Industry best practice: 4-7 layers for most companies

---

## Effective Dates

The date when a planned change takes effect.

**Use cases:**
- Stagger hires across quarters (Q1: 10 positions, Q2: 15 positions)
- Model multi-phase reorganizations
- Plan budget changes by fiscal period

**How it works:**
- Each position change can have a different effective date
- Change Tracker shows timeline view
- Reports can filter by date range

**Example scenario:**
- Jan 15, 2026: Close 20 positions (RIF)
- Apr 1, 2026: Add 10 positions (new hiring)
- Jul 1, 2026: Promote 5 managers (structure change)

---

## Attributes vs Fields

### Attributes
Data points about positions or people (e.g., Department, Location, Salary, Title).

**System attributes** (calculated by Agentnoon):
- Span of Control
- Layer
- Total Org Size
- Cost Impact

**Custom attributes** (defined by your admin):
- Business Unit
- Cost Center
- Employee Type
- Pay Grade

### Fields
How attributes are organized and displayed in the UI (e.g., which attributes appear on cards, which are required).

**Admins control:**
- Which fields are visible
- Which are required vs optional
- Field groupings on cards

---

## Cards

Visual containers displaying position or employee information.

**What's on a card:**
- Name
- Title
- Department
- Salary
- Direct reports count
- Other configured attributes

**Card interactions:**
- Click to open detail panel
- Hover to see quick info
- Drag to move to new manager (in scenarios)
- Color-coded by change type

---


> **[Screenshot placeholder: Example position card showing name, title, department, salary, and other attributes]**

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

---

## Forecast vs Scenarios

Both are planning tools, but serve different purposes:

### Scenarios
- Structural changes to org design
- Best for: Reorganizations, RIFs, major shifts
- Focus: Positions and reporting structure
- Visual: Org chart and directory views

### Forecast
- Headcount and budget projections over time
- Best for: Annual planning, multi-year roadmaps
- Focus: Aggregate numbers by department/quarter
- Visual: Spreadsheet-style interface

**When to use each:**
- **Scenario:** "We're reorganizing the Sales team under a new VP"
- **Forecast:** "We plan to grow Engineering from 50 to 75 people over the next year"

---

## Approvals

Workflow process for reviewing and signing off on scenario changes.

**Typical approval flow:**
1. Planner creates scenario
2. Submit for review
3. Manager/VP approves
4. Finance approves
5. HRBP/Admin implements

**Approval states:**
- Draft (editable)
- Pending Approval (locked)
- Approved (locked)
- Rejected (editable)

**Important:** Once approved, scenarios typically lock to preserve the approved state.

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

## Tags

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

---

## Symbols (Visual Indicators)

Scenarios can display symbols for quick identification:

**Common symbols:**
- ⚡ High Priority
- 💰 Budget-Related
- 👥 Hiring Plan
- ❌ RIF/Layoff
- 🔄 Reorganization
- ✅ Approved
- 🚧 Work in Progress
- 🎯 Annual Plan

**How symbols help:**
- Quick visual scanning of scenario lists
- Communicate scenario purpose at a glance
- Team alignment on priorities

---

## Collaboration Features

### Real-Time Editing
Multiple users can edit scenarios simultaneously with live updates.

### Comments & @Mentions
- Add comments to positions or scenarios
- Tag colleagues with @mention
- Threaded discussions for context

### Sharing
- Share scenarios with specific users or groups
- Control edit vs view permissions
- Collaborate across departments

---

## Permissions & Access Control

### Access Groups
Define who can see what data based on department, location, or custom rules.

**Example access groups:**
- "Engineering Leadership" sees only Engineering org
- "Finance Team" sees all departments
- "HRBP North America" sees only US/Canada positions

### Permission Levels
- **Viewer:** Can see data, cannot edit
- **Planner:** Can create and edit scenarios
- **Approver:** Can approve scenario changes
- **Admin:** Full system access, can configure settings

---

## Data Sync & Refresh

### Initial Import
Load your current org data from HRIS (Workday, BambooHR, etc.) or CSV.

### Regular Sync
Keep Main Org up-to-date with scheduled or manual refreshes.

### Scenario Refresh (Advanced)
Update scenarios with latest Main Org data while preserving your changes.

**Important:** Scenarios are snapshots. They don't automatically update when Main Org changes.

---

## Next Steps

Now that you understand key concepts:

- **Explore Main Org:** View your current organization
- **Create your first scenario:** Model a simple change
- **Try both views:** Switch between Org Chart and Directory
- **Review a use case tutorial:** See concepts in action

**Learn more:**
- [Parts of the Application](parts-of-application.md) - How modules work together
- [Scenarios Fundamentals](scenarios-fundamentals.md) - Deep dive on scenario planning
- [Fields and Attributes](fields-and-attributes.md) - Understanding your data
