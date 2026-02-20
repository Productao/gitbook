---
description: Planning merger and acquisition integration
icon: building
---

# M&A Integration

Plan post-acquisition integration by modeling combined org structures, identifying redundancies, and analyzing cost synergies before making real-world changes.

## Prerequisites

**From both companies:**
- Acquiring company: Main Org loaded in Agentnoon
- Acquired company: HRIS export (CSV with positions, managers, compensation)

Add a "Company" attribute to the acquired company's data file to distinguish employees during analysis.

## Step 1: Upload Acquired Company Data

Use **Partial Upload** to add the acquired org alongside your existing Main Org:

1. Go to **Admin > Data Upload**
2. Select **Partial Upload**
3. Upload the acquired company's CSV file
4. Map fields and confirm

Both organizations now appear side-by-side in Main Org. Verify by filtering the Directory by "Company" attribute.

## Step 2: Create an Integration Scenario

1. Go to **Scenarios > Create New Scenario**
2. Name it: "M&A Integration - [Acquired Company]"
3. Add tags: "M&A", "Integration", "[Year]"

Your scenario starts with both organizations unintegrated.

## Step 3: Plan Leadership Structure

Start at the top and work down:

1. Decide which executive roles to keep, merge, or eliminate (e.g., two CFOs → one CFO)
2. Use **Change Manager** to set new reporting relationships
3. Close redundant positions with a reason note
4. Set **effective dates** for phased transitions (Day 1, 90-day, 180-day)

**Common approaches:** Retain acquiring company leadership (fastest), best-of-both selection (higher retention), or redesign from scratch (most complex).

## Step 4: Integrate Departments

For each function (Finance, HR, Engineering, etc.):

1. Filter the Directory to that department in both companies
2. Identify duplicate roles and decide: consolidate, phase, or keep separate
3. Move teams using **Change Manager** or drag-and-drop
4. Close eliminated positions
5. Use the **Bench** to hold positions during transition

**Example:** Two Finance orgs (15 + 12 people) → Combined Finance team of 20 under one CFO, 5 redundancies eliminated.

## Step 5: Analyze Cost Impact

Open the **Change Tracker** to review:
- Net headcount reduction
- Annual compensation savings by department
- Total cost synergies vs. targets

Focus on ongoing savings, not one-time severance costs.

## Step 6: Phase the Integration

Use effective dates to stagger changes:

| Phase | Timing | Focus |
|-------|--------|-------|
| Day 1 | Immediate | Leadership, critical redundancies |
| 30-60 days | Month 2 | Support functions (HR, Finance, Legal) |
| 90-120 days | Quarter 2 | Customer-facing teams, product |
| 6-12 months | Ongoing | Full integration, culture |

View phasing in **Forecast** > Quarterly > Show Changes.

## Step 7: Compare Integration Approaches

Create multiple scenarios to evaluate tradeoffs:

- **Fast (3 months):** Maximum synergies, higher disruption
- **Moderate (6 months):** Balanced approach, standard timeline
- **Slow (12 months):** Minimal disruption, slower savings
- **Selective:** Integrate support only, keep customer-facing separate

Use **Scenario Comparisons** to view headcount, cost, and timing differences side-by-side.

## Step 8: Export for Approval

1. **PowerPoint:** Before/after org charts for executive review
2. **Excel:** Cost synergies by function and phase
3. **Change summary:** All position changes documented

## Common Challenges

**Duplicate talent in same role:** Create a new expanded role, assign to different geography, or model retention bonus for the employee not selected.

**Incompatible systems (titles, levels, comp):** Harmonize gradually using scenarios to model transition states; phase system consolidation separately from org integration.

**Customer disruption risk:** Keep customer-facing teams stable and integrate back-office first.

## Related Articles

- [Planning a Reorganization](planning-reorganization.md)
- [Scenario Comparisons](../scenarios/comparisons.md)
- [Time-Based Planning](../scenarios/time-based-planning.md)
- [Partial Upload Guide](../admin/data-management/partial-upload.md)
