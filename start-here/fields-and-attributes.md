---
description: Understanding data structure and custom fields
hidden: false
---

# Fields and Attributes

Fields (also called attributes) are the data points that define your organization in Agentnoon. Understanding how they work will help you customize what information you track and how it appears throughout the application.

## What Are Fields?

Fields are individual data points used to capture and store information about your positions and people. Examples include:

- Job Title
- Department
- Work Location
- Pay Grade
- Salary
- Start Date
- Manager Name

Fields appear everywhere in Agentnoon: on cards, in the directory, in analytics charts, and in exports.

## Two Types of Fields

> **[Screenshot placeholder: Fields and Attributes settings showing position fields and people fields grouped separately]**

### Position Fields

**Position fields** are tied to roles in your org structure and exist independently of people:

- Job Title
- Department
- Base Salary Range
- Pay Grade
- Location
- Job Function
- Reports To

**Why it matters:** Position fields persist even when a role is vacant. This allows you to plan for unfilled positions and budget for future hires.

### People Fields

**People fields** are tied to individual employees:

- Employee Name
- Employee ID
- Start Date
- Email Address
- Visa Status
- Performance Rating
- Preferred Name

**Why it matters:** People fields disappear when someone leaves the organization. This separation lets you manage roles and people independently for better workforce planning.

## Groups: Organizing Related Fields

Fields are organized into **groups** for easier management:

- **People Groups** - Fields about individuals (contact info, demographics, HR data)
- **Position Groups** - Fields about roles (job details, compensation, location)

Groups appear as sections in forms, tables, and exports, making your data easier to navigate.

## Calculated Fields (FX Fields)

Some fields are automatically calculated by Agentnoon and marked with "FX":

- **Span of Control** - Number of direct reports
- **Total Organization Size** - Everyone under a manager (direct + indirect)
- **Layer** - Distance from CEO
- **Average SOC** - Average span across the organization

These fields update automatically as your org structure changes, providing instant insights without manual data entry.

## Customizing Field Display

### Card Content

Control which fields appear on org chart cards:

1. Click **Card Content** in the toolbar
2. Select fields to display (e.g., Department, Work City, Pay Grade)
3. Reorder fields by dragging
4. Changes apply immediately

**Pro tip:** Keep card content minimal (3-5 fields) for readability. Add more fields only when needed for specific analysis.

### Directory Columns

Customize table view columns in Directory:

1. Go to **Directory** module
2. Click column settings
3. Add/remove columns
4. Sort and filter by any field
5. Save your preferred view

## Field Configuration (Admin)

Admins can configure fields to match your organization's needs:

- **Data types** - Text, number, date, dropdown, user reference
- **Dropdown options** - Define choices for fields like Department or Job Family
- **Visibility** - Public (all users) or restricted (specific roles)
- **Mandatory settings** - Require certain fields for data completeness
- **Field ordering** - Control how fields appear in lists and forms

For details on admin configuration, see [Fields and Attributes Management](../admin/fields-management.md).

## Standard Fields

Every Agentnoon instance includes standard fields:

**Position Fields:**
- Job Title
- Department
- Manager (Reports To)
- Location

**People Fields:**
- Name
- Employee ID
- Start Date
- Email

Your admin can add custom fields specific to your organization's needs.

## Using Fields in Analysis

Fields power all analytics in Agentnoon:

- **Filtering** - Show only positions matching specific field values (e.g., "Department = Engineering")
- **Highlighting** - Color-code cards by field (e.g., highlight by Work Country)
- **Spotlight** - Find positions where fields match criteria (e.g., "SOC between 1-2")
- **Charts** - Break down data by any field (e.g., headcount by Department and Layer)
- **Exports** - Include any field in CSV/Excel exports

## Best Practices

1. **Keep field names clear and consistent** - Use "Work Location" everywhere, not "Office" in some places and "Location" in others
2. **Use dropdown fields for standardized data** - Prevents typos and inconsistencies (e.g., "NYC" vs "New York City")
3. **Separate position and people data** - Put compensation on positions, performance ratings on people
4. **Don't over-customize** - Start with standard fields, add custom ones only when truly needed
5. **Use calculated fields** - Let Agentnoon compute SOC, layers, and org size automatically

## Next Steps

Now that you understand fields and attributes:
- Learn how to use them in [Scenarios](scenarios-fundamentals.md) to model changes
- Explore [Workforce Hub Fundamentals](workforce-hub-fundamentals.md) to see how fields power analytics
- See [Fields and Attributes Management](../admin/fields-management.md) if you're an admin configuring fields
