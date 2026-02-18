---
description: Best practices for position-based vs headcount-based planning
icon: user-group
hidden: false
---

# Position vs Headcount Management

Understanding the difference between **positions** and **headcount** is fundamental to effective workforce planning. Agentnoon is built position-first, reflecting the best practices of strategic workforce planning and organizational design.

## The Core Difference

### Positions = Roles
**A position is a pre-approved function in your organization with a defined structure and budget.**

**Position attributes:**
- Position ID
- Title (e.g., "Senior Software Engineer")
- Department
- Manager (reporting relationship)
- Salary range or assigned salary
- Location
- Pay grade
- Job family
- FTE (full-time equivalent)

**Key insight:** Positions are stable, structural elements of your organization. They don't change frequently.

**Examples:**
- "Senior Product Manager - Growth Team"
- "VP of Engineering"
- "Sales Development Representative - West Region"

### Headcount = People in Roles
**Headcount refers to the actual employees filling positions.**

**Employee/headcount attributes:**
- Employee ID
- Employee name
- Hire date
- Termination date
- Employee-specific details (birthday, t-shirt size, emergency contact, etc.)
- Performance rating
- Tenure

**Key insight:** Headcount is volatile. People join, leave, go on leave, get promoted, transfer—all independent of the underlying position structure.

**Examples:**
- Sarah Chen fills the "Senior Product Manager - Growth Team" position
- John Smith fills the "VP of Engineering" position
- Position 12345 is vacant (headcount = 0, but position still exists)

---

## Positions vs Headcount: Side-by-Side

| Aspect | Positions | Headcount |
|---|---|---|
| **Purpose** | Organizational structure, workforce planning | Talent management, HR operations |
| **Volatility** | Stable (changes quarterly/annually) | Volatile (changes weekly/daily) |
| **Used for** | Org design, budgeting, strategic planning | Recruiting, performance management, payroll |
| **Attributes** | Title, department, salary, manager, location | Employee name, hire date, performance, tenure |
| **Changes** | Position created/closed, reporting changes, budget changes | Hires, terminations, leaves, transfers |
| **Lifecycle** | Created → Open → Filled → Closed | Hired → Active → On Leave → Terminated |
| **Planning Horizon** | 1-5 years | Days to months |
| **Visibility** | Visible in org charts, budget plans | Visible in HRIS, payroll systems |

---

## Why Agentnoon is Position-First

### Strategic Workforce Planning Requires Position-Level Thinking

**Workforce planning questions:**
- How many "Senior Engineers" do we need in 2026?
- What will it cost to add 10 "Account Executives" next quarter?
- Should we add a "VP of Marketing" or keep the team flat?
- What's the right org structure for our 300-person company?

**These are position questions**, not headcount questions.

You're not asking "How many humans do we need?" (that's too vague). You're asking **"What roles do we need, where do they report, what do they cost, and when do we need them?"**

### Positions Enable Better Planning

**1. Positions Persist Over Time**
- A "Senior Engineer" position exists whether it's filled today, filled next month, or vacant
- Headcount fluctuates (leave, termination, backfill), but the position remains

**2. Positions Have Approved Budgets**
- Each position has an allocated salary
- Total workforce budget = sum of all approved positions
- Even if a position is vacant, the budget is reserved for it

**3. Positions Define Organizational Structure**
- Reporting relationships are position-to-position (not person-to-person)
- Org chart shows structure independent of current employees
- You can model future org structures before hiring anyone

**4. Positions Enable Scenario Planning**
- Add a position to see impact before hiring
- Close a position to model RIF impact
- Move positions between departments to test reorg options

---

## When to Use Position-Based Planning

### Use Positions For:

#### **1. Organizational Design**
**Scenario:** You're restructuring Engineering into 3 sub-teams.

**Position-based approach:**
- Create new "Engineering Manager" positions for each sub-team
- Reassign "Senior Engineer" positions to report to new managers
- Model the new org structure in a scenario before implementing

**Why positions:** You're designing the structure—who reports to whom, what roles exist—independent of current employees.

#### **2. Budgeting and Financial Planning**
**Scenario:** Finance asks for next year's workforce cost by department.

**Position-based approach:**
- Total approved positions in Engineering: 50
- Average salary per position: $150K
- Engineering workforce budget: $7.5M

**Why positions:** Budget is allocated to positions (roles), not specific people. Even if someone quits, the budget for that position remains.

#### **3. Hiring Plans**
**Scenario:** You need to hire 20 new roles in Q2.

**Position-based approach:**
- Create 20 new positions with titles, departments, salaries, hire dates
- Submit for approval as a hiring plan
- Recruiting team fills those approved positions with actual candidates

**Why positions:** You're planning roles to hire, not specific individuals (you don't know their names yet).

#### **4. Reorgs and Restructuring**
**Scenario:** You're moving the Network Operations team into Operations & Logistics.

**Position-based approach:**
- Create a scenario
- Move all "Network Operations" positions to "Operations & Logistics"
- Change reporting relationships accordingly
- See cost and structure impact

**Why positions:** You're restructuring roles, not managing specific people.

#### **5. Long-Term Strategic Planning**
**Scenario:** What will our organization look like in 2028?

**Position-based approach:**
- Model growth in positions: +20 Engineers in 2026, +30 in 2027, +40 in 2028
- Define future org structure (new departments, management layers)
- Forecast cost based on future position count

**Why positions:** Strategic planning is about roles and structure, not specific individuals.

---

## When to Use Headcount-Based Planning

### Use Headcount For:

#### **1. Recruiting and Talent Acquisition**
**Scenario:** How many open roles do we need to fill this month?

**Headcount-based approach:**
- Total approved positions: 100
- Current headcount (filled positions): 85
- Open roles to recruit: 15

**Why headcount:** Recruiting cares about filling vacancies with actual people.

#### **2. Attrition and Turnover**
**Scenario:** What's our attrition rate, and how many backfills do we need?

**Headcount-based approach:**
- 10 people left in Q1 (out of 100)
- Attrition rate: 10%
- Backfill needs: 10 positions now vacant

**Why headcount:** Attrition measures people leaving, not positions closing.

#### **3. Performance Management**
**Scenario:** How many employees are high performers vs. low performers?

**Headcount-based approach:**
- 100 employees rated
- 20% high performers
- 10% low performers

**Why headcount:** Performance ratings apply to people, not positions.

#### **4. Payroll and Benefits Administration**
**Scenario:** What's our total payroll cost this month?

**Headcount-based approach:**
- 85 active employees
- Total actual salaries paid: $850K
- Benefits cost per employee: $2K
- Total payroll + benefits: $1.02M

**Why headcount:** Payroll is based on actual people employed, not approved positions.

#### **5. Onboarding and Training**
**Scenario:** How many new hires need onboarding this quarter?

**Headcount-based approach:**
- 10 people started in Q1
- Each needs 2 weeks onboarding
- Total onboarding capacity needed: 20 person-weeks

**Why headcount:** Onboarding is for actual people joining, not abstract positions.

---

## Agentnoon's Position-First Philosophy

### What This Means in Practice

**Primary focus:** Positions (roles, org structure, budgets)
- Every card in the org chart represents a position
- You plan by adding, closing, or moving positions
- Scenarios model position-level changes

**Secondary context:** Headcount (who's in those positions)
- Employee details appear in the employee section of cards
- Employee-specific fields (hire date, name, performance rating) are tracked
- You can attach or detach employees from positions

**The result:**
- You plan strategically at the position level
- You track operationally at the headcount level
- Both coexist in Agentnoon, with positions as the foundation

### Position States in Agentnoon

**1. Filled Position**
- Position exists with an assigned employee
- Card shows both position details and employee details
- Contributes to both position count and headcount

**2. Open Position (Vacancy)**
- Position exists but no employee assigned
- Card shows position details with "Open" or "Vacant" indicator
- Contributes to position count, but not headcount

**3. Closed Position**
- Position no longer exists (budget eliminated)
- Removed from org chart
- Does not contribute to position count or headcount

**4. Proposed Position (in scenarios)**
- Position planned for future but not yet approved
- Exists in scenario, not in Main Org
- Will become "Open" or "Filled" after scenario is implemented

---

## Common Mistakes and How to Avoid Them

### Mistake #1: Planning at the Headcount Level Only
**Problem:** "We need 10 more people in Engineering."

**Issue:** This doesn't answer:
- What roles? (Junior, Senior, Staff?)
- Where do they report? (Manager A, Manager B, new manager?)
- What do they cost? (Salaries vary by role)
- When do they start? (Phased hiring or all at once?)

**Solution:** Plan at the position level.
- "We need 5 Senior Engineers reporting to Manager A, 3 Mid-Level Engineers reporting to Manager B, and 2 Staff Engineers reporting to the Director."

### Mistake #2: Confusing Vacancies with Headcount
**Problem:** Reporting "We have 100 employees" when you actually have 100 approved positions but only 85 filled.

**Issue:** Misleads stakeholders about actual workforce size.

**Solution:**
- **Approved positions:** 100 (total roles with budget)
- **Current headcount:** 85 (actual employees)
- **Open positions:** 15 (vacancies to fill)

### Mistake #3: Ignoring Position Structure in Talent Management
**Problem:** Moving an employee to a new role without updating the position structure.

**Issue:** Reporting relationships break, org chart doesn't reflect reality, budget tracking fails.

**Solution:**
- Update the position structure (reassign position or create new position)
- Then attach employee to the updated position

### Mistake #4: Over-Focusing on Individual Employees in Strategic Planning
**Problem:** "We need to plan for Sarah's promotion next year."

**Issue:** Strategic workforce planning is about roles, not specific individuals.

**Solution:**
- Plan at the position level: "We need to create a Director-level position in Q3 2026"
- Talent decisions (who gets promoted) happen separately in performance management processes

### Mistake #5: Not Accounting for Vacancies in Budget Planning
**Problem:** "Our workforce cost is $8.5M (85 employees × $100K average)."

**Issue:** You have budget for 100 positions, not 85. Your actual workforce budget is $10M.

**Solution:**
- Budget based on approved positions (100 × $100K = $10M)
- Track actual spend based on filled headcount (85 × $100K = $8.5M)
- Savings from vacancies = $1.5M (can be redirected or saved)

---

## Transitioning from Headcount to Position-Based Planning

### If You've Been Planning by Headcount

Many organizations start with headcount-based planning ("We have 200 employees"). Transitioning to position-based planning requires a mindset shift.

**Step 1: Define Your Position Structure**
- What roles exist in your organization today?
- Create position titles, assign to departments, define reporting relationships
- Associate each employee with their position

**Step 2: Identify Approved Positions vs. Filled Positions**
- Do you have budget-approved positions that are currently vacant?
- Are there positions that exist structurally but aren't funded yet?

**Step 3: Start Planning at the Position Level**
- When planning hires, define the position first (title, salary, manager, department)
- Then recruit to fill that position
- Track progress: positions approved → positions open → positions filled

**Step 4: Use Agentnoon to Visualize Position Structure**
- Import your data with position-level detail
- View org chart to see position-based structure
- Create scenarios to model position-level changes

---

## Combining Position and Headcount Planning

### The Best Approach: Use Both

**Position-level planning (strategic):**
- What org structure do we need?
- What roles are required to execute our strategy?
- What will our workforce cost over the next 3 years?

**Headcount-level tracking (operational):**
- How many people do we currently employ?
- What's our attrition rate?
- How many vacancies do we need to fill this quarter?

**In Agentnoon:**
- **Scenarios and Forecast:** Position-based planning (add/close positions, model changes)
- **Main Org and Directory:** Track current headcount (filled vs. open positions)
- **Metrics:** View both position count and headcount (SOC, IC count, manager count)

---

## Industry Best Practices

### Position-Based Planning is the Standard
**Why leading organizations use position-based planning:**
- Aligns with financial budgeting (positions have approved budgets)
- Supports organizational design (positions define structure)
- Enables scenario planning (test changes before implementing)
- Scales better (positions are stable, headcount is volatile)

**Examples:**
- **Tech companies:** Plan by engineering levels (E3, E4, E5), not just "engineers"
- **Consulting firms:** Plan by consultant grades (Analyst, Consultant, Manager, Partner)
- **Retail:** Plan by store roles (Store Manager, Assistant Manager, Sales Associates per store)

### Agentnoon Aligns with Best Practices
By focusing on positions first:
- You plan strategically (org structure, budget, roles)
- You track operationally (who's in those roles, attrition, vacancies)
- You model future states (scenarios with proposed positions)

---

## Case Study: Position vs Headcount in Action

### Scenario: Engineering Expansion Plan

**Headcount-only approach (wrong):**
- "We need 20 more engineers in 2026."
- Result: No clarity on roles, levels, reporting structure, or phasing.

**Position-based approach (right):**
- **Q1 2026:** Add 5 Senior Engineers (reporting to Manager A), 2 Staff Engineers (reporting to Director)
- **Q2 2026:** Add 1 Engineering Manager, 4 Mid-Level Engineers (reporting to new manager)
- **Q3 2026:** Add 3 Senior Engineers (reporting to Manager B), 2 Junior Engineers
- **Q4 2026:** Add 3 Mid-Level Engineers

**Result:**
- Clear roles, levels, reporting relationships
- Phased hiring plan (not all at once)
- Budget per quarter (use Forecast to project)
- Org structure defined (even before hiring)

**In Agentnoon:**
1. Create "2026 Engineering Expansion" scenario
2. Add 20 positions with titles, levels, managers, hire dates
3. View in Forecast to see headcount and cost ramp by quarter
4. Export for stakeholder approval
5. Submit scenario for executive approval
6. After approval, implement by hiring to fill positions

---

## Next Steps

- **[Making Org Changes](making-org-changes.md)** - Best practices for restructuring
- **[Key Concepts](../start-here/concepts.md)** - Fundamental Agentnoon terminology including positions vs people
- **[Scenarios Overview](../scenarios/overview.md)** - Model position-level changes
- **[Forecast Overview](../forecast/overview.md)** - Project position growth over time
- **[Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)** - Create position-based projections
