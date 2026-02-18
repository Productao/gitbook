---
description: Best practices for naming, versioning, and organizing scenarios
hidden: false
---

# Organizing Scenarios

As your scenario library grows, organization becomes critical. This guide covers best practices for naming conventions, versioning, archiving, and maintaining a clean, efficient workspace.

---

## Naming Conventions

### Why Naming Matters

**Good names help you:**
- Find scenarios quickly
- Understand purpose at a glance
- Avoid confusion with similar scenarios
- Communicate clearly with stakeholders
- Maintain organization as scenarios multiply

**Poor names cause:**
- Confusion about which scenario is current
- Time wasted searching for right scenario
- Duplicate work (can't find existing scenario)
- Miscommunication with stakeholders

---

### Standard Naming Format

**Recommended structure:**

```
[Purpose] - [Scope/Details] - [Version/Date]
```

**Examples:**
- "Engineering Reorg - Flatten Structure - v2"
- "Q2 Hiring Plan - Commercial NA - 2026-02-15"
- "Budget Cut 10% - Option A"
- "VP Engineering Succession - Candidate A"

---

### Naming Components

#### Purpose (Required)

**What this scenario is about:**
- "Hiring Plan"
- "Budget Cut"
- "Reorganization"
- "Succession Planning"
- "Expansion"
- "Consolidation"

**Why include:** Immediately tells viewers the scenario's goal.

---

#### Scope/Details (Recommended)

**Which part of organization:**
- Department: "Engineering", "Sales", "Marketing"
- Geography: "EMEA", "North America", "APAC"
- Team: "Product Marketing", "Enterprise Sales"
- Level: "IC Roles", "Leadership", "VP Level"

**Why include:** Clarifies what's affected, prevents confusion.

---

#### Version/Date (Situational)

**Version for alternatives:**
- "Option A", "Option B", "Option C"
- "v1", "v2", "v3"
- "Conservative", "Moderate", "Aggressive"
- "Draft", "Revised", "Final"

**Date for chronological tracking:**
- "Q1 2026", "Q2 2026"
- "2026-02-15" (ISO format)
- "Feb 2026"

**Why include:** Tracks progression, enables comparisons.

---

### Naming Best Practices

**DO:**
- ✅ Be specific: "Engineering Q2 Hiring" not "Hiring"
- ✅ Include dates: "Q2 2026" not "Next Quarter"
- ✅ Use consistent format across scenarios
- ✅ Keep under 50-60 characters
- ✅ Use hyphens or underscores as separators
- ✅ Capitalize properly for readability

**DON'T:**
- ❌ Leave as "Untitled Scenario" or "New Scenario"
- ❌ Use generic names: "Test", "Scenario 1"
- ❌ Make overly long names (100+ characters)
- ❌ Use special characters that break systems
- ❌ Mix naming conventions inconsistently

---

## Versioning Strategies

### When to Create New Version

**Create new version when:**
- Major direction change
- Stakeholder feedback requires significant revisions
- Testing completely different approach
- Want to preserve previous version for reference

**Example progression:**
1. "Hiring Plan v1" - Initial draft
2. "Hiring Plan v2" - After stakeholder feedback
3. "Hiring Plan v3" - Final approved version

---

### Don't Create New Version For

**Minor changes that don't need versioning:**
- Small tweaks to positions
- Correcting typos or errors
- Adjusting a few salaries
- Minor organizational shifts

**For minor changes:** Just update the existing scenario.

---

### Version Naming Options

#### Option 1: Numbered Versions
- "Plan v1", "Plan v2", "Plan v3"
- **Pro:** Clear progression, easy to understand
- **Con:** Doesn't explain what changed

#### Option 2: Lettered Options
- "Plan - Option A", "Plan - Option B", "Plan - Option C"
- **Pro:** Good for alternatives, not just iterations
- **Con:** Runs out at Z

#### Option 3: Descriptive Versions
- "Plan - Conservative", "Plan - Moderate", "Plan - Aggressive"
- **Pro:** Self-documenting, explains approach
- **Con:** Harder to establish convention

#### Option 4: Date-Based Versions
- "Plan - Feb 1", "Plan - Feb 15", "Plan - Mar 1"
- **Pro:** Chronological, tracks when created
- **Con:** Doesn't explain what changed

**Recommendation:** Combine approaches: "Plan v2 - Aggressive - Feb 15"

---

## Archiving Strategy

### When to Archive

**Archive scenarios that are:**
- Completed and implemented
- Approved but superseded by newer version
- Historical reference (no longer active work)
- Reducing clutter but want to preserve

**Don't archive scenarios that are:**
- Still being worked on
- Under active review
- May need quick changes
- Referenced frequently

---

### Archive vs Delete Decision Tree

```
Is scenario a test or mistake?
└─ YES → DELETE
└─ NO → Was it used for important decision?
    └─ YES → ARCHIVE (preserve history)
    └─ NO → Was it approved/implemented?
        └─ YES → ARCHIVE
        └─ NO → Was significant work invested?
            └─ YES → ARCHIVE
            └─ NO → DELETE (if truly not needed)
```

**General rule:** When in doubt, archive. Deletion is permanent.

---

### Archiving Workflow

**Monthly cleanup:**
1. Review scenarios from past 30 days
2. Archive completed/approved scenarios
3. Delete clear test scenarios
4. Keep active work visible

**Quarterly cleanup:**
1. Review all scenarios from previous quarter
2. Archive all Q1 scenarios if now in Q3
3. Export change logs for archived scenarios
4. Document key decisions before archiving

---

## Folder/Group Structure

If your system supports folders or groups:

### Structure Option 1: By Department

```
📁 Engineering
  ├─ Q1 Hiring
  ├─ Q2 Reorg
  └─ Q3 Budget Cut
📁 Sales
  ├─ Territory Realignment
  ├─ Q2 Expansion
  └─ Quota Model
📁 Marketing
  ├─ Team Consolidation
  └─ Demand Gen Buildout
```

---

### Structure Option 2: By Time Period

```
📁 2026 Q1
  ├─ Engineering Hiring
  ├─ Sales Expansion
  └─ Marketing Reorg
📁 2026 Q2
  ├─ Engineering Reorg
  ├─ Sales Quota Model
  └─ Marketing Budget Cut
📁 2026 Annual
  ├─ Full Org Planning
  └─ Succession Planning
```

---

### Structure Option 3: By Status

```
📁 Draft
  ├─ Engineering Hiring v1
  ├─ Sales Expansion (WIP)
  └─ Marketing Test
📁 In Review
  ├─ Engineering Hiring v2
  └─ Sales Expansion Final
📁 Approved
  ├─ Marketing Reorg
  └─ Engineering Q1 Hiring
📁 Implemented
  ├─ Q4 2025 Plans
  └─ Archive
```

---

## Comparison Sets

### Creating Comparison Sets

**Scenario:** Need to evaluate 3 different approaches to a reorg

**Setup:**
1. Create base scenario: "Reorg - Base Analysis"
2. Duplicate three times:
   - "Reorg - Option A - Flatten Structure"
   - "Reorg - Option B - Add Middlelayer"
   - "Reorg - Option C - Hybrid Approach"
3. Tag all with: "Q2 Reorg Comparison"
4. Model different approaches in each
5. Use comparison view to evaluate side-by-side

**Benefit:** Structured alternatives make decision-making clearer.

---

### Naming Comparison Sets

**Pattern:**
```
[Base Name] - Option [A/B/C] - [Key Differentiator]
```

**Examples:**
- "Budget Cut - Option A - Eliminate Junior Roles"
- "Budget Cut - Option B - Eliminate Senior Roles"
- "Budget Cut - Option C - Hybrid Approach"

**Why:** Makes it obvious these are related alternatives, not independent scenarios.

---

## Cleanup Workflows

### Weekly Quick Cleanup

**5-minute review:**
1. Rename any "Untitled" scenarios
2. Tag new scenarios appropriately
3. Delete obvious test scenarios
4. Archive clearly completed work

---

### Monthly Deep Cleanup

**30-minute review:**
1. Review all scenarios from past month
2. Standardize names to match convention
3. Archive implemented scenarios
4. Delete old test scenarios
5. Update tags for clarity
6. Export change logs for archived scenarios
7. Document key decisions

---

### Quarterly Full Cleanup

**2-hour review:**
1. Review entire scenario library
2. Archive all previous quarter scenarios
3. Delete unnecessary test scenarios
4. Reorganize folder structure (if used)
5. Update tagging conventions
6. Export all change logs for compliance
7. Create summary report of quarter's planning
8. Prepare scenario list for next quarter

---

## Export and Backup Strategy

### Regular Exports

**What to export:**
- Change logs (CSV)
- Org charts (PDF)
- Scenario metadata (list of scenarios with tags, dates, owners)

**When to export:**
- Before archiving scenarios
- After major approvals
- End of quarter
- Before major system changes
- For compliance/audit trails

---

### Export Naming Convention

**Suggested format:**
```
[Scenario Name] - [Export Type] - [Date].csv/pdf
```

**Examples:**
- "Engineering Q2 Hiring - Change Log - 2026-02-15.csv"
- "Budget Cut Option A - Org Chart - 2026-02-15.pdf"
- "Succession Plan VP Eng - Comparison - 2026-02-15.xlsx"

---

## Collaboration and Ownership

### Clear Ownership

**Best practices:**
- Assign clear owner to each scenario
- Owner responsible for naming, cleanup, archiving
- Use tags or attributes to track ownership
- Don't leave scenarios orphaned

**Avoid:**
- Scenarios with no clear owner
- Multiple people editing without coordination
- Confusion about who can archive/delete

---

### Shared Scenarios

**When multiple people collaborate:**
- Agree on naming conventions upfront
- Use consistent tagging
- Document changes in comments
- Designate one person as "scenario lead"
- Regular check-ins to stay aligned

---

## Tools and Features

### Search Functionality

**Use search effectively:**
- Search by scenario name
- Search by tags
- Search by owner
- Search by date range
- Search by content (if supported)

**Pro tip:** Good naming makes search easier.

---

### Favorites or Pinning

**If available:**
- Pin frequently accessed scenarios to top
- Favorite scenarios you own
- Create quick access to active work
- Reduces scrolling through long lists

---

### Bulk Operations

**If supported:**
- Bulk tag multiple scenarios
- Bulk archive old scenarios
- Bulk delete test scenarios
- Batch export multiple scenarios

---

## Best Practices Summary

1. **Name scenarios clearly from the start** - Don't leave as "Untitled"
2. **Use consistent naming conventions** - [Purpose] - [Scope] - [Version]
3. **Tag scenarios systematically** - Department, quarter, purpose
4. **Version intentionally** - Only create versions for significant changes
5. **Archive, don't delete** - Preserve historical planning records
6. **Clean up regularly** - Weekly quick reviews, monthly deep reviews
7. **Export before archiving** - Create backup records
8. **Assign clear ownership** - Someone accountable for each scenario
9. **Use comparison sets** - Structured alternatives for better decisions
10. **Document conventions** - Share standards with team

---

## Common Pitfalls to Avoid

❌ **Leaving too many "Untitled" scenarios**
- Fix: Rename immediately upon creation

❌ **Inconsistent naming across team**
- Fix: Document and share naming convention

❌ **Never archiving or deleting anything**
- Fix: Schedule regular cleanup sessions

❌ **Deleting scenarios that should be preserved**
- Fix: Default to archive, only delete true test scenarios

❌ **Creating too many versions**
- Fix: Only version for significant changes

❌ **Not tagging scenarios**
- Fix: Make tagging required step in workflow

❌ **Unclear ownership**
- Fix: Assign owner to every scenario

---

## Next Steps

Now that you understand organization best practices:
- Review [Basic Actions](basic-actions.md) for scenario management fundamentals
- Learn [Tags](tags.md) for detailed tagging strategies
- Explore [Symbols](symbols.md) to understand change indicators
- Return to [Scenario Management](../management.md) overview
- Practice organizing your current scenario library using these guidelines
