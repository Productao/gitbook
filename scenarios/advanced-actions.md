---
description: Advanced operations for scenario management
icon: gears
---

# Advanced Scenario Actions

Advanced scenario actions allow you to perform complex operations like refreshing scenarios with updated data, merging multiple scenarios together, or promoting approved scenarios to your Main Org.

---

## Overview

Once you're comfortable with basic scenario operations, these advanced actions unlock powerful workflow capabilities:

- **Scenario Refresh**: Update an existing scenario with the latest Main Org data while preserving your changes
- **Scenario Merging**: Combine multiple scenarios into a single consolidated plan
- **Scenario to Main Org**: Promote an approved scenario to become your new current state

> **[Screenshot placeholder: Scenario actions menu showing Refresh, Merge, and Promote to Main Org options]**

---

## Scenario Refresh

**Purpose:** Update your scenario with the latest Main Org data without losing your planned changes.

**When to use:**
- Main Org has changed significantly since you created your scenario
- New employees have joined who should be included in your planning
- Organizational structure has changed and you want to rebase your scenario
- Your scenario is old and you want to work from current reality

**How it works:**
Scenario refresh merges the latest Main Org data into your existing scenario, preserving the changes you've made while updating positions that haven't been modified.

**Learn more:** [Scenario Refresh](refresh.md)

---

## Scenario Merging

**Purpose:** Combine multiple scenarios into a single consolidated scenario.

**When to use:**
- Multiple teams have created scenarios for different parts of the organization
- You want to combine separate hiring plans, reorgs, and budget changes
- Creating a master annual plan from quarterly scenarios
- Consolidating departmental plans into a company-wide plan

**How it works:**
Scenario merging takes changes from two or more scenarios and combines them into a new scenario, handling conflicts and overlaps intelligently.

> **[Screenshot placeholder: Scenario merge interface showing source scenarios being combined into a new merged scenario]**

**Learn more:** [Scenario Merging](merging.md)

---

## Scenario to Main Org

**Purpose:** Promote an approved scenario to become your new Main Org (current state).

**When to use:**
- Scenario has been fully approved through your approval workflow
- Changes are ready to be implemented in reality
- You want Agentnoon Main Org to reflect the new organizational structure

**How it works:**
This action applies all scenario changes to your Main Org, making the planned future state your new current reality. This is typically integrated with your HRIS implementation process.

> **[Screenshot placeholder: Scenario promotion confirmation dialog showing "Promote to Main Org" action]**

**Important considerations:**
- This action is typically restricted to admins
- Should only be used after real-world implementation
- Often integrated with HRIS update workflows
- Creates an audit trail of org changes

**Learn more:** [Scenario to Main Org](scenario-to-main-org.md)

---

## Best Practices for Advanced Actions

### Before Using Advanced Actions

**Backup first:**
- Duplicate your scenario before performing advanced operations
- Advanced actions can be complex and may have unexpected results
- Having a backup ensures you can recover if needed

**Understand impact:**
- Review what changes will be applied
- Check for conflicts or overwriting
- Validate with stakeholders if needed

**Test in isolation:**
- Try advanced actions on test scenarios first
- Validate the results match your expectations
- Only apply to production scenarios once confident

### Scenario Refresh Best Practices

- Use refresh sparingly - consider creating a new scenario instead
- Review all conflicts carefully before applying
- Document why refresh was needed
- Communicate refresh to scenario collaborators

### Scenario Merging Best Practices

- Ensure scenarios don't have conflicting changes to the same positions
- Merge scenarios with non-overlapping scope when possible
- Review the merged result thoroughly before sharing
- Keep source scenarios as reference

### Scenario to Main Org Best Practices

- Only promote after real-world implementation is complete
- Verify all approvals are in place
- Coordinate with HRIS and systems teams
- Communicate org changes to all stakeholders

---

## Common Questions

**Can I undo a scenario refresh?**

No, refresh cannot be undone. This is why creating a duplicate backup before refreshing is critical. If the refresh doesn't produce the desired result, you can delete the refreshed scenario and work from your backup.

**What happens if two scenarios I'm merging have conflicting changes?**

The merge interface will flag conflicts and ask you to resolve them. You'll choose which scenario's change to keep for conflicting positions, or manually set the desired outcome.

**Can anyone promote a scenario to Main Org?**

No, this action is typically restricted to admins or specific roles. It should only be used after organizational changes have been implemented in reality.

**When should I use refresh vs creating a new scenario?**

- **Use refresh when:** You want to preserve your existing changes and just update the baseline data
- **Create new scenario when:** Main Org has changed significantly, your scenario is very old, or you want a fresh start

---

## Related Articles

- [Scenario Management](management.md)
- [Scenario Collaboration](collaboration.md)
- [Scenario Approvals](approvals.md)
- [Creating Scenarios](creating-scenarios.md)
