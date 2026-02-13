---
description: Monitoring scenario impact and changes
icon: chart-mixed
hidden: false
---

# Scenario Tracking & Analysis

As you make changes in scenarios, Agentnoon automatically tracks every modification and shows you the real-time impact. This guide covers the Change Tracker, before-and-after analysis, and how to use analytics to understand your scenario's effects.

## The Change Tracker

The **Change Tracker** is your constant companion when working in scenarios. It's always visible in the right panel, showing real-time cost and headcount impact of every change you make.

### What the Change Tracker Shows

**Three categories of changes:**

1. **Additions (+)** - New positions added
   - Position details (title, department, salary)
   - Cost increase
   - Headcount increase
   - Effective date (if set)

2. **Reductions (-)** - Positions closed/eliminated
   - Position details
   - Cost savings
   - Headcount reduction
   - Closure reason (RIF, Exit, etc.)

3. **Modifications (~)** - Positions changed but not added/removed
   - What changed (title, salary, department, manager, etc.)
   - Before vs After values
   - Cost impact of changes (if salary changed)

**Summary section (bottom):**
- **Net headcount change** (+/- X positions)
- **Net cost impact** (+/- $X)
- **Total scenario cost** (baseline + changes)
- **Budget status** (if budget was set)

---

### Accessing the Change Tracker

**Location:** Right side panel when in a scenario

**How to open/close:**
1. Change Tracker is **open by default** when you enter a scenario
2. Click **👀 icon** in top-right to toggle visibility
3. Panel slides in/out without losing data

**Always visible:** Even when collapsed, you see summary metrics in the taskbar.

---

### Understanding Change Tracker Entries

#### Addition Entry Example

```
➕ Software Engineer
Department: Engineering
Location: San Francisco
Salary: $150,000
Effective Date: Q2 2026
Cost Impact: +$150,000
Headcount Impact: +1
```

**What this tells you:**
- New position added
- All key attributes
- When it takes effect
- Exact cost and headcount impact

---

#### Reduction Entry Example

```
➖ Account Manager
Department: Sales
Reason: Layoff (RIF)
Salary: $120,000
Effective Date: Q1 2026
Cost Impact: -$120,000
Headcount Impact: -1
```

**What this tells you:**
- Position being eliminated
- Why it's closing (RIF vs voluntary exit)
- Cost savings
- When savings start

---

#### Modification Entry Example

```
~ Marketing Manager
Changes:
  • Job Title: Marketing Coordinator → Marketing Manager
  • Salary: $80,000 → $95,000
  • Department: Marketing → Growth
Cost Impact: +$15,000
Headcount Impact: 0
```

**What this tells you:**
- Position modified (not added or removed)
- What specifically changed (before → after)
- Cost impact of changes
- No headcount impact (same person, different attributes)

---

### Using the Change Tracker Effectively

#### Check After Every Change

**Best practice:** Look at Change Tracker immediately after making any change.

**Workflow:**
1. Make a change (add position, close position, edit salary)
2. Look at Change Tracker
3. Verify impact matches expectations
4. If unexpected, undo or adjust
5. Continue modeling

**Example:**
- You close 5 positions expecting $500K savings
- Change Tracker shows $450K savings
- Review: One position had lower salary than expected
- Adjust plan accordingly

---

#### Filter by Change Type

**How to filter:**
1. In Change Tracker panel, click **filter icon**
2. Select which changes to view:
   - **Additions only**
   - **Reductions only**
   - **Modifications only**
   - **All changes** (default)

**When to use:**
- **Additions only** - Review all new positions and total hiring cost
- **Reductions only** - Review all cuts and total savings
- **Modifications only** - See what attributes changed without adds/removes

---

#### Sort by Cost Impact

**How to sort:**
1. Click **column headers** in Change Tracker
2. Sort by:
   - Cost impact (highest to lowest)
   - Headcount impact
   - Effective date
   - Department
   - Alphabetically

**When to use:**
- Find highest-cost additions
- Identify biggest savings opportunities
- Review changes by timing

---

#### Export Change Log

**How to export:**
1. In Change Tracker panel, click **Export** button
2. Choose format:
   - **CSV** - For analysis in Excel
   - **PDF** - For presentation/documentation
3. Select date range (if applicable)
4. Click **Export**

**What gets exported:**
- All changes (additions, reductions, modifications)
- Cost and headcount impact
- Position details
- Effective dates
- Summary totals

**When to use:**
- Documenting scenario for stakeholders
- Creating detailed budget impact report
- Comparing scenario changes offline
- Archiving scenario decisions

---

### Budget Tracking

If you set a **budget** when creating the scenario, the Change Tracker shows how you're tracking against it.

**Budget status display:**
- **Target budget:** $5,000,000
- **Current total:** $4,750,000
- **Remaining:** $250,000 under budget ✅

**Or:**
- **Target budget:** $5,000,000
- **Current total:** $5,200,000
- **Over budget:** $200,000 ⚠️

**Visual indicator:**
- Green = Under budget
- Yellow = Close to budget
- Red = Over budget

**How to use:**
1. Set budget when creating scenario
2. Make changes
3. Monitor budget status in Change Tracker
4. Adjust adds/reductions to stay within budget
5. Final check before submitting for approval

---

## Before-and-After Analysis

Beyond the Change Tracker, Agentnoon provides deeper analytical views to understand scenario impact.

### Accessing Workforce Hub in Scenarios

**How to access:**
1. Open a scenario
2. Click **Org Chart dropdown** in taskbar
3. Select **Workforce Hub**
4. Hub opens with before-and-after views

**What's different from Main Org Hub:**
- All charts show **before-and-after comparison**
- "Before" = Main Org baseline
- "After" = Your scenario changes
- Side-by-side visualization

---

### Before-and-After Charts

#### Headcount Comparison

**What it shows:**
- Headcount before scenario (Main Org)
- Headcount after your changes (Scenario)
- Breakdown by department, location, or other attributes

**Example:**
```
Before: 800 employees
After: 825 employees
Change: +25 employees (+3.1%)

By Department:
  Engineering: 300 → 320 (+20)
  Sales: 200 → 200 (0)
  Marketing: 150 → 155 (+5)
  ...
```

**When to use:**
- Verify headcount targets
- See where growth/reduction is happening
- Present hiring/RIF impact by area

---

#### Cost Comparison

**What it shows:**
- Total compensation cost before
- Total compensation cost after
- Breakdown by department or other dimensions

**Example:**
```
Before: $80M annual cost
After: $82.5M annual cost
Change: +$2.5M (+3.1%)

By Department:
  Engineering: $35M → $37M (+$2M)
  Sales: $22M → $22M ($0)
  Marketing: $12M → $12.5M (+$500K)
  ...
```

**When to use:**
- Budget impact analysis
- Verify cost targets
- Understand cost distribution changes

---

#### Span of Control Comparison

**What it shows:**
- Average span of control before
- Average span of control after
- Distribution of manager team sizes

**Example:**
```
Average Span Before: 6.2 reports per manager
Average Span After: 7.1 reports per manager
Change: +0.9 reports per manager

Managers with large teams:
  Before: 12 managers with >10 reports
  After: 18 managers with >10 reports
```

**When to use:**
- Verify reorganization didn't create span issues
- Flatten organization intentionally
- Identify managers who need support

**Learn more:** [Span of Control Analysis](../use-case-tutorials/span-of-control-analysis.md)

---

#### Layers Comparison

**What it shows:**
- Number of management layers before
- Number of management layers after
- Distribution of employees by layer

**Example:**
```
Layers Before: 6 layers (CEO to IC)
Layers After: 5 layers (CEO to IC)
Change: -1 layer (flattened)

Distribution:
  Layer 1 (CEO): 1 → 1
  Layer 2 (VPs): 8 → 8
  Layer 3 (Directors): 25 → 20
  Layer 4 (Managers): 80 → 95
  Layer 5 (ICs): 686 → 701
```

**When to use:**
- Verify flattening initiatives
- Understand organizational complexity
- Evaluate depth vs flatness tradeoffs

---

#### Custom Metric Comparisons

**What it shows:**
- Any custom metrics configured by your admin
- Before vs after values
- Breakdowns by dimensions

**Examples:**
- Diversity metrics (% women, % underrepresented minorities)
- Average tenure
- Cost per employee
- Ratio of managers to ICs

---

### Customizing Before-and-After Views

#### Toggle Between Views

**Options:**
1. **Before and After** (side-by-side) - Default
2. **Before only** - Show Main Org baseline
3. **After only** - Show scenario final state

**How to toggle:**
1. In Workforce Hub, look for **dropdown** in chart
2. Select view preference
3. Chart updates

**When to use each:**
- **Side-by-side** - Compare and see change clearly
- **Before only** - Remind yourself of starting point
- **After only** - Focus on final state without comparison

---

#### Filter and Drill Down

**How to filter:**
1. In Workforce Hub charts, use **filter controls**
2. Filter by:
   - Department
   - Location
   - Job Family
   - Pay Grade
   - Any custom dimensions
3. Before-and-after view updates to filtered subset

**Example use case:**
- Filter to "Engineering" department
- See headcount before/after for just Engineering
- Verify Engineering grew by 20 as planned

---

## Common Analysis Workflows

### Workflow 1: Verify Budget Cut Hit Targets

**Goal:** Confirm $2M savings achieved.

**Steps:**
1. Complete budget cut scenario (close positions)
2. Open **Change Tracker**
3. Filter to **Reductions only**
4. Look at **Net cost impact** at bottom
5. Verify shows "-$2,000,000" or close
6. If not, add more reductions or adjust
7. Export change log for documentation

**Result:** Verified budget cut meets target.

---

### Workflow 2: Analyze Reorganization Impact

**Goal:** Ensure reorganization didn't unintentionally increase cost.

**Steps:**
1. Complete reorganization (move positions, change managers)
2. Open **Change Tracker**
3. Check **Net cost impact** = $0 (moves are neutral)
4. If cost changed, review **Modifications** for salary changes
5. Open **Workforce Hub**
6. View **Span of Control** before-and-after
7. Verify no managers with excessive spans
8. View **Layers** before-and-after
9. Confirm layers match intent (flatten vs maintain)

**Result:** Reorganization verified as cost-neutral with healthy structure.

---

### Workflow 3: Present Hiring Plan Impact

**Goal:** Show leadership the effect of Q2 hiring plan.

**Steps:**
1. Complete hiring plan scenario (add 50 positions)
2. Open **Change Tracker**
3. Filter to **Additions only**
4. Export to PDF
5. Open **Workforce Hub**
6. View **Headcount** before-and-after by department
7. Screenshot comparisons
8. View **Cost** before-and-after
9. Screenshot cost impact
10. Compile into presentation

**Result:** Data-driven presentation of hiring plan.

---

### Workflow 4: Monitor Scenario as You Build

**Goal:** Keep track of changes while actively modeling.

**Steps:**
1. Open scenario
2. Keep **Change Tracker visible** (don't close it)
3. Make first change (add a position)
4. Glance at Change Tracker (verify +1 headcount, +$X cost)
5. Make second change (close a position)
6. Glance at Change Tracker (verify net impact)
7. Continue making changes
8. Periodically check **Net impact** summary
9. Ensure tracking toward goal (e.g., net neutral cost)

**Result:** Continuous awareness of scenario impact.

---

## Best Practices

1. **Keep Change Tracker open** - Always visible for instant feedback
2. **Check after every change** - Catch mistakes immediately
3. **Use filters** - Focus on specific change types
4. **Export regularly** - Document progress
5. **Leverage Workforce Hub** - Deep-dive into specific metrics
6. **Compare before deciding** - Use before-and-after to evaluate tradeoffs
7. **Set budgets upfront** - Track against targets from the start
8. **Review before submitting** - Final check before approval workflow

---

## Common Mistakes to Avoid

❌ **Ignoring Change Tracker** - Making changes blindly without checking impact

❌ **Not setting a budget** - Missing target tracking capability

❌ **Only checking cost** - Forgetting to review headcount, structure, span of control

❌ **Not exporting change log** - Losing documentation of what changed

❌ **Forgetting effective dates** - Cost timing is important for budget planning

❌ **Not using Workforce Hub** - Missing deeper analytical insights

---

## Troubleshooting

**Problem:** Change Tracker shows unexpected cost impact.
- **Solution:** Review modifications list. Salary or other cost fields may have changed unintentionally.

**Problem:** Headcount doesn't match expected.
- **Solution:** Check for positions marked as closed vs deleted. Closed positions still count as reductions.

**Problem:** Can't find a specific change in Change Tracker.
- **Solution:** Use filter or sort. Or check modification vs addition/reduction category.

**Problem:** Before-and-after charts look the same.
- **Solution:** Ensure you're in a scenario (not Main Org). Verify changes were saved.

**Problem:** Budget status not showing.
- **Solution:** You need to set a budget when creating the scenario. Edit scenario settings to add budget.

**Problem:** Can't export Change Tracker.
- **Solution:** Check permissions. Export may be restricted by admin.

---

## Next Steps

Now that you understand tracking and analysis:
- Use Change Tracker actively while building your next scenario
- Explore Workforce Hub before-and-after views for deeper insights
- Export change logs to document your scenario decisions
- Practice [Scenario Comparisons](comparisons.md) to evaluate multiple options with data
- Learn [Time-Based Planning](time-based-planning.md) to track when changes happen



