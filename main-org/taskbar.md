---
description: Actions available in the Main Org taskbar
icon: wrench
hidden: false
---

# Taskbar (Main Org)

The taskbar at the top of Main Org provides quick access to view controls and analysis tools. Understanding what's available - and what's NOT available - in Main Org will help you work more efficiently.

## Main Org Taskbar Overview

The taskbar is your control center for customizing how you view and analyze your organization. All actions in Main Org are **view-only** - you cannot edit positions, move people, or make organizational changes here.

---

## Available Actions in Main Org

### 1. Search

**Icon:** 🔍 Magnifying glass

**What it does:** Find employees or positions by name or job title.

**How to use:**
- Click the search icon
- Type a name or title
- Select from results to navigate to that position

---

### 2. Filter

**Icon:** Funnel/filter symbol

**What it does:** Show only positions matching specific criteria.

**How to use:**
- Click the filter icon
- Select attribute (Department, Location, Pay Grade, etc.)
- Choose values to include
- Toggle Manager Filtering to preserve hierarchy
- Click Apply

**Pro tip:** Manager Filtering is recommended to keep org structure intact.

---

### 3. Tree View

**Icon:** List with indentation

**What it does:** Display org structure as a hierarchical list.

**How to use:**
- Click the tree view icon
- Browse the indented list
- Click names to navigate in the org chart

**When to use:** Quickly browse deep hierarchies without expanding cards.

---

### 4. Highlight

**Icon:** Paint palette or color symbol

**What it does:** Color-code cards by any attribute.

**How to use:**
- Click the highlight icon
- Select attribute (Department, Work City, Pay Grade, etc.)
- Cards color automatically
- Toggle fill color vs outline color
- Show legend to see color meanings

**Pro tip:** Use both fill and outline colors to highlight two attributes at once.

---

### 5. Card Content (Display Settings)

**Icon:** Gear or settings symbol

**What it does:** Control what fields appear on each card.

**How to use:**
- Click the card content icon
- Check/uncheck fields to show/hide
- Drag to reorder fields
- Changes apply immediately

**Available fields:**
- Standard fields (Name, Title, Department)
- Custom fields configured by your admin
- Calculated "FX" fields (SOC, Total Org Size, Layer)

---

### 6. Spotlight

**Icon:** Spotlight or target symbol

**What it does:** Highlight positions matching criteria while graying out others.

**How to use:**
- Click the spotlight icon
- Choose a rule (e.g., "Average Immediate SOC")
- Set range (e.g., "1-2")
- Click Apply

**Common uses:**
- Find managers with low span of control
- Identify high spans
- Locate positions by pay grade or level

---

### 7. Presets (Saved Views)

**Icon:** Bookmark or star symbol

**What it does:** Save and recall filter/highlight/display configurations.

**How to use:**
- Configure your view
- Click presets icon
- Click "Save Current View"
- Name your preset
- Click Save

**To use a saved preset:**
- Click presets icon
- Select from your saved views

**Sharing:** Other users can access your presets (based on permissions).

---

### 8. Export

**Icon:** Download or export symbol

**What it does:** Export org charts and data in multiple formats.

**Export options:**

**Org Chart Exports:**
- **JPEG** - Screenshot of current view
- **PowerPoint** - One slide per manager

**Data Exports:**
- **CSV** - Raw data table
- **Template Builder** - Custom column configuration (admin only)

**How to export:**
- Click export icon
- Choose format
- Download file

---

### 9. Layout

**Icon:** Grid or layout symbol

**What it does:** Change how the org chart displays.

**Layout options:**
- **Vertical** - Top-down (traditional)
- **Horizontal** - Left-right
- **Compact** - Two columns per level

**Additional controls:**
- Expand/collapse levels (show 1, 2, or 3 levels)
- Fit to screen
- Zoom in/out

---

### 10. Directory View Toggle

**Icon:** Table or grid symbol

**What it does:** Switch between org chart and table view.

**How to use:**
- Click the directory/table icon
- View switches to spreadsheet-style table
- All positions shown in rows
- Sort and filter by columns

**When to use:** When you need to analyze data in table format or export lists.

---

## Actions NOT Available in Main Org

Because Main Org is view-only, these actions are **disabled**:

- **Add Position** - Cannot create new positions
- **Edit Position** - Cannot modify titles, salaries, departments, etc.
- **Move Position** - Cannot change reporting relationships
- **Close Position** - Cannot remove or RIF positions
- **Assign Employee** - Cannot attach people to positions
- **Change Manager** - Cannot reorganize teams
- **Bulk Edit** - Cannot modify multiple positions at once

**To make changes:** Create a Scenario instead. Scenarios are fully editable copies where you can model any organizational changes.

---

## Main Org vs Scenario Taskbar

| Feature | Main Org | Scenarios |
|---------|----------|-----------|
| Search | ✅ Yes | ✅ Yes |
| Filter | ✅ Yes | ✅ Yes |
| Highlight | ✅ Yes | ✅ Yes |
| Card Content | ✅ Yes | ✅ Yes |
| Spotlight | ✅ Yes | ✅ Yes |
| Export | ✅ Yes | ✅ Yes |
| Layout | ✅ Yes | ✅ Yes |
| **Add Position** | ❌ No | ✅ Yes |
| **Edit Position** | ❌ No | ✅ Yes |
| **Move Position** | ❌ No | ✅ Yes |
| **Close Position** | ❌ No | ✅ Yes |
| **Bulk Operations** | ❌ No | ✅ Yes |
| **Change Tracker** | ❌ No | ✅ Yes |
| **Activity Log** | ❌ No | ✅ Yes |
| **Comments** | ❌ No | ✅ Yes |

---

## Keyboard Shortcuts

Speed up your workflow with these shortcuts:

- **1** - Jump to Main Org
- **2** - Jump to Scenarios
- **3** - Jump to Forecast
- **4** - Jump to Workforce Hub
- **5** - Jump to Directory
- **Cmd/Ctrl + F** - Open search
- **Esc** - Close panels or dialogs

---

## Common Workflows Using the Taskbar

### Analyzing Span of Control
1. Click **Spotlight**
2. Select "Average Immediate SOC"
3. Set range "1-2"
4. Click **Apply**
5. Review highlighted positions

### Creating a Department View
1. Click **Filter** → Department
2. Enable Manager Filtering
3. Click **Apply**
4. Click **Highlight** → Location
5. Click **Presets** → Save Current View

### Exporting for Stakeholders
1. Configure filters and highlights
2. Click **Export**
3. Choose PowerPoint
4. Download and share

### Exploring a Manager's Team
1. Click **Search**
2. Type manager's name
3. Click their card
4. Use **Layout** → Expand to level 3
5. View their full org

---

## Best Practices

1. **Use presets for recurring views** - Don't reconfigure the same filters repeatedly
2. **Clear filters between analyses** - Filters carry over to other modules
3. **Combine tools** - Use Highlight + Spotlight together for powerful insights
4. **Save exports as templates** - Ask admins to configure standard export formats
5. **Remember Main Org is view-only** - Create a Scenario to model changes

---

## Troubleshooting

**Problem:** I don't see an action I'm looking for.
- **Solution:** You're in Main Org (view-only). Create a Scenario for editing actions.

**Problem:** My filters aren't working.
- **Solution:** Check if you have Manager Filtering enabled. Try toggling it on/off.

**Problem:** Data looks incomplete.
- **Solution:** Check active filters. Click Filter → Clear All to reset.

**Problem:** I can't find a specific person.
- **Solution:** Verify they're in your access scope. Check with admin if needed.

---

## Next Steps

Now that you understand the Main Org taskbar:
- Learn advanced [Navigation techniques](navigation.md)
- Switch to [Directory View](directory-view.md) for table analysis
- Explore [Org Metrics & Insights](metrics-insights.md)
- Create a [Scenario](../scenarios/creating-scenarios.md) to model changes
- Compare [Scenario Taskbar](../scenarios/taskbar.md) to see editing features
