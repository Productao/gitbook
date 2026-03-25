---
description: Combine changes from multiple scenarios into one
icon: merge
---

# Scenario Merging

Scenario Merging lets you consolidate changes from one scenario (source) into another (destination). Use it when multiple teams have worked on separate scenarios that need to be combined.

**Best for** — Independent teams working on non-overlapping parts of the org. The less overlap between scenarios, the smoother the merge.

## How to Merge

1. Open the destination scenario
2. Go to Toolbar > **Data Management** > **Merge Scenario**

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

3. Select the source scenario from the dropdown

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

4. **Select Records** — choose All or a filtered subset
5. **Select Fields** — choose All fields or specific attributes (e.g., salary only)
6. Review the summary (records, fields, destination backup info)
7. **Conflict Review** — see conflicts and resolve (details below)

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

8. Click **Merge**

A backup of the destination scenario is automatically created before merging.

## No Conflicts (Independent Teams)

If the two scenarios modified completely different positions (e.g., one owns Engineering, the other owns Sales), no conflicts appear. Select **Merge All Fields to Destination** and click **Merge**. The merged changes appear as separate org branches — use **Make Root** on each top node if they should remain independent.

## With Conflicts (Overlapping Changes)

Conflicts occur when both scenarios modified the same position (different managers, different salaries, one closed while the other edited).

**Current resolution** — All-or-nothing. "Merge All Fields to Destination" makes the source win for all conflicts. If you want the destination to keep its values, cancel and coordinate manually.

Use the **Show only conflicts** filter to review what you'd be overwriting before deciding.

## When Not to Use Merge

* Scenarios with significant overlap — coordinate in a single shared scenario instead
* Final approved scenarios — don't merge into them; create a new scenario
* Scenarios built on different Main Org baselines

## Troubleshooting

<table><thead><tr><th width="263.3515625">Problem</th><th>Solution</th></tr></thead><tbody><tr><td>Duplicate positions after merge</td><td>Both scenarios created the same new position — delete one duplicate</td></tr><tr><td>Broken hierarchy after merge</td><td>Click the orange broken hierarchy icon > reassign managers to reconnect</td></tr><tr><td>Can't see merged changes</td><td>Clear all filters; confirm <strong>Show After</strong> mode is active</td></tr><tr><td>Merged wrong scenario</td><td>Restore from the automatic backup created before the merge</td></tr></tbody></table>

## Related Articles

* [Scenario Comparisons](comparisons.md) — Compare without merging
* [Scenario Refresh](/broken/pages/fnnfy4SZXur2iTxRXwHb) — Update scenario with Main Org changes
* [Bulk Operations](bulk-operations.md)
