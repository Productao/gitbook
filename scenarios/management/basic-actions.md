---
description: Creating, renaming, duplicating, and deleting scenarios
hidden: false
---

# Basic Scenario Actions

This guide covers fundamental scenario management actions you'll use regularly: creating, renaming, duplicating, deleting, and archiving scenarios.

---

## Creating Scenarios

New scenarios are created from the homepage or scenario list. The creation process is covered in detail in the [Creating Scenarios](../creating-scenarios.md) guide.

**Quick reference:**
- Click **New Scenario** button
- Choose scenario type (Full Org, Partial Org, etc.)
- Give it a clear name
- Set effective date (optional)
- Start modeling

---

## Opening and Switching Scenarios

### Opening from Homepage

1. Go to homepage
2. Browse scenario list
3. Click scenario name to open

### Switching Between Scenarios

**From inside a scenario:**
1. Click **scenario name dropdown** in top-left
2. See list of all accessible scenarios
3. Click different scenario to switch
4. Previous scenario auto-saves

**Tip:** Use search in dropdown to find scenarios quickly.

---

## Rename a Scenario

### Why Rename

- Original name was placeholder ("Untitled Scenario")
- Purpose changed as you built it
- Need clearer name for stakeholders
- Standardizing naming conventions

### How to Rename

**From homepage or scenario list:**
1. Find the scenario
2. Click **⋮** (three dots) menu
3. Select **Rename**
4. Enter new name
5. Click **Save**

**From inside scenario:**
1. Click scenario name in top-left
2. Name becomes editable
3. Type new name
4. Press Enter

### Naming Best Practices

**Include key information:**
- Purpose: "Engineering Reorg", "Q2 Hiring Plan"
- Date or quarter: "Q2 2026", "FY27"
- Version if comparing: "Option A", "v2"
- Keep under 50 characters

**Good examples:**
- "Commercial NA Q1 2026 Expansion"
- "Engineering Reorg - Flatten Structure v2"
- "Budget Cut 10% - Option A"
- "VP Engineering Succession - Candidate A"

**Avoid:**
- Generic names: "Scenario 1", "Test", "New"
- Overly long names: "This is the scenario we discussed in the meeting on Tuesday about the reorganization"
- Inconsistent formats: Mix of date formats, abbreviations

---

## Duplicate a Scenario

### Why Duplicate

- Test alternative approaches (keep original intact)
- Create version 2 while preserving version 1
- Use existing scenario as template
- Branch to explore different options

### How to Duplicate

1. Go to homepage or scenario list
2. Find the scenario to duplicate
3. Click **⋮** (three dots) menu
4. Select **Duplicate**
5. New scenario created with name "[Original Name] Copy"
6. Rename the duplicate appropriately

### What Gets Duplicated

**Included in duplicate:**
- ✅ All positions and structure
- ✅ All changes (adds, closes, moves)
- ✅ Effective dates
- ✅ Budget settings
- ✅ Comments (typically yes, but check settings)

**Not included:**
- ❌ Shared access (typically no - only you have access to duplicate)
- ❌ Approval status (starts as draft)

### Common Workflow

**Example: Testing alternatives**
1. Create "Scenario A - Base Plan"
2. Duplicate to "Scenario B - Alternative 1"
3. Duplicate to "Scenario C - Alternative 2"
4. Model different approaches in each
5. Compare all 3 to choose best option

---

## Delete a Scenario

### When to Delete

- Test scenario no longer needed
- Outdated planning from previous quarter
- Duplicate created by mistake
- Scenario superseded by approved version

**Important:** Consider archiving instead of deleting for scenarios that might have historical value.

### How to Delete

1. Go to homepage or scenario list
2. Find the scenario to delete
3. Click **⋮** (three dots) menu
4. Select **Delete**
5. Confirm deletion

### Important Warnings

⚠️ **Deletion is permanent**
- Cannot be undone
- All changes and comments are lost
- Consider archiving instead (see below)

**Who can delete:**
- Scenario owner (creator)
- Admins (depending on settings)

---

## Archive a Scenario

### What It Does

Removes scenario from active list but preserves it for historical reference.

### When to Archive

- Scenario completed and implemented
- No longer actively working on it
- Want to preserve for reference
- Reduce clutter in scenario list

### How to Archive

1. Go to scenario list
2. Click **⋮** menu
3. Select **Archive**
4. Scenario moves to archived section

### Viewing Archived Scenarios

1. On homepage, toggle **Show Archived**
2. Archived scenarios appear (grayed out or marked)
3. Can still open and view (usually read-only)

### How to Unarchive

1. Find scenario in archived list
2. Click **⋮** menu
3. Select **Unarchive**
4. Returns to active scenario list

### Best Practice

**Archive rather than delete** for scenarios that were:
- Approved or implemented
- Used for important decisions
- May be referenced later
- Part of historical planning record

---

## Common Workflows

### Workflow 1: Version Progression

**Goal:** Iterate on a scenario through multiple versions

**Steps:**
1. Create "Hiring Plan v1" (initial draft)
2. Get feedback from stakeholders
3. Duplicate to "Hiring Plan v2" (preserves v1)
4. Make major revisions in v2
5. Get approval on v2
6. Archive v1 (keep for reference)
7. Implement v2

---

### Workflow 2: Testing Multiple Options

**Goal:** Model 3 different approaches to a problem

**Steps:**
1. Create "Budget Cut - Option A" (close junior roles)
2. Duplicate to "Budget Cut - Option B" (close senior roles)
3. Duplicate to "Budget Cut - Option C" (hybrid approach)
4. Model each approach fully
5. Compare all 3 side-by-side
6. Choose best option (e.g., Option B)
7. Delete Option A and C (or archive for reference)
8. Rename Option B to "Budget Cut - Approved"

---

### Workflow 3: Quarterly Cleanup

**Goal:** Clean up scenario list at end of quarter

**Steps:**
1. Review all scenarios from completed quarter
2. Archive approved/implemented scenarios
3. Delete test scenarios and mistakes
4. Rename any remaining scenarios for clarity
5. Tag current quarter scenarios appropriately
6. Export change logs for archived scenarios

---

## Troubleshooting

**Problem:** Can't rename scenario.
- **Solution:** You may not be the owner. Only owners can rename. Ask owner or admin.

**Problem:** Duplicate button not working.
- **Solution:** Check permissions. May require edit or admin access.

**Problem:** Deleted scenario by accident.
- **Solution:** Contact admin immediately. May be able to restore from backup (not guaranteed).

**Problem:** Scenario disappeared from list.
- **Solution:** Check if it was archived. Toggle "Show Archived" filter on homepage.

---

## Best Practices Summary

1. **Name scenarios clearly from the start** - Avoid "Untitled Scenario"
2. **Use consistent naming conventions** - Include purpose, date, version
3. **Duplicate before major changes** - Don't destroy previous versions
4. **Archive instead of delete** - Preserve historical planning records
5. **Clean up regularly** - Don't let scenario list become cluttered
6. **Document version changes** - Use comments to explain why v2 differs from v1

---

## Next Steps

Now that you understand basic scenario actions:
- Learn [Tags](tags.md) to organize scenarios by category
- Explore [Organizing Scenarios](organizing-scenarios.md) for advanced organization strategies
- Understand [Symbols](symbols.md) to interpret visual change indicators
- Return to [Scenario Management](../management.md) overview
