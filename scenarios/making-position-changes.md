---
description: Add, edit, move, and remove positions
icon: user-gear
hidden: false
---

# Making Position Changes

Learn all the ways to modify positions in scenarios. This guide covers everything from basic actions (add, edit, move) to advanced operations (dotted lines, backfills, making root positions).

## Overview

In scenarios, you have full editing power to model any organizational change. All actions are performed by **hovering over a position card** to reveal action buttons.

**Important:** Position editing is ONLY available in Scenarios, not in Main Org. Main Org is view-only.

---

## Basic Position Actions

### Hover to Reveal Actions

When you hover over any position card in a scenario, you'll see action buttons appear:

**Quick actions (always visible):**
- ← → **Move left/right** - Reorder cards at same level
- ➕ **Add position** - Add a direct report below this position
- ✏️ **Edit** - Modify position details
- 📎 **Assign** - Attach an employee to this position
- 📋 **Duplicate** - Create copies of this position
- ❌ **Close** - Mark position as closed (RIF)
- **⋮** (three dots) - Advanced actions menu

---

## 1. Adding Positions

### Add a Direct Report

**How to do it:**
1. Hover over the position that will be the **manager**
2. Click the **➕ Add Position** button
3. A new blank position card appears below
4. Click **Edit** on the new card to add details

**What you can add:**
- Job title
- Department
- Salary/compensation
- Location
- Pay grade
- Any custom fields

**Visual indicator:** New positions show a **green icon** in the bottom-left corner.

**Pro tip:** Add positions one at a time for simple changes. Use [Bulk Operations](bulk-operations.md) to add many positions at once.

---

## 2. Editing Positions

### Edit Position Details

**How to do it:**
1. Hover over any position
2. Click the **✏️ Edit** button
3. Edit panel opens on the right side
4. Modify any fields
5. Click **Save**

**What you can edit:**
- Job title
- Department
- Manager (reports to)
- Salary
- Pay grade
- Location (work city, work country)
- Job function
- Any custom fields configured by your admin

**Fields you typically CANNOT edit:**
- Employee name (use Assign/Detach instead)
- Employee ID
- Auto-calculated fields (SOC, Total Org Size, Layer)

**Pro tip:** Edit one position at a time for precision. Use [Bulk Operations](bulk-operations.md) to edit many positions simultaneously.

---

## 3. Moving Positions

### Drag and Drop (Single Position)

**How to do it:**
1. Click and **hold** on a position card
2. **Drag** to the new manager
3. **Drop** under the new manager
4. Position reporting relationship updates immediately

**What happens:**
- Position moves to new manager
- Reporting relationships update
- Org chart restructures automatically
- No cost change (it's a move, not an add)

---

### Drag and Drop (Entire Team)

**How to do it:**
1. Click and **hold** on a manager's card
2. **Drag** the entire team (manager + all direct reports)
3. **Drop** under a new manager
4. The whole team moves together

**What happens:**
- Manager changes reporting relationship
- All direct reports stay with their manager
- Entire team structure moves intact
- Useful for reorganizations

**Pro tip:** This is the fastest way to reorganize entire teams.

---

### Change Manager (Alternative Method)

**How to do it:**
1. Hover over a position
2. Click **⋮** (three dots) for advanced menu
3. Select **Change Manager**
4. Choose new manager from dropdown
5. Click **Save**

**When to use this instead of drag-and-drop:**
- New manager is far away in the org chart (hard to drag)
- Moving multiple positions to the same manager
- More precise than drag-and-drop

---

## 4. Closing Positions (RIF)

### Close a Position

**How to do it:**
1. Hover over the position
2. Click the **❌ Close** button (minus icon)
3. Select closure reason:
   - **Layoff (Reduction in Force)** - Position eliminated due to budget/restructuring
   - **Exit (Voluntary Departure)** - Employee leaving voluntarily
4. Click **Confirm**

**What happens:**
- Position marked as closed
- Stays visible in org chart (grayed out or marked)
- Tracked in Change Tracker as cost savings
- If employee is attached, they can be reassigned or removed

**Important:** Closing tracks savings and keeps historical record. This is different from deleting (see below).

---

## 5. Duplicating Positions

### Duplicate a Position

**How to do it:**
1. Hover over the position to duplicate
2. Click the **📋 Duplicate** button
3. Select how many copies:
   - **1x** - One copy
   - **5x** - Five copies
   - **Custom** - Enter a number
4. Click **Duplicate**

**What happens:**
- Multiple identical positions created
- All have same title, salary, department, etc.
- All report to the same manager
- You can edit each one individually after

**When to use:**
- Adding multiple similar roles (e.g., 5 Software Engineers)
- Scaling a team quickly
- Modeling uniform growth

**Pro tip:** Duplicate then edit individual copies to customize (e.g., "Software Engineer - iOS", "Software Engineer - Android").

---

## 6. Deleting Positions

### Delete a Position

**How to do it:**
1. Hover over position
2. Click **⋮** (three dots) for advanced menu
3. Select **Delete**
4. Confirm deletion

**What happens:**
- Position permanently removed from scenario
- Does NOT track in Change Tracker
- No historical record
- Cannot undo (except through Activity Log)

**When to use:**
- Cleaning up test positions
- Removing mistakes
- Cleaning up data

**When NOT to use:**
- Modeling budget cuts → Use **Close** instead (tracks savings)
- Eliminating real positions → Use **Close** instead (preserves history)

**Important:** Delete is for cleanup. Close is for modeling real organizational changes.

---

## 7. Assigning Employees to Positions

### Assign an Employee

**How to do it:**
1. Hover over a **vacant position** (no employee attached)
2. Click the **📎 Assign** button
3. Search for or select an employee
4. Click **Assign**

**What happens:**
- Employee name appears on position card
- Paperclip icon (📎) shows position is filled
- Employee is now associated with this position

**When to use:**
- Filling vacant positions
- Modeling internal transfers
- Succession planning (moving people to new roles)

---

### Detach an Employee

**How to do it:**
1. Hover over a **filled position** (has employee)
2. Click **⋮** (three dots)
3. Select **Detach Employee**
4. Confirm

**What happens:**
- Employee removed from position
- Position becomes vacant
- Position remains in org chart

**When to use:**
- Modeling employee departures
- Freeing up an employee to move elsewhere
- Creating vacancies

---

## Advanced Position Actions

All advanced actions are accessed through the **⋮** (three dots) menu.

### 1. Add a Backfill

**What it does:** Closes the current position and creates a new replacement position.

**How to do it:**
1. Hover over position
2. Click **⋮** → **Add Backfill**
3. New position created with same details
4. Original position marked as closed

**When to use:**
- Succession planning
- Replacing departing employees
- Modeling role transitions

**Example:** Current VP is retiring. Add backfill to model the replacement VP.

---

### 2. Create Dotted Line Reporting

**What it does:** Establishes matrix reporting where a position reports to multiple managers.

**How to do it:**
1. Hover over position
2. Click **⋮** → **Add Dotted Line**
3. Select the second manager
4. Click **Add**

**What happens:**
- Position has solid line to primary manager
- Dotted line shows to secondary manager
- Useful for cross-functional teams

**When to use:**
- Matrix organizations
- Project-based reporting
- Cross-functional collaboration

**Example:** Product Manager reports solidly to VP Product, dotted line to VP Engineering.

---

### 3. Make Position a Root

**What it does:** Makes a position a top-level role (like CEO).

**How to do it:**
1. Hover over position
2. Click **⋮** → **Make Root**
3. Position moves to top level

**When to use:**
- Creating multiple organization charts
- Modeling separate business units
- Building new organizations from scratch

**Example:** Modeling a new subsidiary with its own CEO.

---

### 4. Select Positions (for Bulk Actions)

**How to select:**

**Single position:**
- Click on the position card (it highlights)

**Multiple positions:**
- Hold **Cmd (Mac)** or **Ctrl (Windows)**
- Click multiple position cards
- All selected positions highlight

**Entire team:**
- Hover over manager
- Click **⋮** → **Select Team**
- Manager + all direct reports selected

**Keyboard shortcut:**
- **Cmd+K (Mac)** or **Ctrl+K (Windows)** for quick selection mode

**Once selected, you can:**
- Change manager for all at once
- Close multiple positions
- Edit attributes for all (see [Bulk Operations](bulk-operations.md))

---

### 5. Add Comments

**How to do it:**
1. Hover over position
2. Click **⋮** → **Comment**
3. Write your comment
4. Optionally **@mention** collaborators
5. Click **Post**

**When to use:**
- Explaining why you made a change
- Asking for feedback from stakeholders
- Discussing position-specific questions
- Documenting assumptions

**Example:** "@jsmith - Should this role report to Product or Engineering?"

---

## Moving Cards Left and Right

**What it does:** Changes the display order of positions at the same level (doesn't change reporting).

**How to do it:**
1. Hover over position
2. Click **←** to move left
3. Click **→** to move right

**When to use:**
- Organizing card display order
- Grouping similar roles visually
- Improving readability

**Note:** This is cosmetic only. It doesn't change org structure or reporting relationships.

---

## Common Workflows

### Reorganize a Team

1. **Identify the team** to reorganize
2. **Select the manager** and their team
3. **Drag to new manager** OR use Change Manager
4. **Verify** reporting relationships look correct
5. **Check Change Tracker** for cost impact

---

### Model a Budget Cut

1. **Identify positions** to close
2. **Close each position** using ❌ button
3. Select **"Layoff (RIF)"** as reason
4. **Review Change Tracker** to see savings
5. **Verify** org structure still functions

---

### Add a New Department

1. **Add a department head** position under appropriate VP
2. **Duplicate** base positions (e.g., 5 engineers, 2 designers)
3. **Edit each position** to customize titles/details
4. **Review Change Tracker** for total cost
5. **Verify** reporting structure

---

### Model an Internal Transfer

1. **Detach employee** from current position
2. **Find target position** (create if needed)
3. **Assign employee** to new position
4. **Review** org chart to verify
5. **Add comment** explaining the transfer

---

## Best Practices

1. **Make changes incrementally** - Don't try to reorganize everything at once
2. **Check Change Tracker frequently** - Keep an eye on cost impact
3. **Use comments to document** - Explain your reasoning
4. **Close (don't delete) when modeling RIFs** - Preserves tracking
5. **Duplicate for similar roles** - Faster than creating each manually
6. **Use drag-and-drop for small moves** - Use Change Manager for large reorganizations
7. **Select teams, not individuals** - Faster to move entire teams together

---

## Troubleshooting

**Problem:** I can't make any changes to positions.
- **Solution:** You're in Main Org (view-only). Create a Scenario to make changes.

**Problem:** Changes aren't showing up.
- **Solution:** Click **Save** after editing. Changes require confirmation.

**Problem:** I accidentally deleted a position.
- **Solution:** Check Activity Log to undo, or recreate the position.

**Problem:** Drag-and-drop isn't working.
- **Solution:** Use Change Manager instead (⋮ menu → Change Manager).

**Problem:** I can't find a position to move someone to.
- **Solution:** Create the position first, then assign the employee.

---

## Next Steps

Now that you know how to make position changes:
- Learn [Bulk Operations](bulk-operations.md) for faster editing
- Explore [Working with People](working-with-people.md) for employee assignments
- Use [Change Tracker](tracking-analysis.md) to monitor impact
- Try [Time-Based Planning](time-based-planning.md) to schedule changes
- See the [Planning a Reorganization](../use-case-tutorials/planning-reorganization.md) tutorial

