---
description: Understanding position and employee cards
hidden: false
---

# Cards

Cards are the fundamental building blocks of your org chart in Agentnoon. Each card represents either a **position** or an **employee** in your organization, displaying key information at a glance.

## What Are Cards?

When you open the org chart in Agentnoon, you'll immediately see cards arranged hierarchically. Each card is a visual representation containing:

- **Name** (employee or position title)
- **Job title** or role
- **Department** or team
- **Custom attributes** you've configured (location, salary, pay grade, etc.)

## Card Anatomy

Every card displays:

1. **Header** - Name and/or position title
2. **Subtitle** - Job function or department
3. **Custom fields** - Any attributes you've added via Card Content settings
4. **Visual indicators**:
   - 📎 Paperclip icon = Position has an employee assigned
   - Direct reports count (e.g., "10 direct reports")
   - Total org size (e.g., "612 people under them")

## Card Content Customization

You can customize what information appears on cards:

1. Click the **Card Content** button in the toolbar
2. Select from available attributes:
   - Work City
   - Work Country
   - Pay Grade
   - Department
   - Span of Control (calculated automatically by Agentnoon)
   - Total Organization Size
   - Any custom fields your admin has configured
3. Add or remove fields as needed
4. Changes apply immediately to all visible cards

**Pro tip:** Attributes with "FX" labels are automatically calculated by Agentnoon and provide instant insights without manual data entry.

## Highlighting Cards

Use highlighting to visually distinguish cards by specific attributes:

1. Click the **Highlight** button in the toolbar
2. Select an attribute (e.g., Work Country, Department, Pay Grade)
3. Cards automatically color-code based on their values
4. A legend appears showing what each color represents

**Example:** Highlighting by "Work City" will show different colors for New York, London, Tokyo, etc., making it easy to see geographic distribution at a glance.

## Interacting with Cards

In **Main Org** (view-only):
- Click to expand/collapse reporting lines
- Hover to see additional details
- Use search to find specific cards

In **Scenarios** (editable):
- Hover over a card to see action buttons:
  - ← → Move card left/right (change reporting order)
  - ➕ Add position below this card
  - ✏️ Edit position details
  - 📎 Assign employee to position
  - 📋 Duplicate position
  - ❌ Close position (RIF - Reduction in Force)
- Click and drag cards to move them
- Select multiple cards for bulk actions

## Position vs Employee Cards

**Position cards** represent roles in your org structure:
- May or may not have an employee assigned
- Show job title and organizational placement
- Persist even when vacant

**Employee cards** represent actual people:
- Always attached to a position (shown with 📎 paperclip icon)
- Display person's name and role
- Can be moved between positions in scenarios

## Next Steps

Now that you understand cards, learn how to:
- Use [Spotlight](../main-org/navigation.md#spotlight) to find cards matching specific criteria
- Create [Scenarios](scenarios-fundamentals.md) to model organizational changes
- Customize [Fields and Attributes](fields-and-attributes.md) to track what matters to your organization
