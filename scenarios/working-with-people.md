---
description: Mapping employees to positions
hidden: false
---

# Working with People

Learn how to manage the relationship between employees and positions in scenarios. This guide covers assigning employees to positions, detaching employees, modeling transfers, and succession planning.

## Understanding Positions vs People

In Agentnoon, **positions** and **people** are separate concepts:

**Position** = A role in your org structure
- Job title (e.g., "Software Engineer")
- Compensation range
- Reporting relationships
- Can be vacant or filled

**Person/Employee** = An individual
- Name and employee ID
- Attached to a position (or not)
- Can move between positions

**Key concept:** Positions exist independently of people. You can have vacant positions (budgeted roles not yet filled) and you can move people between positions without deleting the old position.

---

## Position States

### Filled Position

**What it is:** Position with an employee attached

**Visual indicator:** 📎 Paperclip icon on the card

**Example:** "Software Engineer" position with "Jane Smith" assigned

---

### Vacant Position

**What it is:** Position without an employee attached

**Visual indicator:** No paperclip icon, position card shows only job title

**Example:** "Software Engineer" position (open requisition)

**When you see vacant positions:**
- New positions you just created
- Positions where employee departed or was detached
- Budgeted future hires

---

## Assigning Employees to Positions

### Assign an Employee

**How to do it:**
1. Hover over a **vacant position**
2. Click the **📎 Assign** button
3. Search bar appears
4. Type employee name or ID
5. Select employee from results
6. Click **Assign**

**What happens:**
- Employee name appears on position card
- Paperclip icon (📎) appears
- Employee is now in this role
- If employee was in another position, they're moved (not duplicated)

**When to use:**
- Filling open positions
- Modeling internal transfers
- Succession planning
- Assigning new hires to positions

---

### Quick Assign (Alternative)

**How to do it:**
1. Find the employee in another part of the org
2. Drag their card to the new position
3. Drop on the new position
4. Employee moves to new role

**Pro tip:** This is faster when you can see both positions on screen.

---

## Detaching Employees from Positions

### Detach an Employee

**How to do it:**
1. Hover over a **filled position**
2. Click **⋮** (three dots)
3. Select **Detach Employee**
4. Confirm

**What happens:**
- Employee removed from position
- Position becomes vacant
- Position remains in org chart (doesn't delete)
- Employee is available to assign elsewhere

**When to use:**
- Modeling employee departures
- Freeing an employee to reassign elsewhere
- Creating vacancies for planning purposes

**Important:** Detaching an employee does NOT delete the position. It just makes the position vacant.

---

## Moving Employees Between Positions

### Internal Transfer

**Goal:** Move an employee from one position to another.

**Method 1: Detach and Reassign**
1. **Detach** employee from current position
2. **Find** the target position
3. **Assign** employee to target position

**Method 2: Direct Assign (Recommended)**
1. **Find** the target position (vacant or create new)
2. Click **📎 Assign**
3. Search for and **select** the employee
4. Employee automatically moves from old position to new position

**What happens:**
- Employee moves to new position
- Old position becomes vacant
- New position is now filled
- Reporting relationships update

**Pro tip:** You don't need to detach first. Just assign to the new position and Agentnoon handles the move automatically.

---

## Common Employee Scenarios

### 1. Model an Internal Promotion

**Scenario:** Jane Smith (Software Engineer) is promoted to Engineering Manager.

**Steps:**
1. Create new "Engineering Manager" position (or use existing vacant one)
2. Place it under appropriate director
3. Hover over new position → Click **📎 Assign**
4. Search for "Jane Smith"
5. Assign her to new position
6. Jane's old "Software Engineer" position becomes vacant (ready for backfill)

---

### 2. Model a Lateral Move

**Scenario:** John Doe moves from Product Team A to Product Team B (same role, different manager).

**Steps:**
1. Find or create "Product Manager" position under Team B manager
2. Hover → Click **📎 Assign**
3. Search for "John Doe"
4. Assign to new position
5. Old position becomes vacant

---

### 3. Backfill a Departing Employee

**Scenario:** VP of Engineering is leaving. Need to model the replacement.

**Steps:**
1. Hover over VP position (currently filled)
2. Click **⋮** → **Add Backfill**
3. Original VP position marked as closed
4. New VP position created (vacant)
5. Optionally assign a successor to new position

**Alternative approach:**
1. **Detach** current VP (or mark position as closing)
2. Create new VP position
3. Assign successor (if known)

---

### 4. Model a New Hire

**Scenario:** Hiring 5 new Software Engineers in Q2.

**Steps:**
1. Create 5 "Software Engineer" positions (use duplicate)
2. Leave them vacant (representing open requisitions)
3. Optionally add effective dates (Q2 start dates)
4. Track cost in Change Tracker
5. Later, assign actual hires when known

---

### 5. Model Succession Planning

**Scenario:** Identify and test potential successors for leadership roles.

**Steps:**
1. Create scenario for succession planning
2. Find leadership position with potential retirement
3. Create new position with successor (or use backfill feature)
4. Assign potential successor candidate
5. Review org chart to see impact
6. Compare multiple successor scenarios (Scenario A, B, C with different candidates)

---

## The Bench

### What is the Bench?

The **bench** is a holding area for employees who are not assigned to any position.

**When employees are on the bench:**
- They're not in any position
- They don't show up in the org chart
- They're available to assign to positions
- Useful for modeling transitions

### Move to Bench

**How to do it:**
1. Hover over filled position
2. Click **⋮** → **Move to Bench**
3. Employee removed from position and placed on bench
4. Position becomes vacant

**When to use:**
- Temporarily removing employees during restructuring
- Modeling employees between roles
- Holding employees while determining new assignments

### Assign from Bench

**How to do it:**
1. Click **📎 Assign** on any vacant position
2. Search shows employees on bench
3. Select employee
4. They move from bench to position

---

## Working with New Hires

### Adding Positions for Future Hires

**Goal:** Model new positions you plan to hire into.

**Steps:**
1. Add new positions where needed
2. Leave them **vacant**
3. Set salaries/pay grades
4. Optionally set effective dates (hire dates)
5. Track cost impact in Change Tracker

**Pro tip:** Keep new hire positions vacant until you know who you're hiring. This models your plan without committing to specific people.

---

### Assigning Known Hires

**Goal:** You've identified a specific hire and want to model them in a position.

**Steps:**
1. Create the position (if not already created)
2. **Create a new employee** (if they don't exist yet):
   - Some systems let you add placeholder employees
   - Or use comments to note "Plan to hire: Sarah Johnson"
3. Assign employee to position

---

## Employee Details

### Viewing Employee Information

**How to view:**
1. Click on a filled position card
2. Employee details appear in side panel
3. See all employee attributes:
   - Name and employee ID
   - Current position
   - Start date
   - Email
   - Any other people fields

**What you can see:**
- Current role and manager
- Historical positions (if available)
- Employee-specific attributes
- Link to employee profile

---

### Editing Employee Information

**Important:** In most Agentnoon setups, employee data (name, ID, start date, etc.) syncs from your HRIS and is **read-only** in scenarios.

**What you typically CANNOT edit:**
- Employee name
- Employee ID
- Start date
- Personal information

**What you CAN edit:**
- Position the employee is assigned to
- Position-specific attributes (title, salary, department of their role)

---

## Best Practices

1. **Model positions, not just people** - Create positions first, assign people second
2. **Keep new hire positions vacant** - Don't create fake employee records for future hires
3. **Use backfill for succession** - Cleanly model departures and replacements
4. **Comment on assignments** - Explain why you made a transfer or promotion
5. **Consider effective dates** - Model when transfers/hires will actually happen
6. **Test multiple succession candidates** - Create Scenario A, B, C with different people in key roles

---

## Common Mistakes to Avoid

❌ **Deleting positions to remove employees** - Use Detach instead. Positions and people are separate.

❌ **Creating duplicate employees** - Employees can only be in one position at a time.

❌ **Editing employee personal data in scenarios** - This data syncs from HRIS and is read-only.

❌ **Not modeling vacancies** - Vacant positions are valuable! They show open reqs and future hires.

❌ **Forgetting to track transfers** - Use comments to document why someone moved.

---

## Troubleshooting

**Problem:** I can't find an employee to assign.
- **Solution:** They may already be assigned somewhere else. Detach them first, or search and assign directly (Agentnoon will move them).

**Problem:** Employee disappeared from org chart.
- **Solution:** They may have been detached and moved to bench. Check bench or search for them.

**Problem:** I assigned someone but they're still in their old position.
- **Solution:** Refresh the page. If issue persists, detach from old position manually then reassign.

**Problem:** I can't edit an employee's name or start date.
- **Solution:** This is read-only data from your HRIS. Changes must be made in your HRIS system.

**Problem:** I want to model a new hire who doesn't exist yet.
- **Solution:** Leave the position vacant and use comments to note "Future hire: Q2 2026". Or check if your admin has enabled placeholder employees.

---

## Next Steps

Now that you understand working with people:
- Learn [Time-Based Planning](time-based-planning.md) to schedule transfers and hires
- Use [Change Tracker](tracking-analysis.md) to see cost impact of moves
- Explore [Bulk Operations](bulk-operations.md) to move multiple people at once
- Try the [Succession Planning](../use-case-tutorials/succession-planning.md) tutorial
