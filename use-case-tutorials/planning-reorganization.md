---
description: End-to-end reorganization workflow
hidden: false
---

# Planning a Reorganization

Model organizational changes in Agentnoon to visualize new structures, identify unintended consequences, and get stakeholder buy-in before making real-world changes.

## Step 1: Analyze the Current Structure

Before making changes, understand where problems exist.

**Span of Control analysis:**
1. Go to **Workforce Hub** > open the **Layers and Spans of Control** chart
2. Configure SOC groupings to see distribution (e.g., 0–2, 3–9, 10–15, 16+)
3. Look for: managers with 1–2 reports (inefficiency), managers with 16+ reports (burnout risk)

**Spotlight to find specific issues:**
1. Main Org > **Spotlight** > select "Direct Span of Control" > set range (e.g., 1–2)
2. Matching positions highlight across the org chart for visual navigation

Document specific problems: compression points (manager reporting to manager of same level), very long chains (8+ layers), unbalanced workloads.

## Step 2: Define Goals

Set clear, measurable objectives before modeling. Examples:
- "Reduce management layers from 8 to 6 in Commercial org"
- "Eliminate all VP-to-VP reporting relationships"
- "Balance span of control to 5–9 for all Directors"
- "Save $400K annually in management costs"

## Step 3: Create a Reorganization Scenario

1. Click **New Scenario** > select **Partial Org** (for department-specific reorgs)
2. Choose the organizational scope (e.g., "Commercial NA")
3. Name clearly: "Commercial NA Q1 2026 Reorg"

The scenario starts with the current structure as the "before" state.

## Step 4: Model the Changes

**Move individual positions:** Hover card > ⋮ menu > **Change Manager**, or drag-and-drop to new manager card.

**Move entire teams:** Hover team lead > **Select Team** (selects lead + all subordinates) > **Change Manager**.

**Flatten hierarchy (remove a layer):**
1. Select all direct reports of the position being removed
2. Change Manager to the level above
3. Close the now-empty position with reason "Organizational flattening"

**Add a management layer:**
1. Add new position under the manager (e.g., Senior Manager)
2. Move ~half the current direct reports to the new manager

**Bulk attribute changes (department/location):** Select team > **Edit Attribute** > choose field > set new value.

## Step 5: Analyze Impact

**Span of Control:** Add "Total SOC" to Card Content (Taskbar > Card Content) to see spans on every card.

**Broken hierarchies:** Spotlight > Rules > Broken Hierarchies — fix any before proceeding.

**Change Tracker (OpEx Panel):** Shows net headcount change, cost impact, and every individual change with before/after values. Review before submitting.

**Forecast view:** Switch to Forecast > Aggregate by Department > Show Changes to see which departments gained or lost headcount and when (if effective dates are set).

## Step 6: Create Alternative Scenarios

Create 2–3 options to compare tradeoffs (Conservative / Moderate / Aggressive reorg). Use **Scenario Comparisons** (homepage > select scenarios > Compare) for side-by-side cost, headcount, and structure differences.

## Step 7: Gather Feedback and Iterate

Share the scenario via Scenario Settings > add collaborators by email. Use the **Comments** feature for threaded discussion on specific positions. Common feedback:
- "Wrong reporting relationship" → Change Manager
- "Team too large" → Add a manager layer or redistribute
- "Phase this over two quarters" → Use effective dates (see Step 8)

## Step 8: Add Effective Dates for Phased Rollout

1. Select positions moving in Q1 > Edit > set **Effective Date: January 1, 2026**
2. Select positions moving in Q2 > Edit > set **Effective Date: April 1, 2026**

In Forecast, each quarter shows only the changes effective by that date.

## Step 9: Submit for Approval

1. Open **OpEx Panel** > click **Configure Submission**
2. Review approvers (Levels 0–3) and add scenario-specific approvers if needed
3. Write a justification (business rationale, problems solved, expected benefits, timeline)
4. Click **Submit**

If rejected: review feedback, make adjustments, save, and resubmit. Previously approved items typically remain approved.

## Step 10: Implement

After approval:
1. Export from Directory view as CSV to share with HR/IT for HRIS implementation
2. Communicate changes to affected teams — lead with business rationale, not cost savings
3. Monitor post-reorg: check in with managers, survey employee sentiment, adjust if needed

## Key Span of Control Guidelines

- **Optimal range:** 5–9 direct reports for most roles
- **Lower for complexity:** Geographically dispersed or highly cross-functional teams → aim for 5–7
- **New managers:** 4–6 reports; experienced managers can handle 8–10+
- **Avoid:** 1–2 reports (inefficiency) or 16+ reports (burnout risk)

## Related Resources

- [Span of Control Analysis](span-of-control-analysis.md)
- [Bulk Operations](../scenarios/bulk-operations.md)
- [Scenario Approvals](../scenarios/approvals.md)
- [Time-Based Planning](../scenarios/time-based-planning.md)
- [Scenario Comparisons](../scenarios/scenario-comparisons.md)
