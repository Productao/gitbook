---
description: Add, edit, move, and remove positions
---

# Making Position Changes

All position editing happens in Scenarios — Main Org is view-only. Hover over any position card to reveal action buttons.

## Basic Actions

**Add a direct report**

1. Hover over the manager card > click **+**
2. A new blank position appears below; click Edit to fill in details (title, department, salary, location, etc.)

New positions show a green indicator in the bottom-left corner.

**Edit a position**

* Hover > click **Edit (✏️)** > modify fields in the right panel > Save
* Editable: title, department, manager, salary, pay grade, location, custom fields
* Not directly editable: employee name (use Assign/Detach), employee ID, calculated fields (SOC, layer)

**Move a position (drag-and-drop)**

* Click and hold the card, drag to the new manager, release
* To move an entire team: drag the manager card — all direct reports move with it
* Alternative: Hover > **⋮** > **Change Manager** > select from dropdown (better when the target is far away in the chart)

**Close a position (RIF)**

* Hover > click **❌** > select reason (Layoff/RIF or Exit/Voluntary) > Confirm
* Closed positions are tracked in the OpEx Panel as cost savings and remain visible (grayed out)
* Use Close (not Delete) when modeling real org changes — Close preserves the audit trail

**Duplicate a position**

* Hover > click **📋** > enter quantity > Duplicate
* All copies have the same attributes; edit each individually to customize

**Delete a position**

* Hover > **⋮** > Delete — permanently removes from scenario with no OpEx Panel record
* Use only for test positions or mistakes, not for modeling real reductions

## Employee Assignment

**Assign an employee to a vacant position**

* Hover > click **📎 Assign** > search/select employee > Assign

**Detach an employee (vacancy)**

* Hover > **⋮** > Detach Employee

## Advanced Actions (⋮ Menu)

**Add backfill:** Closes the current position and creates a new replacement with the same details. Use for succession planning or modeling departures.

**Add dotted line:** Creates matrix reporting to a secondary manager. Position keeps its primary (solid line) manager and gains a dotted-line relationship.

**Make root:** Elevates the position to top-level (no manager). Use for modeling separate org units or new subsidiaries.

**Select team:** Selects the manager and all direct reports for bulk actions.

## Selecting Multiple Positions

* **Single:** click the card
* **Multiple:** Cmd+click (Mac) or Ctrl+click (Windows)
* **Entire team:** Hover over manager > **⋮** > **Select Team**

Once selected: Change Manager for all, Close multiple, or edit attributes in bulk (see [Bulk Operations](bulk-operations.md)).

## Adding Comments

Hover > **⋮** > **Comment** — add notes, @mention collaborators, explain decisions or ask questions inline on a specific position.

## Reordering Cards

Use ← → buttons to move cards left or right within the same manager level. This is cosmetic only — it doesn't change reporting relationships.

## Troubleshooting

| Problem                                   | Solution                                         |
| ----------------------------------------- | ------------------------------------------------ |
| Can't make any changes                    | You're in Main Org (view-only) — open a scenario |
| Changes aren't showing up                 | Click Save after editing                         |
| Accidentally deleted a position           | Check Activity Log to undo, or recreate it       |
| Drag-and-drop not working                 | Use ⋮ > Change Manager instead                   |
| Can't find position to assign employee to | Create the position first, then assign           |

## Related Resources

* [Bulk Operations](bulk-operations.md)
* [Working with People](working-with-people.md)
* [Scenario Tracking & Analysis](/broken/pages/BweIAu0kM4eCKuYXwrHV)
* [Time-Based Planning](time-based-planning.md)
