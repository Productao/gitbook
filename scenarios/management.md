---
description: Organizing, tagging, and versioning scenarios
icon: folder-tree
hidden: false
---

# Scenario Management

As you create more scenarios, keeping them organized becomes essential. This guide covers scenario management features including renaming, duplicating, tagging, archiving, and understanding visual symbols that indicate changes.

## The Scenario List

### Accessing Your Scenarios

**From homepage:**
- See all your scenarios listed
- Scenarios you created
- Scenarios shared with you
- Organized by tags (if used)

**From inside a scenario:**
- Click **scenario name dropdown** in top-left
- See list of all accessible scenarios
- Select different scenario to switch

---

## Basic Scenario Actions

### Rename a Scenario

**Why rename:**
- Original name was placeholder ("Untitled Scenario")
- Purpose changed as you built it
- Need clearer name for stakeholders
- Standardizing naming conventions

**How to rename:**
1. Go to homepage or scenario list
2. Find the scenario
3. Click **⋮** (three dots) menu
4. Select **Rename**
5. Enter new name
6. Click **Save**

**Or from inside scenario:**
1. Click scenario name in top-left
2. Name becomes editable
3. Type new name
4. Press Enter

**Naming best practices:**
- Include purpose: "Engineering Reorg", "Q2 Hiring Plan"
- Include date or quarter: "Q2 2026", "FY27"
- Include version if comparing: "Option A", "v2"
- Keep under 50 characters

**Good examples:**
- "Commercial NA Q1 2026 Expansion"
- "Engineering Reorg - Flatten Structure v2"
- "Budget Cut 10% - Option A"

---

### Duplicate a Scenario

**Why duplicate:**
- Test alternative approaches (keep original intact)
- Create version 2 while preserving version 1
- Use existing scenario as template
- Branch to explore different options

**How to duplicate:**
1. Go to homepage or scenario list
2. Find the scenario to duplicate
3. Click **⋮** (three dots) menu
4. Select **Duplicate**
5. New scenario created with name "[Original Name] Copy"
6. Rename the duplicate appropriately

**What gets duplicated:**
- All positions and structure
- All changes (adds, closes, moves)
- Effective dates
- Budget settings
- Comments (typically yes, but check settings)
- Shared access (typically no - only you have access to duplicate)

**Common workflow:**
1. Create "Scenario A - Base Plan"
2. Duplicate to "Scenario B - Alternative 1"
3. Duplicate to "Scenario C - Alternative 2"
4. Model different approaches in each
5. Compare all 3 to choose best option

---

### Delete a Scenario

**When to delete:**
- Test scenario no longer needed
- Outdated planning from previous quarter
- Duplicate created by mistake
- Scenario superseded by approved version

**How to delete:**
1. Go to homepage or scenario list
2. Find the scenario to delete
3. Click **⋮** (three dots) menu
4. Select **Delete**
5. Confirm deletion

**Important:**
- Deletion is **permanent**
- Cannot be undone
- All changes and comments are lost
- Consider archiving instead (see below)

**Who can delete:**
- Scenario owner (creator)
- Admins (depending on settings)

---

### Archive a Scenario

**What it does:** Removes scenario from active list but preserves it for historical reference.

**When to archive:**
- Scenario completed and implemented
- No longer actively working on it
- Want to preserve for reference
- Reduce clutter in scenario list

**How to archive:**
1. Go to scenario list
2. Click **⋮** menu
3. Select **Archive**
4. Scenario moves to archived section

**How to view archived:**
1. On homepage, toggle **Show Archived**
2. Archived scenarios appear (grayed out or marked)
3. Can still open and view (usually read-only)

**How to unarchive:**
1. Find scenario in archived list
2. Click **⋮** menu
3. Select **Unarchive**
4. Returns to active scenario list

**Best practice:** Archive rather than delete for scenarios that were approved or implemented. Keeps historical record.

---

## Organizing with Tags

### What Are Tags?

**Tags** are labels you attach to scenarios to group related plans together.

**Common tag categories:**
- **By department:** "Engineering", "Sales", "Marketing"
- **By planning cycle:** "Q1 2026", "Q2 2026", "Annual"
- **By purpose:** "Budget Cuts", "Growth Plans", "Reorgs"
- **By status:** "Draft", "In Review", "Approved"
- **By project:** "AI Initiative", "Expansion EMEA"

---

### Creating Tags

**How to create:**
1. Go to scenario list
2. Click **⋮** menu on any scenario
3. Select **Change Tag**
4. Type new tag name
5. Press **Enter**
6. Tag created and applied to scenario

**Tag naming:**
- Short and clear
- Consistent across scenarios
- Avoid special characters
- Capitalize for readability

---

### Applying Tags to Scenarios

**How to add tag:**
1. Find scenario in list
2. Click **⋮** menu
3. Select **Change Tag**
4. Choose existing tag from dropdown OR create new
5. Tag applied

**Multiple tags:**
- Depending on settings, may support single or multiple tags per scenario
- Check with your admin

**Tag indicator:**
- Scenarios show tag label
- Can filter scenario list by tag

---

### Filtering by Tags

**How to filter:**
1. On homepage/scenario list
2. Click **Filter** or tag dropdown
3. Select tag
4. Only scenarios with that tag appear

**When to use:**
- Find all scenarios for a department
- See all Q2 planning scenarios
- Focus on specific project scenarios

---

### Removing Tags

**How to remove:**
1. Click **⋮** menu on scenario
2. Select **Change Tag**
3. Select "No Tag" or clear selection
4. Tag removed from scenario

---

## Understanding Scenario Symbols

As you make changes in scenarios, Agentnoon adds **visual symbols** to position cards to indicate what changed. This helps you (and collaborators) quickly see at a glance what's different from the baseline.

### Symbol Guide

#### ➕ Newly Added Position (Green Icon)

**What it means:** This position was added in the scenario (didn't exist in Main Org).

**Visual:** Green icon in bottom-left corner of position card.

**Example:** New "Software Engineer" position created for Q2 hiring.

---

#### ❌ RIF / Layoff (Red Icon)

**What it means:** Position marked for Reduction in Force (layoff/elimination).

**Visual:** Red icon or strikethrough on position card.

**Example:** "Account Manager" position closed due to budget cuts.

---

#### 🚪 Exit (Orange Icon)

**What it means:** Position marked as voluntary departure (resignation, retirement).

**Visual:** Orange icon on position card.

**Example:** "VP Sales" retiring, position closed as exit.

---

#### ✏️ Edit (Blue Icon)

**What it means:** Position attributes modified (title, salary, department, etc.) but position not added or closed.

**Visual:** Blue icon on position card.

**Example:** "Marketing Coordinator" title changed to "Marketing Manager" with salary increase.

---

#### 🔀 Move (Purple Arrow Icon)

**What it means:** Position moved to different manager (reporting relationship changed).

**Visual:** Purple arrow icon on position card.

**Example:** "Product Manager" moved from VP Product to VP Engineering.

---

#### 🪑 Bench (Yellow Icon)

**What it means:** Employee moved to bench (removed from org chart but not closed).

**Visual:** Yellow icon on position card.

**Example:** Employee temporarily removed from structure during reorg planning.

---

#### 📎 Detach (Gray Icon)

**What it means:** Employee detached from position, leaving position vacant.

**Visual:** Gray icon, position card shows no employee name.

**Example:** Current employee removed, position left open for backfill.

---

#### 🔒 Closed Position (Lock Icon)

**What it means:** Vacant position that has been filled and closed (no longer open requisition).

**Visual:** Lock icon on position card.

**Example:** Open "Software Engineer" req filled, position closed.

---

### Using Symbols Effectively

**Scan for changes quickly:**
- Open scenario
- Visually scan for colored icons
- Immediately see what changed without reading Change Tracker

**Communicate with stakeholders:**
- Share scenario
- Stakeholders understand symbols
- No explanation needed for standard changes

**Review before approval:**
- Ensure all symbols match intent
- Check for unintended changes (e.g., accidental edits)

---

## Exporting Scenario Data

### Export Change Log (CSV)

**What it includes:**
- All position changes (adds, closes, modifications)
- Headcount adjustments
- Cost changes
- Before and after values

**How to export:**
1. Open scenario
2. Click **Export** or **Download** in taskbar
3. Select **Comparison** or **Change Log**
4. Choose **CSV** format
5. Click **Export**
6. File downloads

**When to use:**
- Offline analysis in Excel
- Creating detailed reports
- Archiving scenario decisions
- Sharing with finance team

**Learn more:** [Exporting & Reporting](../directory/exporting-reporting.md)

---

### Export Org Chart (PDF)

**What it includes:**
- Visual org chart
- Position details
- Can include symbols/changes

**How to export:**
1. Open scenario
2. Click **Export** button
3. Select **Org Chart**
4. Choose **PDF** format
5. Select options (show symbols, include Change Tracker, etc.)
6. Click **Export**

**When to use:**
- Presentations
- Printed handouts
- Board meetings
- External stakeholders

---

## Scenario Versioning Best Practices

### Version Naming Convention

**Use consistent naming for versions:**
- "Plan v1", "Plan v2", "Plan v3"
- "Option A", "Option B", "Option C"
- "Conservative", "Moderate", "Aggressive"
- "Q1 Draft", "Q1 Revised", "Q1 Final"

**Why this helps:**
- Easy to identify latest version
- Clear when comparing scenarios
- Stakeholders understand progression

---

### When to Create New Version

**Create new version when:**
- Major direction change
- Stakeholder feedback requires significant revisions
- Testing completely different approach
- Want to preserve previous version

**Don't create new version for:**
- Minor tweaks
- Small adjustments
- Iterative changes within same approach

**Use duplicate to create versions:**
1. "Engineering Reorg v1" (original)
2. Duplicate → "Engineering Reorg v2" (alternative approach)
3. Duplicate → "Engineering Reorg v3" (stakeholder feedback incorporated)

---

## Best Practices

1. **Name scenarios clearly from the start** - Don't leave as "Untitled"
2. **Use tags consistently** - Establish tag naming conventions
3. **Duplicate before major changes** - Create v2 instead of destroying v1
4. **Archive implemented scenarios** - Don't delete historical records
5. **Export change logs regularly** - Backup your work
6. **Check symbols before sharing** - Ensure they accurately reflect changes
7. **Delete only test scenarios** - Archive everything else
8. **Use versioning for alternatives** - Compare multiple approaches

---

## Troubleshooting

**Problem:** Can't rename scenario.
- **Solution:** You may not be the owner. Only owners can rename. Ask owner or admin.

**Problem:** Duplicate button not working.
- **Solution:** Check permissions. May require edit or admin access.

**Problem:** Can't see archived scenarios.
- **Solution:** Toggle "Show Archived" filter on homepage.

**Problem:** Tags not appearing on scenario.
- **Solution:** Ensure tag was saved. Refresh page.

**Problem:** Deleted scenario by accident.
- **Solution:** Contact admin immediately. May be able to restore from backup (not guaranteed).

**Problem:** Symbols not showing on position cards.
- **Solution:** Refresh page. Check if symbols are toggled off in view settings.

---

## Next Steps

Now that you understand scenario management:
- Organize your existing scenarios with clear names and tags
- Duplicate your next scenario to test alternatives
- Archive completed scenarios for historical reference
- Practice exporting change logs for stakeholder reports
- Learn [Scenario Approvals](approvals.md) to formalize workflow after organizing scenarios



