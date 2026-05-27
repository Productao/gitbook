---
description: How to navigate and explore the org chart, and available toolbar tools
icon: route
---

# Orientation & Navigation

The left toolbar provides all navigation and analysis tools in Main Org. All actions are **view-only** — to make changes to positions, create a Scenario.

<figure><img src="../.gitbook/assets/Screenshot 2026-02-27 at 2.08.06 AM.png" alt=""><figcaption></figcaption></figure>

## Toolbar Tools

#### **Search (🔍)**

Find employees or positions by name or job title.&#x20;

* Results navigate the org chart to that position.
* Works across your accessible scope.
* Shortcut: Cmd/Ctrl+K or `/`.

#### **Filter**

Show only positions matching specific criteria (for example, Department, Location, Pay Grade, or custom fields).

Two filter modes are available:

1. Standard Filtering — Shows only matching positions and may break visual hierarchy.
2. Manager Filtering (reccomended) — Preserves reporting context by keeping managers visible above matching positions.

Filters persist across Org Chart, Directory, and Forecast views.

Use **Clear All** to reset filters.

#### **Tree View**

Displays the organization as an indented list. Use Tree View to quickly navigate deep hierarchies without expanding cards manually.

#### **Highlight**

Color-code positions by any attribute.

* Use **Fill Color** to apply one attribute.
* Use **Outline Color** to apply a second attribute.
* Toggle the legend to see what each color represents.

Highlighting does not change data — it is a visual tool for analysis.

#### **Card Content**

Control which fields appear on position cards.

* Add standard, custom or calculated fields
* Drag and drop to reorder fields.
* Changes apply immeditely.&#x20;

:bulb: Keep cards minimal — 3–5 fields for readability; add more only for specific analysis.

#### **Spotlight**

Dim non-matching positions to focus on specific criteria.

* Apply preconfigured rules (for example, span of control ranges)
* Spotlight by any available attribute, including custom fields
* Matching positions are highlighted; others appear dimmed

Spotlight helps identify patterns within the organization.

#### **Presets (Saved Views)**

Save your current configuration of: Filters, Highlights and Card Content. Saved views can be reloaded later and may be available to other users based on permissions.

<figure><img src="../.gitbook/assets/Screenshot 2026-02-24 at 2.28.32 PM.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 2026-02-24 at 2.29.09 PM.png" alt=""><figcaption></figcaption></figure>

#### **Export**

Export your current view as:

* JPEG (images)
* PowerPoint (one slide per manager, configurable depth)
* CSV (all data, respects active filters and visible columns
* Template builder (admin only)

#### **Layout**

Switch between layout options:

* Vertical
* Horizontal
* Compact

Adjust how many levels are expanded (1–3 levels). Use zoom and pan controls to navigate large structures.

**Directory Toggle**

Switch to Directory view to analyze data in a table format.

#### Keyboard Shortcuts

`1` = Main Or

`5` = Directory

`/` or Cmd/Ctrl+K = Search

Esc = Close panels

#### Available Actions: Main Org vs. Scenarios

| Tool                                                               | Main Org | Scenarios |
| ------------------------------------------------------------------ | -------- | --------- |
| Search, Filter, Highlight, Spotlight, Card Content, Export, Layout | ✅        | ✅         |
| Add/Edit/Move/Close positions                                      | ❌        | ✅         |
| Bulk Operations                                                    | ❌        | ✅         |
| OpEx Panel                                                         | ❌        | ✅         |
| Comments                                                           | ❌        | ✅         |
| Approvals                                                          | ❌        | ✅         |

## Related Articles

* [Directory View](directory-view.md)
* [Org Metrics & Insights](metrics-insights.md)
* [Creating a Scenario](../scenarios/creating-scenarios.md)
