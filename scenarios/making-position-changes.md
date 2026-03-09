---
description: Add, edit, move, and remove positions
icon: up-down-left-right
---

# Making Position Changes

All position editing happens in Scenarios - Main Org is view-only. Hover over any position card to reveal action buttons.

## Basic Actions

#### Add a Direct Report

1. Hover over a manager card and click **+**

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 11.13.47 AM.png" alt=""><figcaption></figcaption></figure>

2. A new blank position appears below. Click **Edit** to fill in details (title, department, salary, location, etc.)

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 11.16.41 AM.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 2026-03-06 at 11.14.57 AM.png" alt=""><figcaption></figcaption></figure>

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
* Always use **Close** instead of Delete when modeling real reductions - it preserves the audit trail

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 11.17.15 AM.png" alt=""><figcaption></figcaption></figure>

#### Duplicate a Position

* Hover > click **📋** > enter quantity > **Duplicate**

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 11.46.50 AM.png" alt=""><figcaption></figcaption></figure>

* All copies share the same attributes - edit each individually to customize

#### Delete a Position

* Hover > **⋮** > **Delete** — permanently removes the position from the scenario with no OpEx Panel record

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

* Use only for test positions or mistakes, not for modeling real reductions

#### Employee Assignment

**Assign an employee to a vacant position**

* Hover > click **📎 Assign** > search and select an employee > **Assign**

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 11.49.32 AM.png" alt=""><figcaption></figcaption></figure>

**Detach an employee**

* Hover > click **📎 Assign** > **Detach Employee**

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Advanced Actions (⋮ Menu)

**Add backfill** - Closes the current position and creates a new replacement with the same details. Use for succession planning or modeling departures.

**Add dotted line** - Creates matrix reporting to a secondary manager. The position keeps its primary (solid line) manager and gains a dotted-line relationship.

**Make root** - Elevates the position to top-level (no manager). Use for modeling separate org units or new subsidiaries.

**Select team** - Selects the manager and all direct reports for bulk actions.

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 11.57.38 AM.png" alt=""><figcaption></figcaption></figure>

## Selecting Multiple Positions

**Single:** click the card

**Multiple:** Cmd+click (Mac) or Ctrl+click (Windows), hovering over a card and pressing "x" on your keyboard

**Entire team:** Hover over manager > **⋮** > **Select Team**

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 12.00.32 PM.png" alt=""><figcaption></figcaption></figure>

Once selected, you can change the manager for all, close multiple positions, or edit attributes in bulk. See [Bulk Operations](bulk-operations.md).

## Adding Comments

Hover > **⋮** > **Comment** — add notes, explain decisions or ask questions inline on a specific position.

<figure><img src="../.gitbook/assets/Screenshot 2026-03-04 at 11.59.14 AM.png" alt=""><figcaption></figcaption></figure>

## Reordering Cards

Use ← → buttons to move cards left or right within the same manager level. This is cosmetic only — it doesn't change reporting relationships.

## Troubleshooting

| Problem                                   | Solution                                                                                                                                                                                           |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Can't make any changes                    | Confirm you are not in the Main Org. Check if you have permissions to edit certain attributes/fields (contact your admin). Confirm you have a stable internet connection, and refresh the browser. |
| Changes aren't showing up                 | Confirm you have a stable connection to the internet, and refresh the browser.                                                                                                                     |
| Drag-and-drop not working                 | Use **⋮** > **Change Manager** and select from the dropdown instead                                                                                                                                |
| Can't find position to assign employee to | Ensure the position you would like to assign an employee to exists. If it does, please reach out to support for help.                                                                              |

## Related Resources

* [Bulk Operations](bulk-operations.md)
* [Working with People](working-with-people.md)
* [Scenario Tracking & Analysis](/broken/pages/BweIAu0kM4eCKuYXwrHV)
* [Time-Based Planning](time-based-planning.md)
