---
description: End-to-end reorganization workflow
hidden: false
---

# Planning a Reorganization

Reorganizations are complex initiatives that require careful analysis, stakeholder alignment, and clear communication. This comprehensive tutorial walks you through planning and executing a reorganization using Agentnoon, from initial analysis to stakeholder approval.

## When to Use Agentnoon for Reorganizations

Agentnoon is ideal for planning reorganizations when you need to:

- **Flatten organizational hierarchies** to reduce layers and improve decision-making speed
- **Add management layers** to support growing teams and reduce manager overload
- **Combine or split teams** to align with strategic priorities
- **Optimize span of control** across the organization
- **Centralize or decentralize functions** (moving teams between departments)
- **Restructure leadership** after acquisitions, mergers, or strategic pivots
- **Analyze cost and headcount impact** before implementing changes

By modeling reorganizations in Agentnoon, you can visualize the new structure, identify unintended consequences, and get stakeholder buy-in before making real-world changes.

## Common Reorganization Patterns

### Flattening the Hierarchy

**When to use:** Too many management layers create bureaucracy and slow decision-making.

**What it looks like:** Remove middle management layers by having ICs or managers report directly to more senior leaders.

**Example:** A VP currently has 2 Senior Directors, each with 3 Directors, each with teams. After flattening, the VP has 6 Directors reporting directly, eliminating the Senior Director layer.

**Considerations:**
- Increased span of control for senior leaders
- May reduce manager-level headcount and cost
- Can improve communication speed but may reduce attention for direct reports

### Adding Management Layers

**When to use:** Managers are overburdened with too many direct reports (span of control too high).

**What it looks like:** Insert a new management layer between existing managers and their teams.

**Example:** A Director has 18 direct reports. After restructuring, add 2 Senior Managers who each manage 9 people, and both report to the Director.

**Considerations:**
- Reduces span of control to manageable levels
- Adds management cost
- May slow decision-making if not implemented thoughtfully

### Combining Teams

**When to use:** Multiple small teams have overlapping functions or too few people to be effective independently.

**What it looks like:** Merge 2-3 teams under a single manager, eliminating redundant management positions.

**Example:** Three regional sales teams with 4 people each (12 total) are combined into one team with 12 people under a single manager.

**Considerations:**
- Reduces management overhead
- May lose specialized regional knowledge
- Manager needs skills to handle larger, more diverse team

### Span of Control Optimization

**When to use:** Organization has inconsistent manager workloads—some with 2 direct reports, others with 25.

**What it looks like:** Rebalance teams to achieve consistent span of control (typically 5-9 for most roles).

**Example:** Manager A has 2 direct reports, Manager B has 15. After rebalancing, both managers have 8-9 direct reports.

**Considerations:**
- Creates more equitable workloads
- May require moving people between teams
- Can surface managers who are underutilized or at risk of burnout

## Step-by-Step Reorganization Workflow

### Step 1: Analyze Current Organizational Structure

Before making changes, understand the current state and identify specific problems to solve.

#### Use Span of Control Analysis

1. Navigate to **Workforce Hub** from the homepage
2. Open the **Layers and Spans of Control** chart
3. Click the **settings gear** icon to configure SOC groupings:
   - 0-0 (Individual Contributors)
   - 1-2 (Low span)
   - 3-9 (Optimal range)
   - 10-15 (High span)
   - 16+ (Very high span)
4. Analyze the distribution:
   - Are there many managers with 1-2 direct reports? (Potential compression or inefficiency)
   - Are there managers with 16+ reports? (Potential burnout risk)
   - What layers have the most concentration of low-span managers?

> **[Screenshot placeholder: Layers and Spans of Control chart showing SOC distribution with many 1-2 span managers highlighted in layers 5 and 6]**

#### Drill Down with Spotlight

1. Go to **Main Org** from the homepage
2. Click **Spotlight** in the toolbar
3. Select **Average Immediate SOC** or **Direct Span of Control**
4. Set the range (e.g., 1-2 for low span managers)
5. Click **Apply** to highlight all matching positions

Now you can visually navigate the org chart and see exactly where problematic patterns exist.

> **[Screenshot placeholder: Org chart with Spotlight highlighting managers with 1-2 direct reports in red/orange]**

#### Identify Specific Issues

As you explore, document:
- **Compression points:** Managers reporting to managers with similar titles or levels
- **Long reporting chains:** Teams with 8+ layers between CEO and frontline employees
- **Unbalanced workloads:** Adjacent managers with vastly different team sizes
- **Isolated roles:** VPs or Directors with only 1 direct report

**Real-world example:** You discover a VP of Skin Health & Beauty has only 1 direct report (a VP of APAC), who has 8 direct reports. This is a compression point worth addressing.

### Step 2: Define Reorganization Goals

Based on your analysis, set clear objectives. Examples:

- "Reduce management layers from 8 to 6 in the Commercial organization"
- "Eliminate all 1-to-1 reporting relationships at VP level and above"
- "Balance span of control to 5-9 direct reports for all directors"
- "Consolidate 4 small regional teams into 2 larger cross-regional teams"

Clear goals help you measure success and explain changes to stakeholders.

### Step 3: Create a Reorganization Scenario

Now you'll model your proposed changes in a safe sandbox environment.

#### Create a Partial Org Scenario

1. From the homepage, click **New Scenario**
2. Select **Partial Org** (faster and more focused than Full Org)
3. Choose the organizational scope (e.g., "Commercial NA" or "Growth")
4. Name your scenario clearly: **"Commercial NA Q1 2026 Reorg"**
5. Click **Next** to create the scenario

> **[Screenshot placeholder: New Scenario modal with Partial Org selected, name field showing "Commercial NA Q1 2026 Reorg", and team selector showing Commercial NA highlighted]**

**Why Partial Org?** It's faster to work with, easier to share with specific stakeholders, and focuses attention on the area being reorganized.

#### Orient Yourself in the Scenario

Once created:
- The org chart shows the current structure (this is your "before" state)
- You can now make edits (unlike the view-only Main Org)
- All your previous filters and highlights are preserved
- The OpEx Panel on the right shows your changes as you make them

### Step 4: Model Organizational Changes

Now implement your reorganization using Agentnoon's editing tools.

#### Moving Individual Positions

**Use case:** Moving a VP to report to a different executive

1. Hover over the position you want to move
2. Click the **three dots** or right-click the card
3. Select **Change Manager**
4. Search for and select the new manager
5. The position immediately moves in the org chart

Alternatively, use **drag-and-drop:**
1. Click and hold the position card
2. Drag it to the new manager's card
3. Release to complete the move

> **[Screenshot placeholder: Org chart showing a position card being dragged from one manager to another with a dotted line indicating the move]**

#### Moving Entire Teams

**Use case:** Moving a 12-person team from one department to another

1. Hover over the team lead position
2. Click **Select Team** (this selects the lead plus all subordinates)
3. With the team selected, click **Change Manager**
4. Select the new manager
5. All selected positions move together

**Pro tip:** Press the **X key** on your keyboard while hovering over a card to quickly select just that card (not the whole team).

> **[Screenshot placeholder: Org chart with multiple cards highlighted in blue showing a selected team, with the Change Manager dialog open]**

#### Eliminating Management Layers (Flattening)

**Use case:** Remove a VP layer and have Directors report directly to SVP

1. Select all positions currently reporting to the VP being removed
2. Click **Change Manager**
3. Select the SVP (or other higher-level leader)
4. Click **Close Position** on the now-empty VP position
5. Provide a reason: "Position eliminated as part of organizational flattening"

The OpEx Panel now shows -1 position and the associated cost savings.

#### Adding Management Layers

**Use case:** Insert a Senior Manager layer to reduce Director's span of control

1. Hover over the Director position
2. Click **Add Position**
3. Fill in the new Senior Manager details:
   - Job Title: Senior Manager, Operations
   - Department: Operations
   - Manager: Select the Director
   - Salary: Enter amount or use rate card
4. Click **Save**
5. Now select ~half of the Director's current direct reports
6. Click **Change Manager** and move them to the new Senior Manager

> **[Screenshot placeholder: Add Position dialog showing fields for Job Title, Department, Manager, Salary with Rate Card option visible]**

#### Combining Teams

**Use case:** Merge 3 small teams under one manager

1. Identify the manager who will lead the combined team
2. For each of the other two teams:
   - Select all team members
   - Change their manager to the combined team leader
3. Close the now-empty manager positions
4. Optionally update department or team names to reflect the new structure

#### Bulk Attribute Changes

**Use case:** Moving an entire team to a new department or location

1. Select the team (use Select Team or multi-select by holding Shift)
2. Click **Edit Attribute** in the bulk actions toolbar
3. Choose the field to update (e.g., Department)
4. Select the new value (e.g., "Operations & Logistics")
5. Click **Save**

All selected positions now have the updated attribute.

### Step 5: Analyze Organizational Impact

After making changes, assess the impact before finalizing.

#### Review Span of Control Changes

1. In your scenario, add **Total Span of Control** to Card Content
2. Click **Card Content** in the toolbar
3. Select **Total Span of Control** and **Direct Span of Control**
4. Click **Apply**

Now every card shows the manager's span. Visually scan for:
- Did you successfully reduce high spans (16+ → 8-10)?
- Did you eliminate very low spans (1-2 → 5-7)?
- Are managers' workloads more balanced?

> **[Screenshot placeholder: Org chart cards showing span of control numbers on each manager card, with some highlighted in green (optimal range) and others in yellow (needs attention)]**

#### Check for Broken Hierarchies

1. Use **Spotlight** → **Rules** → **Broken Hierarchies**
2. If any positions are highlighted, investigate
3. Common causes: Circular reporting relationships or positions without managers

Fix any broken hierarchies before proceeding.

#### Use the OpEx Panel (Change Tracker)

The OpEx Panel on the right side shows:
- **Total headcount change** (positions added vs. closed)
- **Total cost impact** (annual salary change)
- **Breakdown by change type:**
  - Additions (new positions)
  - Reductions (closed positions)
  - Data Changes (moves, attribute updates)

Click **👀 View Details** to see each individual change with before/after states.

> **[Screenshot placeholder: OpEx Panel showing +2 additions, -5 reductions, 12 data changes, with net savings of $450K and -3 headcount]**

**Key questions to ask:**
- Does the cost impact align with budget expectations?
- Are there unintended position closures?
- Do the moves make logical sense when reviewed individually?

#### View Changes in Forecast

To see how changes affect departmental headcount over time:

1. At the top of the scenario, click **Forecast** (next to Directory)
2. Select **Aggregate by: Department**
3. Toggle between **Show After** and **Show Changes**
4. View **Quarterly** or **Yearly**

**Show Changes** reveals:
- Which departments gained headcount (+)
- Which departments lost headcount (-)
- The timing of changes if you used effective dates

> **[Screenshot placeholder: Forecast view showing Department rows with Q1-Q4 columns, displaying +5/-5 headcount changes across departments]**

### Step 6: Create Alternative Scenarios for Comparison

Reorganizations rarely have a single "right answer." Create multiple options to compare tradeoffs.

**Example: Three reorg options**

**Scenario A: Conservative Reorg**
- Eliminate only the most obvious compression points
- Minimal cost savings (~$200K)
- Low organizational disruption

**Scenario B: Moderate Reorg**
- Flatten 2 management layers
- Consolidate some small teams
- Moderate cost savings (~$500K)
- Medium organizational disruption

**Scenario C: Aggressive Reorg**
- Flatten 3 management layers
- Consolidate all small teams
- Significant cost savings (~$900K)
- High organizational disruption

#### Compare Scenarios Side-by-Side

1. Go to the homepage
2. Select 2-4 scenarios to compare
3. Click **Compare** (bottom-right corner)
4. View side-by-side org charts, cost comparisons, and headcount comparisons

This helps leadership make informed decisions about which option best balances strategic goals, cost savings, and organizational impact.

> **[Screenshot placeholder: Scenario comparison view showing three scenarios side-by-side with cost, headcount, and pyramid chart comparisons]**

### Step 7: Gather Stakeholder Feedback

Before finalizing, share scenarios with key stakeholders.

#### Share Scenarios for Review

1. In your scenario, click **Share** or add collaborators in Scenario Settings
2. Add stakeholders by email (they'll receive access)
3. Include a note explaining:
   - Why the reorganization is needed
   - What problems it solves
   - What tradeoffs exist
4. Stakeholders can view the scenario, add comments, and provide feedback

**Pro tip:** Use the **Comments** feature to have threaded discussions directly on specific positions or sections of the org chart.

#### Iterate Based on Feedback

Common feedback and how to address it:

**"This person shouldn't report to that leader"**
- Use Change Manager to adjust reporting relationships

**"This team is too large now"**
- Split the team by adding a manager layer or redistributing people

**"We need to preserve this specific team structure"**
- Revert changes to that part of the org using Undo or manually repositioning

**"Can we phase this over two quarters instead of all at once?"**
- Use effective dates to schedule changes for different time periods (see Step 8)

### Step 8: Add Effective Dates for Phased Rollout (Optional)

If your reorganization will happen in phases, use effective dates.

**Example: Phased reorg over 2 quarters**

1. Select positions moving in **Q1**
2. Click **Edit** and set **Effective Date: January 1, 2026**
3. Select positions moving in **Q2**
4. Click **Edit** and set **Effective Date: April 1, 2026**

Now in Forecast:
- Q1 shows only the Q1 changes
- Q2 shows both Q1 and Q2 changes
- Departments see gradual headcount shifts, not sudden swings

This helps manage change more effectively and prevents overwhelming teams with too much change at once.

> **[Screenshot placeholder: Position edit dialog showing Effective Date field set to "January 1, 2026" with save button]**

### Step 9: Submit for Approval

Once the scenario is finalized and stakeholders are aligned, submit for formal approval.

#### Configure Approval Workflow

1. In your scenario, open the **OpEx Panel**
2. Click **Configure Submission** at the bottom
3. Review:
   - Global approvers (Level 1 and Level 2)
   - Scenario-specific approvers (Level 0 and Level 3) - add if needed
   - Bottom-line impact summary (headcount and cost)
4. Write a **justification** explaining:
   - Business rationale for the reorganization
   - Problems being solved
   - Expected benefits (faster decision-making, cost savings, better span of control)
   - Implementation timeline
5. Click **Submit**

> **[Screenshot placeholder: Configure Submission modal showing approver list, bottom-line cost impact, justification text field, and Submit button]**

#### Approval Process

Your scenario now enters the approval queue:
- **Level 0 (if configured):** Scenario-specific reviewers
- **Level 1:** First global approval level (department heads, HR partners)
- **Level 2:** Final global approval level (VPs, CFO, CHRO)
- **Level 3 (if configured):** Final scenario-specific reviewers

Each approver reviews changes and can:
- ✅ **Approve** changes to proceed to the next level
- ❌ **Reject** changes with reasons, sending the scenario back for revisions

**If rejected:** Review feedback, make adjustments, and resubmit. Previously approved changes remain approved, so reviewers only re-review what changed.

### Step 10: Implement the Reorganization

After final approval, implement the reorganization in your HRIS and communicate changes.

#### Export Reorganization Data

1. From the scenario, go to **Directory** view
2. Click **Export** to download a CSV with all positions and their new attributes
3. Share with HR/IT teams for implementation in Workday, SAP, or other systems

#### Communicate Changes

**Announce reorganization to affected teams:**
- Hold town halls or department meetings to explain the "why"
- Provide 1-on-1 conversations for people changing managers or roles
- Share updated org charts showing new structure
- Address concerns and questions proactively

**Messaging tips:**
- Lead with business rationale, not cost savings
- Acknowledge that change is difficult
- Emphasize benefits (clearer roles, better support, faster decisions)
- Provide a timeline and next steps

#### Monitor Post-Reorganization

After implementation:
- Check in with managers to ensure new spans of control are manageable
- Survey employees to gauge sentiment and identify issues
- Be prepared to make minor adjustments if something isn't working

## Best Practices for Reorganizations

### Do's

✅ **Start with clear objectives** - Know what problem you're solving
✅ **Analyze before acting** - Use Workforce Hub and Spotlight to identify issues
✅ **Model multiple options** - Create 2-3 scenarios to compare tradeoffs
✅ **Involve stakeholders early** - Share scenarios for feedback before finalizing
✅ **Consider span of control** - Aim for 5-9 direct reports for most managers
✅ **Phase large reorganizations** - Use effective dates to spread change over time
✅ **Communicate transparently** - Explain why changes are happening and what benefits they bring

### Don'ts

❌ **Don't reorganize without data** - Gut feelings lead to poor decisions
❌ **Don't optimize for cost alone** - Consider organizational effectiveness and employee experience
❌ **Don't surprise people** - Involve affected managers and teams in planning
❌ **Don't make changes too frequently** - Constant reorganization creates instability
❌ **Don't ignore broken hierarchies** - Fix reporting relationship issues before submitting
❌ **Don't skip approval workflows** - Ensure proper governance and accountability

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Flattening Too Aggressively

**Problem:** Removing too many management layers leaves senior leaders with 15-20 direct reports.

**Solution:** Balance flattening with realistic span of control. If a VP would have 18 direct reports after flattening, consider keeping or adding a Director layer.

### Pitfall 2: Not Considering Manager Capabilities

**Problem:** Assigning a manager 12 direct reports when they've never managed more than 3.

**Solution:** Factor in manager experience and capability. New managers should have smaller teams (4-6), experienced managers can handle more (8-10+).

### Pitfall 3: Ignoring Geographic or Functional Complexity

**Problem:** Giving a manager 10 direct reports across 5 countries and 3 functions.

**Solution:** High complexity requires lower spans. If a team is geographically dispersed or functionally diverse, keep span of control on the lower end (5-7).

### Pitfall 4: Reorganizing Without Employee Context

**Problem:** Moving people based on titles alone without considering working relationships, skills, or preferences.

**Solution:** Involve managers in the planning process. They know their people and can identify which structures will work best.

### Pitfall 5: Underestimating Change Fatigue

**Problem:** Implementing major reorganizations every 6 months, causing instability and disengagement.

**Solution:** Reorganize thoughtfully and infrequently. Give teams time to stabilize (12-18 months) before making major changes again.

## Measuring Reorganization Success

After implementation, track these metrics to evaluate success:

### Quantitative Metrics
- **Span of control distribution** - Are more managers in the 5-9 range?
- **Layers of hierarchy** - Did you reduce organizational depth as planned?
- **Cost savings** - Did you achieve projected savings?
- **Time-to-decision** - Are decisions happening faster post-reorg?

### Qualitative Metrics
- **Manager satisfaction** - Do managers feel their workload is manageable?
- **Employee engagement** - Did engagement improve or decline post-reorg?
- **Clarity of roles** - Do people understand their responsibilities better?
- **Cross-team collaboration** - Is collaboration easier in the new structure?

## Real-World Example: Commercial NA Reorganization

**Background:** The Commercial North America organization has 250 people across 8 layers. Analysis reveals:
- 40% of managers have 1-2 direct reports
- There are 3 VP-to-VP reporting relationships (compression)
- Some Directors have 18+ direct reports while others have 3

**Goals:**
1. Eliminate VP-to-VP compression
2. Reduce layers from 8 to 6
3. Balance span of control to 5-9 for all Directors
4. Save $400K annually in management costs

**Approach:**
1. Created "Commercial NA Q1 Reorg" partial org scenario
2. Identified 3 VPs with single direct reports and moved their teams to report to SVPs
3. Eliminated the now-empty VP positions
4. Split one Director's 18-person team into two 9-person teams (added a Director layer)
5. Combined three Directors with 3 reports each into one Director with 9 reports (eliminated 2 Director positions)
6. Reviewed changes in OpEx Panel: -3 VPs, -2 Directors, +1 Director = -4 net positions, $450K savings
7. Shared scenario with Commercial NA leadership for feedback
8. Adjusted based on feedback (kept one VP role that had strategic importance)
9. Submitted for approval through Level 1 (HR partner) and Level 2 (CFO, CHRO)
10. Received approval and implemented changes in Workday

**Results:**
- Reduced layers from 8 to 6 ✅
- 85% of managers now have 5-9 direct reports (up from 60%) ✅
- Eliminated all VP-to-VP compression ✅
- Saved $380K annually (close to $400K goal) ✅
- Manager satisfaction increased due to more balanced workloads ✅

## Related Resources

- **[Span of Control Analysis](span-of-control-analysis.md)** - Identify organizational inefficiencies
- **[Creating Scenarios](../scenarios/creating-scenarios.md)** - Learn scenario basics
- **[Making Position Changes](../scenarios/making-position-changes.md)** - Edit positions in scenarios
- **[Bulk Operations](../scenarios/bulk-operations.md)** - Move multiple positions efficiently
- **[Scenario Approvals](../scenarios/approvals.md)** - Submit scenarios for stakeholder review
- **[Time-Based Planning](../scenarios/time-based-planning.md)** - Use effective dates for phased rollouts
- **[Scenario Comparisons](../scenarios/scenario-comparisons.md)** - Compare multiple reorganization options

## Visual Guide

> **[Screenshot placeholder: Before and after org chart views showing reorganization - before shows 8 layers with multiple compression points, after shows 6 layers with balanced spans]**

> **[Screenshot placeholder: Change Tracker showing impact of reorganization - lists all position moves, additions, and closures with cost impact]**

> **[Screenshot placeholder: Scenario comparison of three reorg options side-by-side showing cost, headcount, and span of control differences]**

> **[Screenshot placeholder: Forecast view showing phased reorganization impact by department across Q1-Q4]**
