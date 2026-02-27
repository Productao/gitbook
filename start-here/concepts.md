---
description: Essential concepts for understanding Agentnoon
icon: circle-exclamation
---

# Key Concepts

These core concepts will help you navigate Agentnoon and understand how workforce planning works within the platform.

***

## Positions vs People

#### **Position**

A job role in your organization, whether filled or open. Positions include attributes such as title, department, salary range, and reporting structure.

#### **People (Employee)**

The individual assigned to a position. One person can only fill one position at a time.

:bulb: Agentnoon is primarily position-based. You plan by creating and modifying positions first, then assigning people to them. This allows you to model future organizational structures before roles are filled.

<figure><img src="../.gitbook/assets/Screenshot 2026-02-26 at 9.33.39 AM.png" alt=""><figcaption></figcaption></figure>

***

## Main Org vs Scenarios

#### **Main Org**

Your **current-state** organization as it exists today.

* View-only (cannot be edited directly)
* Reflects real-time or imported data
* Updated through data sync
* Serves as the baseline for scenario planning

**Learn more:** [Key Concepts for Main Org](/broken/pages/sdPpZlvz7HLxJDQxhUFd)

#### **Scenarios**

Editable copies of Main Org used for planning **future** changes.

* Support what-if modeling
* Track additions, reductions, and modifications
* Can be compared, shared, and submitted for approval

Scenarios are isolated from Main Org until changes are implemented externally and data is refreshed.

**Learn more:** [Key Concepts for Scenarios](../scenarios/key-concepts-scenarios.md)

***

## Views: Org Chart vs Directory

#### Org Chart View

A visual, hierarchical view that displays reporting relationships.

Best used for:

* Understanding organizational structure
* Visualizing reporting lines
* Drag-and-drop changes in scenarios

#### Directory View

A table-style view of all positions and employees with sortable columns.

Best used for:

* Bulk analysis
* Filtering and sorting data
* Exporting structured reports

:bulb: You can switch between Org Chart and Directory views at any time with keyboard shortcuts (3 for Org Chart, 5 for Directory).

<figure><img src="../.gitbook/assets/Screenshot 2026-02-26 at 9.38.48 AM.png" alt=""><figcaption></figcaption></figure>

***

## Cards

In Org Chart view, each position appears as a card.

Cards display key information such as:

* Name and title
* Department
* Direct reports count
* Additional selected attributes

Card content can be configured to display different fields, including calculated metrics.

**Card interactions:**

* Click to open detail panel
* Hover to see quick info
* Drag to move to new manager (in scenarios)
* Color-coded indicators show change type (in scenarios)

<figure><img src="../.gitbook/assets/Screenshot 2026-02-26 at 9.57.10 AM.png" alt="" width="292"><figcaption></figcaption></figure>

***

## Attributes vs Fields

#### **Attributes**

&#x20;Data points about positions or people (for example, Department, Location, Salary, Title).

#### **Fields**

How attributes are organized and displayed in the platform.

Attributes appear throughout the system — on cards, in the Directory, in analytics charts, in filters, and in exports.&#x20;

There are two types of attributes:

1.  **System attributes** (FX)\
    Calculated automatically by the platform. These update automatically as the organization changes. Examples include:

    * Span of Control
    * Layer
    * Total Org Size
    * Cost Impact


2.  **Custom attributes**&#x20;

    Defined by your administrator to reflect your organization’s structure. Custom attributes can be used in filters, highlights, analytics, and exports. Examples may include:

    * Business Unit
    * Cost Center
    * Employee Type
    * Pay Grade

**Learn more:** [Fields and Attributes](fields-and-attributes.md)

***

## Spans and Layers

#### Span of Control (SOC)

Span of Control helps evaluate management distribution and organizational balance. It is calculated automatically and reflects the number of positions that report directly to a given position.

Common ranges:

* **Individual Contributors:** 0 direct reports
* **First-Line Managers:** 5–10 direct reports
* **Mid-Level Managers:** 5–8 direct reports
* **Executives:** 5–10 direct reports

<figure><img src="../.gitbook/assets/Screenshot 2026-02-26 at 9.59.43 AM.png" alt=""><figcaption></figcaption></figure>

#### Layers

Layers help define organizational depth and represents the number of management levels between a position and the CEO. Industry best practice typically ranges from 4–7 layers for most companies, depending on size and complexity.

Example:

* CEO: Layer 0
* VP: Layer 1
* Director: Layer 2
* Manager: Layer 3
* Individual Contributor: Layer 4

***

## Permissions & Access Control

#### **Access Groups**

Access Groups define who can see what data in the platform and can be scoped based on department, location, or other defined attributes.

Permission Levels:

* Viewer: Can see data, cannot edit
* Planner: Can create and edit scenarios
* Approver: Can approve scenario changes
* Admin: Full system access, configuration

Permissions are configured by administrators.

**Learn more:** [Access Control](../access-control/overview.md)

***

## Deep Dives

* [Key Concepts for Main Org](/broken/pages/sdPpZlvz7HLxJDQxhUFd) — Data sync, read-only nature, baseline for scenarios
* [Key Concepts for Scenarios](../scenarios/key-concepts-scenarios.md) — Change types, OpEx Panel, approvals, comparisons
