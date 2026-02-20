---
description: Implement approved scenarios to your Main Org
hidden: false
---

# Scenario to Main Org

Merge an approved scenario into Main Org to make planned changes the new organizational baseline.

**Requirements:** Only approved scenarios can be merged; only admins can perform this operation; merges are permanent.

## How to Merge

1. Navigate to **Main Org**
2. Open taskbar > **Data Management** > **Merge Approved Scenarios to Main**
3. Select the approved scenario from the list
4. Click **Next**

**Select fields to merge:**
- **Select All** (recommended) — all scenario changes apply to Main Org
- **Selective fields** — only chosen fields update (e.g., Department only); useful when a scenario only modeled one type of change

**Include New Positions checkbox:**
- Check to bring new positions created in the scenario into Main Org
- Uncheck if new positions were hypothetical only

5. Review conflicts — when the same position was edited in both the scenario and Main Org since the scenario was created, a conflict appears. Click **"Use Scenario Values for All Conflicts"** — approved scenarios should be treated as the source of truth.
6. Click **Merge to Main**
7. Wait for completion, then verify changes in Main Org

## Full Org vs. Partial Org Scenarios

The merge process is the same for both. A partial org scenario only affects positions within its scope — the rest of Main Org is untouched.

## Before Merging

1. Verify the scenario is fully approved
2. Review it one more time (open the scenario, check Change Tracker for complete impact)
3. Communicate to affected teams that changes are going live
4. Choose timing: merge during low-activity periods; coordinate with team announcements

## After Merging

1. Browse Main Org to confirm changes applied (new positions, reporting changes, modifications)
2. Notify stakeholders that changes are live and share updated org chart if needed
3. Archive the scenario or keep for historical record

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Scenario doesn't appear in merge list | Verify scenario status = "Approved"; check admin permissions; refresh page |
| New positions didn't merge | "Include New Positions" was unchecked — create a new scenario with just those positions and merge |
| Some changes didn't apply | Check which fields were selected; verify conflicts were resolved with scenario values |
| Merge is taking a long time | Wait — large orgs with many changes take longer; don't refresh the page |

## Related Articles

- [Scenario Approvals](approvals.md)
- [Scenario Merging](merging.md)
- [Change Tracker](tracking-analysis.md)
