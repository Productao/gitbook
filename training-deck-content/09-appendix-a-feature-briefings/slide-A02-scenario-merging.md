# Slide A2 — Scenario Merging

## Title
Scenario Merging

## Lead-line
Consolidate changes from multiple scenarios into one — ideal when different teams plan in parallel.

## What Is It?
Scenario Merging lets you take changes from a source scenario and apply them to a destination scenario. This is useful when independent teams have been working on different parts of the org in separate scenarios and you need to bring it all together.

## How to Set It Up
1. Create separate scenarios for each team or workstream (e.g., "Engineering Reorg" and "Sales Restructure")
2. Each team works independently in their own scenario
3. Ensure the teams are working on **non-overlapping** parts of the org for best results

## How to Use It
1. Open the **destination** scenario (the one you want to merge into)
2. Go to **Data Management** → **Merge Scenario**
3. Select the **source** scenario
4. Choose which **records and fields** to bring over
5. Review any **conflicts** (positions changed in both scenarios)
6. Click **Merge** — an automatic backup of the destination is created before merging
7. Conflicts are resolved on an **all-or-nothing basis** — the source scenario's version wins

## When NOT to Use It
- Significant overlap between scenarios (same positions changed in both)
- One or both scenarios are already approved
- Scenarios were created from different baselines or at very different times

## Screenshot / Visual
The Merge Scenario dialog showing the source selector, record/field selection, and conflict review.

## Speaker Notes
Merging works best when it's planned from the start. Before creating separate scenarios, agree on who handles which department or team. If there's overlap — say, both teams moved the same position — the merge will flag it as a conflict, but the resolution is all-or-nothing (source wins). For this reason, minimize overlap wherever possible. Always review the merged result carefully before submitting for approval.
