---
description: Long-term headcount and budget planning
hidden: false
---

# Multi-Year Planning

Strategic workforce planning extends beyond the next fiscal year. Agentnoon's Forecast module supports multi-year planning, allowing you to project workforce costs and headcount up to 5 years into the future.

## Why Multi-Year Planning Matters

### Strategic Benefits
- **Board and investor presentations:** Show 3-5 year workforce growth trajectory
- **Long-term budget planning:** Understand cumulative workforce costs over time
- **Scenario testing:** Model different growth strategies and their long-term impacts
- **Capital planning:** Tie workforce expansion to revenue forecasts and funding rounds
- **Geographic expansion:** Plan multi-year rollouts of international offices
- **Organizational scaling:** Anticipate when to add management layers as you grow

### Typical Use Cases
- **Startup scaling:** Model headcount from 50 to 500 employees over 3 years
- **Enterprise transformation:** Plan 5-year workforce restructuring initiative
- **Geographic expansion:** Phase international hiring across 2026-2028
- **M&A integration:** Project workforce costs post-acquisition over 3 years
- **Budget rationalization:** Model gradual cost reduction over multiple years

---

## Setting Up Multi-Year Forecasts

### Step 1: Create a Multi-Year Scenario

Unlike annual planning, multi-year planning requires careful use of hire dates to phase growth over time.

**In a new scenario:**
1. Name your scenario descriptively: "2026-2028 Growth Plan"
2. Add positions for Year 1 (2026) with hire dates throughout the year
3. Add positions for Year 2 (2027) with hire dates in 2027
4. Add positions for Year 3 (2028) with hire dates in 2028
5. Use effective dates for organizational changes that happen mid-period

**Example:**
- **2026:** Add 50 positions (hire dates Jan-Dec 2026)
- **2027:** Add 75 positions (hire dates Jan-Dec 2027)
- **2028:** Add 100 positions (hire dates Jan-Dec 2028)
- **Result:** Phased growth from 200 → 250 → 325 → 425 employees over 3 years

### Step 2: Configure Forecast for Multi-Year View

**View your multi-year scenario in Forecast:**
1. Open your scenario
2. Switch to **Forecast** view
3. Select **Yearly** time period
4. Row aggregator: **Department** (or Location, Employee Type, etc.)
5. Toggle: **Headcount** (to see growth trajectory)
6. Toggle: **Cost** (to see budget implications)

**What you'll see:**
A table showing 5 columns: 2026, 2027, 2028, 2029, 2030
- Each row shows a department (or location, etc.)
- Values increase as hire dates pass
- Positions with hire dates appear in the year they start

### Step 3: Model Growth Assumptions

**Key considerations:**
- **Attrition:** Will you close positions to account for expected turnover?
- **Backfills:** Will you add positions to replace departures?
- **Compound growth:** Does headcount grow at a consistent % year-over-year?
- **Budget constraints:** Is there a maximum workforce cost per year?
- **Promotions:** Will salaries increase over time (use effective dates)?

**Example: Modeling 20% annual growth**
- 2026 starting headcount: 200
- 2027 target: 240 (200 × 1.20)
- 2028 target: 288 (240 × 1.20)
- 2029 target: 346 (288 × 1.20)

Add net new positions with hire dates to hit these targets.

---

## Handling Uncertainty in Long-Term Projections

### The Challenge
The further out you forecast, the less certain you can be about:
- Market conditions
- Company strategy shifts
- Funding availability
- Hiring success rates
- Attrition rates
- Salary inflation

### Strategies for Handling Uncertainty

#### 1. Scenario-Based Planning
Create multiple scenarios with different assumptions:

**Conservative Growth Scenario:**
- 10% annual headcount growth
- Minimal salary increases
- High attrition rate (15%)

**Moderate Growth Scenario:**
- 20% annual headcount growth
- 3% annual salary increases
- Standard attrition rate (10%)

**Aggressive Growth Scenario:**
- 35% annual headcount growth
- 5% annual salary increases
- Low attrition rate (5%)

**Compare all three in Forecast:**
- View each scenario in Forecast (yearly view, 5 years)
- Export each to CSV
- Place side-by-side in Excel to compare trajectories
- Present range to leadership: "We expect to reach 300-500 employees by 2028"

#### 2. Use Ranges, Not Exact Numbers
When presenting multi-year forecasts to stakeholders:
- Avoid false precision ("We'll have 347 employees in 2028")
- Use ranges ("We expect 300-350 employees in 2028")
- Acknowledge assumptions ("Assumes 20% growth and 10% attrition")

#### 3. Plan in Phases
Break multi-year plans into annual phases that can be adjusted:

**2026 (Detailed):**
- Specific positions with titles, departments, hire dates, salaries
- Full organizational design with reporting relationships

**2027 (High-Level):**
- Position counts by department (e.g., "+10 Engineers, +5 Sales")
- Budget allocations, not specific names or titles

**2028 (Directional):**
- Headcount targets by function
- Rough budget estimates
- Acknowledged as preliminary

**Why this works:** You can refine 2027 plans in Q3/Q4 2026 based on actual performance.

---

## Multi-Year Hiring Ramps

### Phased Hiring Strategy

Avoid front-loading all hires in Year 1. Spread hiring across years to:
- Match revenue growth
- Preserve cash runway
- Allow time to integrate new employees
- Adjust plans based on learnings

**Example: 3-Year Engineering Expansion**
- **Year 1 (2026):** +20 engineers (Q1: 5, Q2: 5, Q3: 5, Q4: 5)
- **Year 2 (2027):** +30 engineers (Q1: 7, Q2: 8, Q3: 7, Q4: 8)
- **Year 3 (2028):** +40 engineers (Q1: 10, Q2: 10, Q3: 10, Q4: 10)
- **Result:** Engineering grows from 50 → 140 over 3 years

**How to model in Agentnoon:**
1. Create 90 new engineering positions in your scenario
2. Assign hire dates across 2026-2028 quarters
3. View in Forecast (Quarterly or Monthly view) to see the ramp
4. Switch to Yearly view to see cumulative growth
5. Export to CSV and create visual timeline for stakeholders

### Modeling Different Growth Curves

**Linear growth:** Same number of hires per quarter
- Q1 2026: +10, Q2 2026: +10, Q3 2026: +10, Q4 2026: +10

**Accelerating growth:** Increasing hires over time
- Q1 2026: +5, Q2 2026: +10, Q3 2026: +15, Q4 2026: +20

**Decelerating growth:** Decreasing hires as you scale
- Q1 2026: +20, Q2 2026: +15, Q3 2026: +10, Q4 2026: +5

**Stepped growth:** Hiring in bursts tied to funding rounds
- Q1 2026: +50 (post-Series B), Q2-Q4 2026: +0, Q1 2027: +75 (post-Series C)

---

## Budget Projections Across Fiscal Years

### Modeling Salary Inflation

Salaries increase over time due to:
- Cost of living adjustments (COLA)
- Performance-based raises
- Promotions
- Market rate increases

**How to model:**
1. Create a scenario with your current workforce
2. For each year, apply salary increases using effective dates
3. View in Forecast to see cost increases over time

**Example: 3% Annual Salary Increases**
- 2026: Baseline salaries (no change)
- 2027: Add effective date adjustments (+3% for all employees)
- 2028: Add another effective date adjustment (+3%)
- 2029: Add another (+3%)

**Result:** Forecast shows workforce cost increasing even without new hires.

**Note:** This requires manual position-by-position salary updates or bulk operations. Agentnoon doesn't currently auto-calculate annual raises, so factor this into planning time.

### Geographic Cost Differences

When expanding internationally, account for location-based cost differences:

**Example: US vs. India Cost Structure**
- US Software Engineer: $150K annual salary
- India Software Engineer: $50K annual salary

**Multi-year plan:**
- 2026: Hire 20 US engineers ($150K each) = $3M
- 2027: Hire 30 India engineers ($50K each) = $1.5M
- 2028: Hire 40 India engineers ($50K each) = $2M
- **Result:** Headcount grows, but cost grows more slowly

**How to model:**
1. Add positions in your scenario with location-specific salaries
2. Use rate cards to auto-populate salaries by location
3. View in Forecast aggregated by Location
4. Compare cost efficiency across geographies

---

## Scenario Planning Within Multi-Year Forecasts

### Comparing Growth Strategies

**Use case:** You're deciding between three multi-year growth strategies.

**Option A: Domestic Growth**
- Grow US headcount from 200 → 500 over 3 years
- Higher cost per employee ($120K average)
- Total 3-year cost: ~$100M

**Option B: International Expansion**
- Grow US headcount to 300, India headcount to 200 over 3 years
- Blended cost per employee ($85K average)
- Total 3-year cost: ~$70M

**Option C: Hybrid + Contractors**
- Grow US headcount to 300, add 200 contractors globally
- Blended cost per employee ($75K average)
- Total 3-year cost: ~$60M

**How to evaluate:**
1. Create 3 scenarios (one for each option)
2. Add positions with phased hire dates across 2026-2028
3. View each scenario in Forecast (Yearly view)
4. Export all 3 to CSV
5. Compare total 3-year cost, headcount ramp, and cost per employee
6. Present to leadership for decision

---

## Rolling Forecasts vs. Static Multi-Year Plans

### Static Multi-Year Plan
- Created once at the start of the planning cycle
- Shows 2026-2030 projections based on 2026 assumptions
- Updated annually during budget planning season

**Best for:**
- Board presentations and investor updates
- Long-term strategic planning
- Capital planning tied to headcount growth

### Rolling Forecast
- Updated quarterly throughout the year
- Always shows "next 4 quarters" or "next 3 years"
- Incorporates actuals and adjusts future projections

**Best for:**
- Operational workforce planning
- Dynamic environments with high uncertainty
- Agile organizations that adjust plans frequently

### Implementing Rolling Forecasts in Agentnoon

**Quarterly update process:**
1. **Q1 2026:** Create "2026-2028 Plan v1" scenario
2. **Q2 2026:** Compare actuals to forecast, create "2026-2028 Plan v2" scenario with adjustments
3. **Q3 2026:** Create "2026-2028 Plan v3" incorporating Q1-Q2 actuals
4. **Q4 2026:** Finalize 2026, refine 2027, and add detail to 2028 in "2026-2028 Plan v4"

**Each quarter:**
- Update Main Org with actual data (CSV upload or live integration)
- Create new scenario based on updated Main Org
- Adjust future hire dates based on actual hiring pace
- Re-forecast remaining quarters/years
- Export and share updated projections

**Tip:** Name scenarios with version numbers or dates to track changes over time:
- "2026-2028 Growth Plan - Q1 2026 Version"
- "2026-2028 Growth Plan - Q2 2026 Update"
- "2026-2028 Growth Plan - Q3 2026 Revision"

---

## Communicating Multi-Year Plans to Leadership

### Executive Summary Format

When presenting multi-year workforce plans, focus on:

**Headline Metrics:**
- Starting headcount: 200 (2026)
- Ending headcount: 425 (2028)
- Total growth: 225 employees (112% increase)
- Total 3-year workforce cost: $150M
- Average cost per employee: $118K

**Key Assumptions:**
- 20% annual headcount growth
- 3% annual salary increases
- 10% attrition rate (backfilled positions)
- 60% US, 40% international by 2028

**Phasing:**
- 2026: +50 employees
- 2027: +75 employees
- 2028: +100 employees

**Risk Factors:**
- Assumes Series B funding closes Q2 2026
- Assumes hiring success rate of 80%
- Assumes market conditions remain favorable

**Visuals:**
- Line chart showing headcount growth 2026-2028
- Stacked bar chart showing cost by department per year
- Geographic distribution pie chart (2028)

### Board Presentation Best Practices

**Focus on:**
- Strategic rationale (why this growth trajectory?)
- Alignment to revenue targets (what's the revenue per employee?)
- Capital efficiency (are we hiring ahead of or behind revenue?)
- Comparison to industry benchmarks (how do we compare to peers?)

**Avoid:**
- Position-level details (board doesn't need to see individual roles)
- Monthly granularity (stick to yearly or quarterly views)
- Excessive precision (use ranges, acknowledge uncertainty)

---

## Best Practices for Multi-Year Planning

### 1. Start with the End in Mind
**Define your 3-year target state first:**
- What's the total headcount goal?
- What's the organizational structure?
- What's the geographic distribution?
- What's the budget envelope?

**Then work backwards:**
- What needs to happen in Year 3 to reach the goal?
- What needs to happen in Year 2 to set up Year 3?
- What needs to happen in Year 1 to enable Year 2?

### 2. Balance Detail with Flexibility
**Year 1 (Current Year):** High detail
- Specific positions with titles, salaries, hire dates, managers
- Organizational design with reporting relationships

**Year 2 (Next Year):** Moderate detail
- Position counts by department and role family
- Budget ranges, not exact salaries
- Quarterly phasing of hires

**Year 3+ (Future Years):** Directional targets
- Headcount goals by function
- Rough budget estimates
- Acknowledged as subject to change

### 3. Tie Workforce Plans to Business Metrics
**Link headcount growth to:**
- Revenue targets (what's our revenue per employee?)
- Customer growth (what's our customers per employee ratio?)
- Product milestones (what team size is needed to ship Product X?)
- Market expansion (what's required to enter EMEA market?)

**Example:**
"To reach $100M ARR by 2028, we need 500 employees at a revenue per employee of $200K, requiring 225 net new hires over 3 years."

### 4. Update Plans with Actuals Throughout the Year
**Don't wait until the next planning cycle to adjust.**

**Quarterly check-ins:**
- Did we hire as many people as planned?
- Are salaries tracking to forecast?
- Has attrition been higher or lower than expected?
- Do we need to adjust future quarters based on learnings?

**Update your scenario:**
- Refresh Main Org data with actuals
- Create a new scenario version incorporating actuals
- Adjust future hire dates and positions based on actual performance
- Re-forecast and share updated projections

### 5. Create Contingency Plans
**What if hiring is slower than expected?**
- Have a "slower ramp" scenario ready
- Adjust revenue targets or timelines accordingly

**What if funding is delayed?**
- Have a "reduced growth" scenario ready
- Identify which roles can be delayed or cut

**What if attrition is higher than expected?**
- Model higher backfill needs in scenarios
- Adjust net headcount growth targets

---

## When to Refresh Multi-Year Forecasts

### Annual Refresh (Required)
**Timing:** Q3 or Q4 of the prior year (for next year's plan)
- Full bottom-up rebuild of multi-year workforce plan
- Incorporate learnings from current year
- Align to updated business strategy and revenue targets

### Quarterly Refresh (Recommended)
**Timing:** First month of each quarter
- Update Main Org with actual data
- Create new scenario version with adjusted future periods
- Re-forecast based on current trajectory
- Share updated projections with Finance and leadership

### Ad-Hoc Refresh (As Needed)
**Triggers:**
- Major funding round closes
- Business strategy shifts significantly
- M&A activity
- Unexpected attrition or hiring success
- Market downturn requiring cost reductions

---

## Example: Modeling a 3-Year Startup Scaling Plan

### The Goal
Scale from 50 → 200 employees over 3 years while maintaining capital efficiency.

### Step 1: Define Phases
- **2026 (Year 1):** +50 employees (100 total)
- **2027 (Year 2):** +60 employees (160 total)
- **2028 (Year 3):** +40 employees (200 total)

### Step 2: Allocate by Function
**2026:**
- Engineering: +20
- Sales: +15
- Customer Success: +10
- Marketing: +3
- G&A: +2

**2027:**
- Engineering: +25
- Sales: +18
- Customer Success: +12
- Marketing: +3
- G&A: +2

**2028:**
- Engineering: +15
- Sales: +12
- Customer Success: +8
- Marketing: +3
- G&A: +2

### Step 3: Create Scenario
1. Create "2026-2028 Growth Plan" scenario
2. Add 150 new positions (50 + 60 + 40)
3. Assign hire dates across 2026-2028
4. Use rate cards to auto-populate salaries
5. Assign to appropriate departments and managers

### Step 4: View in Forecast
1. Switch to Forecast view
2. Select Yearly time period
3. Row aggregator: Department
4. Toggle: Headcount (then Cost)
5. Export to CSV

### Step 5: Present to Board
**Key slide:**
- Line chart: Headcount growth 50 → 200
- Bar chart: Workforce cost by year ($6M → $30M)
- Table: Headcount by function in 2026, 2027, 2028
- Assumptions: 20% attrition, $150K average salary, 80% hire success rate

---

## Next Steps

- **[Forecast Overview](overview.md)** - Understand Forecast module fundamentals
- **[Building Headcount Forecasts](building-headcount-forecasts.md)** - Create workforce projections
- **[Budget Planning & Tracking](budget-planning-tracking.md)** - Align forecasts with budgets
- **[Scenarios Overview](../scenarios/overview.md)** - Learn to create scenarios for multi-year planning
- **[Use Case: Building an Annual Hiring Plan](../use-case-tutorials/annual-hiring-plan.md)** - Step-by-step guide
