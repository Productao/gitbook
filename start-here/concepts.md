---
description: Essential concepts for understanding Agentnoon
hidden: false
---

# Key Concepts

These core concepts will help you navigate Agentnoon and understand how workforce planning works in the platform.

---

## Positions vs People

**Position:** A job role in your organization, whether filled or open. Positions have attributes like title, department, salary range, and reporting structure.

**Person/Employee:** The individual assigned to a position. One person can only fill one position at a time.

**Key insight:** Agentnoon is primarily position-based. You plan with positions first, then assign people to them. This allows you to model future org structures even before hiring.

> **[Screenshot placeholder: Position card showing open position vs filled position with employee]**

---

## Main Org vs Scenarios

### Main Org

Your **current state** organization as it exists today. This is the source of truth imported from your HRIS or data file.

**Characteristics:**
- View-only (read-only)
- Reflects real-time data
- Updated via data imports
- Cannot be edited directly

**Learn more:** [Key Concepts for Main Org](key-concepts-main-org.md)

### Scenarios

**Future state** versions of your organization where you model changes. Think of scenarios as sandboxes where you can experiment with org design.

**Characteristics:**
- Editable copies of the Main Org
- Support "what-if" planning
- Track all changes
- Can be compared, shared, and approved

**Learn more:** [Key Concepts for Scenarios](key-concepts-scenarios.md)

---

## Views: Org Chart vs Directory

### Org Chart View

Visual, hierarchical tree showing reporting relationships.

**Best for:** Understanding structure, visualizing chains, dragging positions

### Directory View

Table/spreadsheet view of all positions with sortable columns.

**Best for:** Analyzing data in bulk, filtering, exporting, bulk editing

**Pro tip:** Switch between views with keyboard shortcuts (3 for Org Chart, 5 for Directory).

> **[Screenshot placeholder: Side-by-side comparison of Org Chart view vs Directory view]**

---

## Cards

Visual containers displaying position or employee information.

**What's on a card:**
- Name and Title
- Department
- Salary
- Direct reports count
- Other configured attributes

**Card interactions:**
- Click to open detail panel
- Hover to see quick info
- Drag to move to new manager (in scenarios)
- Color-coded by change type

> **[Screenshot placeholder: Example position card showing name, title, department, salary, and other attributes]**

---

## Attributes vs Fields

**Attributes:** Data points about positions or people (e.g., Department, Location, Salary, Title).

**Fields:** How attributes are organized and displayed in the UI.

**System attributes** (calculated by Agentnoon):
- Span of Control
- Layer
- Total Org Size
- Cost Impact

**Custom attributes** (defined by your admin):
- Business Unit, Cost Center, Employee Type, Pay Grade, etc.

**Learn more:** [Fields and Attributes](fields-and-attributes.md)

---

## Spans and Layers

### Span of Control (SOC)

The number of direct reports a manager has.

**Healthy ranges:**
- Individual Contributors: 0 direct reports
- First-Line Managers: 5-10 direct reports
- Mid-Level Managers: 5-8 direct reports
- Executives: 5-10 direct reports

> **[Screenshot placeholder: Org chart with span of control highlighting]**

### Layers

The number of management levels between an employee and the CEO.

**Example:**
- CEO: Layer 0
- VP: Layer 1
- Director: Layer 2
- Manager: Layer 3
- IC: Layer 4

**Industry best practice:** 4-7 layers for most companies

---

## Permissions & Access Control

### Access Groups
Define who can see what data based on department, location, or custom rules.

### Permission Levels
- **Viewer:** Can see data, cannot edit
- **Planner:** Can create and edit scenarios
- **Approver:** Can approve scenario changes
- **Admin:** Full system access, configuration

---

## Next Steps

Now that you understand core concepts:

- **Explore Main Org:** View your current organization
- **Create your first scenario:** Model a simple change
- **Learn module-specific concepts:**
  - [Key Concepts for Main Org](key-concepts-main-org.md)
  - [Key Concepts for Scenarios](key-concepts-scenarios.md)

**Other helpful resources:**
- [Parts of the Application](parts-of-application.md) - How modules work together
- [Scenarios Fundamentals](scenarios-fundamentals.md) - Deep dive on scenario planning
- [Fields and Attributes](fields-and-attributes.md) - Understanding your data
