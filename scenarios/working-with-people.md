---
description: Mapping employees to positions
icon: people-line
---

# Working with People

Positions and employees are separate in Agentnoon. Positions are roles in your org structure; employees are the people filling them. A position can be vacant or filled, and employees can move between positions independently.

## Assign an Employee to a Position

1. Hover over a vacant position > click **Assign** (📎)
2. Search by name or employee ID > select > **Assign**

The employee appears on the card. If they were already in another position, they move automatically - no need to detach first.

**Alternative:** Drag an employee's card onto a target position when both are visible on screen.

## Detach an Employee

Hover over a filled position > **⋮** > **Detach Employee** > **Confirm**.

The position becomes vacant and remains in the org chart. The employee is available to reassign elsewhere.

## Common Scenarios

**Internal transfer** - Find the target position > **Assign** > search for the employee. They automatically move from their current position, which becomes vacant.

**Promotion** - Create the new higher-level position under the correct manager > **Assign** the employee to it > their old position becomes vacant for backfill. Note: make sure you have employee & position level fields separated as only employee level fields get copied over.

**Backfill (departing employee)** - Hover over the departing employee's position > **⋮** > **Add Backfill** — closes the existing position and creates a new vacant one in its place.

**Model new hires** - Add positions, leave them vacant, and set salaries and hire dates. Assign real people later when known. Track cost impact in the OpEx Panel.

**Succession planning** - Create multiple scenarios (e.g., Scenario A for Candidate 1, Scenario B for Candidate 2), each assigning a different person to the leadership role.

## The Bench

The bench is a holding area for employees not assigned to any position. They don't appear in the org chart but are available for assignment.

**Move to bench** - Hover over a filled position > **⋮** > **Move to Bench** — the employee moves to the bench and the position becomes vacant.

**Assign from bench** - Click **Assign** on any vacant position — bench employees appear in search results.

Use the bench during large restructurings to temporarily park employees while you determine their new assignments.

## Employee Data Limits

Most employee data (name, ID, start date, personal info) syncs from your HRIS and is read-only in scenarios. What you can change: which position they're assigned to and position-specific attributes (title, salary, department, manager of the role).

## Troubleshooting

| Problem                                       | Solution                                                                                        |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Can't find an employee to assign              | They may already be assigned elsewhere - assign directly and Agentnoon moves them automatically |
| Employee disappeared from org chart           | They may have been detached or moved to the bench - search for them or check the bench          |
| Still appears in old position after assigning | Refresh the page. If it persists, detach manually then reassign                                 |
| Can't edit employee name or start date        | This is read-only - make the change in your HRIS                                                |
| Need to model a not-yet-known future hire     | Leave the position vacant and use Comments to note "Future hire: Q2 2026"                       |

## Related Articles

* [Making Position Changes](making-position-changes.md)
* [Time-Based Planning](time-based-planning.md)
* [Bulk Operations](bulk-operations.md)
