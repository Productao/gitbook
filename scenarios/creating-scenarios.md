---
description: How to create new scenarios
hidden: false
---

# Creating Scenarios

Learn how to create scenarios step-by-step. This guide covers all three scenario types, naming conventions, and how to set up your scenario for success.

## Before You Start

**Prerequisites:**
- You need edit access to create scenarios (not just view access)
- Identify what you want to model (reorganization, budget cut, expansion, etc.)
- Know which part of the org you want to include (full org vs specific department)
- Have a clear name in mind (more on naming below)

**Best practice:** Before creating a scenario, explore Main Org first to understand the current state. You can't model changes effectively if you don't know what you're changing from.

---

## Three Ways to Create Scenarios

### Method 1: From Homepage

1. Click the **+** icon in the bottom left corner of the homepage
2. Or click **"Create Scenario"** button on homepage
3. Scenario creation dialog opens

### Method 2: From Main Org

1. Open **Main Org** (keyboard shortcut: **1**)
2. Click **"Create Scenario"** button in top right
3. Scenario creation dialog opens

### Method 3: From Scenario List

1. Go to homepage or scenarios list
2. Click **"New Scenario"** or **+** icon
3. Scenario creation dialog opens

---

## Step-by-Step: Creating a Scenario

### Step 1: Choose Scenario Type

You'll see three options:

#### Option 1: Full Org (Select Everyone)

**What it does:** Duplicates your entire accessible org chart into a new scenario.

**When to choose this:**
- Company-wide reorganizations
- Annual planning affecting multiple departments
- Strategic planning requiring full context
- Cross-functional changes

**Considerations:**
- Slower with large orgs (5000+ people)
- Can be overwhelming to navigate
- Best for experienced users

---

#### Option 2: Partial Org (Filtered Selection) ⭐ RECOMMENDED

**What it does:** Creates a scenario for a specific subset of your organization.

**When to choose this:**
- Department reorganizations
- Team restructuring
- Focused planning
- Faster performance needed
- **Most common choice**

**How to select your subset:**

1. Click **"Partial Org"** or **"Filtered Selection"**
2. Choose your selection method:

**Method A: Select by Manager**
- Pick a manager from the dropdown
- Their entire org (direct + indirect reports) is included
- Manager and everyone below them
- Most common approach

**Method B: Filter Selection**
- Apply filters (Department, Location, etc.)
- Preview which positions will be included
- Option to include "Manager Filtering" (shows reporting chain above selected positions)
- Verify scope before proceeding

**Pro tip:** Use "Manager Filtering" option to include the reporting chain above your selected positions. This preserves context and lets you see where your subset fits in the larger org.

**Considerations:**
- Can't move positions outside the scoped area
- Don't see positions outside your selection
- May miss cross-department dependencies

---

#### Option 3: New Org (Blank Scenario)

**What it does:** Creates an empty canvas for building an org from scratch.

**When to choose this:**
- New department creation
- Greenfield organization design
- Zero-based budgeting
- Starting completely fresh

**Considerations:**
- Time-consuming (add every position manually)
- No baseline to compare against
- Easy to forget roles
- Best for experienced scenario users

---

### Step 2: Name Your Scenario

**Naming conventions matter!** Good names help you (and others) understand what the scenario is for.

#### Good Naming Patterns

**Format:** `[Department/Area] [Purpose] [Time Period]`

**Examples:**
- "Engineering Q2 2026 Expansion"
- "Commercial NA Reorg v2"
- "Global Sales Budget Cut 10%"
- "Product Team Restructure - Option A"
- "Finance 2026 Annual Plan"

#### Bad Naming Patterns

❌ "Scenario 1" - Not descriptive
❌ "Test" - What are you testing?
❌ "New" - New what?
❌ "Bob's scenario" - What's the purpose?
❌ "Draft" - Draft of what?

#### Naming Best Practices

1. **Be specific** - Say what you're modeling
2. **Include timing** - Q1 2026, FY27, etc.
3. **Note versions** - v1, v2, Option A, Option B
4. **Include context** - Department, initiative, purpose
5. **Keep it concise** - Under 50 characters if possible

---

### Step 3: Set Budget (Optional)

**What it does:** Sets a target budget for the scenario. Agentnoon will show whether you're over/under budget as you make changes.

**When to use:**
- Budget-constrained planning
- Cost reduction exercises
- When you have a specific target to hit

**How to set:**
1. Check "Set a budget" checkbox
2. Enter target amount (e.g., $5,000,000)
3. As you make changes, Change Tracker shows budget vs actual

**When to skip:**
- Exploratory planning without budget constraints
- Reorganizations focused on structure, not cost
- Early ideation before budget discussions

---

### Step 4: Set Effective Date (Optional)

**What it does:** Sets a target implementation date for the scenario.

**When to use:**
- Planning changes for a specific quarter/date
- Phased implementation
- Time-sensitive reorganizations

**How to set:**
1. Check "Set effective date" checkbox
2. Select date (e.g., April 1, 2026)

**When to skip:**
- General exploration
- No specific timeline yet

---

### Step 5: Add Description (Optional but Recommended)

**What it does:** Adds context about the scenario purpose and goals.

**What to include:**
- Why you're creating this scenario
- What problem you're solving
- Key assumptions or constraints
- Expected outcomes

**Example:**
"Modeling the reorganization of the Engineering team to better align with product priorities. Moving iOS and Android teams under a single mobile leader. Target headcount: 85 engineers. Target date: Q2 2026."

---

### Step 6: Review and Create

1. Review your selections:
   - Scenario type (Full/Partial/New)
   - Name
   - Budget (if set)
   - Effective date (if set)
   - Description
2. Click **"Next"** or **"Create Scenario"**

**What happens next:**
- Agentnoon creates the scenario (takes 5-30 seconds depending on size)
- You're taken to the scenario org chart
- You can start making changes immediately

---

## After Creating a Scenario

### Verify Your Scope

1. **Check the scenario name** appears in top-left corner
2. **Verify you're IN the scenario** (not Main Org)
3. **Navigate the org chart** to confirm the right positions are included
4. **Check headcount/cost** in the top summary bar

### Start Making Changes

Now you can:
- Add positions
- Edit positions
- Move positions to different managers
- Close positions (RIF)
- Reorganize teams

See [Making Position Changes](making-position-changes.md) for detailed instructions.

---

## Switching Between Scenarios

**To switch scenarios:**
1. Click the **scenario name dropdown** in top-left corner
2. Select a different scenario from the list
3. Or select "Main Org" (marked with view icon) to return to current state

**Pro tip:** Open multiple browser tabs to compare scenarios side-by-side.

---

## Common Scenarios to Create

### Department Reorganization

**Type:** Partial Org
**Scope:** Select department leader and their org
**Name:** "[Department] [Quarter] Reorganization"
**Example:** "Engineering Q2 2026 Reorg"

### Annual Hiring Plan

**Type:** Full Org or Partial Org
**Scope:** All areas adding headcount
**Name:** "[Year] Annual Hiring Plan"
**Budget:** Set to allocated hiring budget
**Example:** "2026 Annual Hiring Plan"

### Budget Cut Scenario

**Type:** Partial Org (affected departments)
**Scope:** Areas being cut
**Name:** "[Area] Budget Cut [Percentage]"
**Budget:** Set to reduced budget target
**Example:** "Sales & Marketing Budget Cut 15%"

### Team Expansion

**Type:** Partial Org
**Scope:** Team being expanded
**Name:** "[Team] [Quarter] Expansion"
**Example:** "Product Team Q3 Growth"

### Merger Integration

**Type:** Full Org
**Scope:** Both organizations
**Name:** "[Company A] + [Company B] Integration - [Option]"
**Example:** "Acme + Widget Co Integration - Option A"

---

## Scenario Creation Best Practices

1. **Start with Partial Org** - Faster and more focused for most use cases
2. **Name scenarios immediately** - Don't leave as "Untitled Scenario"
3. **Include manager reporting chains** - Use Manager Filtering when creating Partial Org scenarios
4. **Set budgets for cost-constrained planning** - Helps keep you on track
5. **Add descriptions** - Future you (and others) will thank you
6. **Create multiple versions** - Make Option A, Option B, Option C to compare
7. **Don't create too many scenarios** - Keep your list manageable (archive old ones)

---

## Troubleshooting

**Problem:** Scenario creation is taking too long.
- **Solution:** You may be creating a Full Org scenario with 5000+ people. Consider Partial Org instead.

**Problem:** I can't see all the positions I expected.
- **Solution:** Check your filter or manager selection. You may have selected too narrow a scope.

**Problem:** I see positions I don't want to include.
- **Solution:** Adjust your filters or select a more specific manager for Partial Org.

**Problem:** I accidentally created the wrong type.
- **Solution:** Delete the scenario and start over. Can't convert between types after creation.

**Problem:** My scenario name is too long.
- **Solution:** Edit the scenario name (if available) or delete and recreate with shorter name.

---

## Next Steps

Now that you've created a scenario:
- Learn [how to make position changes](making-position-changes.md)
- Understand [scenario basics](using-scenarios-basics.md)
- Explore [bulk operations](bulk-operations.md) for faster editing
- See [Change Tracker](tracking-analysis.md) to monitor impact
- Try [comparing scenarios](comparisons.md) to evaluate options

## Visual Guide

> **[Screenshot placeholder: Create New Scenario button and modal]**

> **[Screenshot placeholder: Scenario type selection (Full Org, Partial Org, New Org)]**

> **[Screenshot placeholder: Newly created scenario in org chart view]**
