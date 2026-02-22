---
description: Common scenario planning questions
hidden: false
---

# Scenarios FAQs

Answers to common questions about creating, managing, and working with scenarios. Learn how to model organizational changes, collaborate with stakeholders, and submit scenarios for approval.

---

## Understanding Scenarios

### What's the difference between scenario types (Full Org, Partial Org, New Org)?
**Answer:** Full Org copies your entire organization (best for company-wide planning). Partial Org copies a specific department or subset (faster, most common choice). New Org starts with a blank canvas (for building new departments from scratch).

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

### When should I use Partial Org instead of Full Org?
**Answer:** Use Partial Org for department reorganizations, team restructuring, or focused planning. It's faster to create and work with, keeps you focused on the relevant area, and is the most commonly used scenario type.

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

### Can I make changes to Main Org directly?
**Answer:** No. Main Org is view-only—it reflects your current organizational data from your HRIS. To model changes, create a scenario. Scenarios are sandboxes where you can freely add, edit, move, or close positions without affecting Main Org.

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### What changes can I make in a scenario?
**Answer:** You can add new positions, close existing positions (RIF), move people to different managers, edit position details (title, salary, department), reorganize entire departments, create dotted-line reporting, and model future org structures.

**Learn more:** [Making Position Changes](../scenarios/making-position-changes.md)

---

## Creating & Managing Scenarios

### How many scenarios can I create?
**Answer:** There's no hard limit. However, keep your scenario list manageable—delete test scenarios and archive completed ones. Most organizations maintain 5-15 active scenarios for current planning efforts.

**Learn more:** [Scenario Management](../scenarios/management.md)

### How do I name scenarios effectively?
**Answer:** Use format: [Department/Area] [Purpose] [Time Period]. Good examples: "Engineering Q2 2026 Expansion", "Sales Budget Cut 10%", "Product Team Reorg v2". Avoid generic names like "Scenario 1" or "Test".

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

### Can I duplicate a scenario to test different approaches?
**Answer:** Yes! Duplicating is the best way to compare alternatives. Duplicate your base scenario, rename it (e.g., "Option A", "Option B"), then model different approaches in each. Compare side-by-side to choose the best option.

**Learn more:** [Scenario Management](../scenarios/management.md)

### What's the difference between deleting and archiving a scenario?
**Answer:** Deleting is permanent—the scenario and all changes are lost forever. Archiving removes it from your active list but preserves it for historical reference. Best practice: archive implemented scenarios, only delete test scenarios.

**Learn more:** [Scenario Management](../scenarios/management.md)

### Can I undo changes in a scenario?
**Answer:** For recent changes, use browser undo (Cmd/Ctrl + Z). For older changes, check the Activity Log if available. Alternatively, delete the scenario and start over, or duplicate the scenario before making major changes to preserve previous versions.

**Learn more:** [Making Position Changes](../scenarios/making-position-changes.md)

---

## Working with Positions

### How do I add multiple similar positions at once?
**Answer:** Use the Duplicate function. Hover over a position, click Duplicate, select how many copies (1x, 5x, or custom), then edit each copy individually. This is faster than creating positions one at a time.

> **[Screenshot placeholder: Position card context menu showing "Duplicate" option with submenu displaying "1x", "5x", and "Custom" duplication options]**

**Learn more:** [Making Position Changes](../scenarios/making-position-changes.md)

### What's the difference between closing and deleting a position?
**Answer:** Closing a position tracks it in the OpEx Panel as cost savings and preserves history (use for RIFs and budget cuts). Deleting permanently removes it with no tracking (use only for cleanup of test positions or mistakes).

**Learn more:** [Making Position Changes](../scenarios/making-position-changes.md)

### How do I move an entire team to a new manager?
**Answer:** Drag and drop the manager's card to the new manager—the entire team (manager + all direct reports) moves together intact. Alternatively, select the team and use Change Manager from the three-dot menu.

**Learn more:** [Making Position Changes](../scenarios/making-position-changes.md)

### What are effective dates and when should I use them?
**Answer:** Effective dates control when changes take effect in time-based projections. Use them to phase organizational changes over time—for example, mark a department transfer with effective date January 2027, and in Forecast it appears starting that month.

**Learn more:** [Forecast Overview](../forecast/overview.md)

---

## Collaboration & Sharing

### Can multiple people edit a scenario simultaneously?
**Answer:** This depends on your Agentnoon configuration. Some setups support real-time collaboration, others require sequential editing. Check with your admin. Best practice: coordinate with team members to avoid conflicting changes.

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### How do I share a scenario with my team?
**Answer:** Sharing options vary by configuration. Typically, you can share via the scenario settings menu, generate a share link, or add collaborators by email. Shared users can view or edit depending on permissions you set.

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### How do I add comments to positions or scenarios?
**Answer:** Hover over a position, click the three-dot menu, select Comment, write your comment, optionally @mention collaborators, then post. Use comments to explain changes, ask for feedback, or document assumptions.

**Learn more:** [Making Position Changes](../scenarios/making-position-changes.md)

---

## Tracking Impact & Analysis

### Where do I see the cost and headcount impact of my changes?
**Answer:** Check the OpEx Panel (also called OpEx Panel or Scenario Impacts and Changes). It shows net headcount change, net cost impact, list of all additions and closures, and a submission button for approval.

> **[Screenshot placeholder: OpEx Panel panel displaying summary metrics - Net Headcount: +12, Net Cost: +$1.8M, with expandable sections for Additions (15 green), Reductions (3 red), and Data Changes (8 blue)]**

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### How do I compare two scenarios side-by-side?
**Answer:** Open both scenarios in separate browser tabs, or use the scenario comparison feature if available. Compare the OpEx Panel summaries, org chart structures, and export both to CSV for detailed analysis in Excel.

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### What do the colored icons on position cards mean?
**Answer:** Icons indicate changes: green = newly added position, red = RIF/layoff, orange = exit/voluntary departure, blue = edited details, purple = moved to different manager, yellow = on bench. These help you quickly identify what changed at a glance.

> **[Screenshot placeholder: Org chart in scenario view showing position cards with different colored indicator icons - green plus icon for additions, red X for RIF, blue pencil for edits, purple arrow for moves]**

**Learn more:** [Scenario Management](../scenarios/management.md)

---

## Approvals & Implementation

### What happens when I submit a scenario for approval?
**Answer:** The scenario enters the approval workflow, routing to designated approvers (Level 0 → Level 1 → Level 2 → Level 3). Depending on settings, the scenario may lock (preventing edits during approval). Approvers can approve, reject, or request changes.

> **[Screenshot placeholder: Scenario approval workflow view showing Level 0 (Approved - green checkmark), Level 1 (Pending - yellow clock icon), Level 2 (Not started - gray), Level 3 (Not started - gray)]**

**Learn more:** [Scenario Approvals](../scenarios/approvals.md)

### Who can approve scenarios?
**Answer:** Approvers are configured by admins. Typically includes Level 1 and Level 2 approvers (global) plus Level 0 and Level 3 approvers (scenario-specific). Common approvers: department heads, finance leaders, HR leaders, or executives.

**Learn more:** [Admin Overview](../admin/overview.md)

### Does approving a scenario automatically change Main Org?
**Answer:** No. Scenarios don't automatically update Main Org. After approval, you implement the changes in your real HRIS (Workday, BambooHR, etc.), then your admin refreshes Main Org data, and the changes appear.

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

---

## Next Steps

- **[Scenarios Overview](../scenarios/overview.md)** - Complete introduction to scenarios
- **[Creating Scenarios](../scenarios/creating-scenarios.md)** - Step-by-step creation guide
- **[Making Position Changes](../scenarios/making-position-changes.md)** - Learn all position actions
- **[Scenario Management](../scenarios/management.md)** - Organizing and versioning scenarios
- **[Forecast FAQs](forecast.md)** - Forecast and time-based planning questions
