---
description: Implement approved scenarios to your Main Org
---

# Scenario to Main Org

Merge an approved scenario into Main Org to make planned changes the new organizational baseline.

**Before you start:**

* Only approved scenarios can be merged
* Only admins can perform this operation
* Merges are permanent

## How to Merge

1. Navigate to **Main Org**
2. Open toolbar > **Data Management** > **Merge Approved Scenarios to Main**
3. Select the approved scenario from the list
4. Click **Next**

**Select fields to merge:**

* Select All (recommended) — all scenario changes apply to Main Org
* Selective fields — only chosen fields update (e.g., Department only); useful when a scenario only modeled one type of change

**Include New Positions:**

* Check to bring new positions created in the scenario into Main Org
* Uncheck if new positions were hypothetical only

5. Review conflicts — when the same position was edited in both the scenario and Main Org since the scenario was created, a conflict appears. Click **"Use Scenario Values for All Conflicts"** — approved scenarios should be treated as the source of truth.
6. Click **Merge to Main**
7. Wait for completion, then verify changes in Main Org

## Full Org vs. Partial Org Scenarios

The merge process is the same for both. A Partial Org scenario only affects positions within its scope — the rest of Main Org is untouched.

## Before Merging

* Verify the scenario is fully approved
* Review the scenario one more time — open it and check the OpEx Panel for complete impact
* Communicate to affected teams that changes are going live
* Choose your timing — merge during low-activity periods and coordinate with team announcements

## After Merging

* Browse Main Org to confirm changes applied (new positions, reporting changes, modifications)
* Notify stakeholders that changes are live and share the updated org chart if needed
* Archive the scenario or keep it for historical reference

## Troubleshooting

| Problem                               | Solution                                                                                          |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Scenario doesn't appear in merge list | Verify scenario status = "Approved"; check admin permissions; refresh the page                    |
| New positions didn't merge            | "Include New Positions" was unchecked — create a new scenario with just those positions and merge |
| Some changes didn't apply             | Check which fields were selected; verify conflicts were resolved with scenario values             |
| Merge is taking a long time           | Wait — large orgs with many changes take longer; don't refresh the page                           |

| Problem                               | Solution                                                                                          |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Scenario doesn't appear in merge list | Verify scenario status = "Approved"; check admin permissions; refresh page                        |
| New positions didn't merge            | "Include New Positions" was unchecked — create a new scenario with just those positions and merge |
| Some changes didn't apply             | Check which fields were selected; verify conflicts were resolved with scenario values             |
| Merge is taking a long time           | Wait — large orgs with many changes take longer; don't refresh the page                           |

## Related Articles

* [Scenario Approvals](approvals.md)
* [Scenario Merging](merging.md)
* [OpEx Panel](/broken/pages/BweIAu0kM4eCKuYXwrHV)
