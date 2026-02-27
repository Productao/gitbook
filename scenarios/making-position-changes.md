---
description: Add, edit, move, and remove positions
---

# Making Position Changes

All position editing happens in Scenarios — Main Org is view-only. Hover over any position card to reveal action buttons.

## Basic Actions

#### Add a Direct Report

1. Hover over a manager card and click **+**
2. A new blank position appears below. Click **Edit** to fill in details (title, department, salary, location, etc.)

New positions are marked with a green indicator in the bottom-left corner.

#### Edit a Position

* Hover > click **Edit** (✏️) > modify fields in the right panel > **Save**
* **Editable:** title, department, manager, salary, pay grade, location, custom fields
* **Not editable:** employee name (use Assign/Detach), employee ID, calculated fields (SOC, layer)

#### Move a position (drag-and-drop)

* Click and hold a card, drag to the new manager, and release
* To move an entire team, drag the manager card — all direct reports move with it
* **Alternative:** Hover > **⋮** > **Change Manager** > select from dropdown (better when the target is far away in the chart)

#### Close a Position

* Hover > click **❌** > select a reason (Layoff/RIF or Exit/Voluntary) > **Confirm**
* Closed positions stay visible (grayed out) and are tracked in the OpEx Panel as cost savings
* Always use **Close** instead of Delete when modeling real reductions — it preserves the audit trail

#### Duplicate a Position

* Hover > click **📋** > enter quantity > **Duplicate**
* All copies share the same attributes — edit each individually to customize

#### Delete a Position

* Hover > **⋮** > **Delete** — permanently removes the position from the scenario with no OpEx Panel record
* Use only for test positions or mistakes, not for modeling real reductions

#### Employee Assignment

**Assign an employee to a vacant position**

* Hover > click **📎 Assign** > search and select an employee > **Assign**

**Detach an employee**

* Hover > **⋮** > **Detach Employee**

## Advanced Actions (⋮ Menu)

**Add backfill** — Closes the current position and creates a new replacement with the same details. Use for succession planning or modeling departures.

**Add dotted line** — Creates matrix reporting to a secondary manager. The position keeps its primary (solid line) manager and gains a dotted-line relationship.

**Make root** — Elevates the position to top-level (no manager). Use for modeling separate org units or new subsidiaries.

**Select team** — Selects the manager and all direct reports for bulk actions.

## Selecting Multiple Positions

**Single:** click the card

**Multiple:** Cmd+click (Mac) or Ctrl+click (Windows)

**Entire team:** Hover over manager > **⋮** > **Select Team**

Once selected, you can change the manager for all, close multiple positions, or edit attributes in bulk. See [Bulk Operations](bulk-operations.md).

## Adding Comments

Hover > **⋮** > **Comment** — add notes, @mention collaborators, explain decisions or ask questions inline on a specific position.

## Reordering Cards

Use ← → buttons to move cards left or right within the same manager level. This is cosmetic only — it doesn't change reporting relationships.

## Troubleshooting

| Problem                                   | Solution                                                                                                                                                                                           |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Can't make any changes                    | Confirm you are not in the Main Org. Check if you have permissions to edit certain attributes/fields (contact your admin). Confirm you have a stable internet connection, and refresh the browser. |
| Changes aren't showing up                 | Confirm you have a stable connection to the internet, and refresh the browser.                                                                                                                     |
| Accidentally deleted a position           | Check the Activity Log to undo, or recreate the position manually                                                                                                                                  |
| Drag-and-drop not working                 | Use **⋮** > **Change Manager** and select from the dropdown instead                                                                                                                                |
| Can't find position to assign employee to | Ensure the position you would like to assign an employee to exists. If it does, please reach out to support for help.                                                                              |

## Related Resources

* [Bulk Operations](bulk-operations.md)
* [Working with People](working-with-people.md)
* [Scenario Tracking & Analysis](/broken/pages/BweIAu0kM4eCKuYXwrHV)
* [Time-Based Planning](time-based-planning.md)
