# Slide B3 — Rate Cards (Compensation Bands)

## Title
Rate Cards

## Lead-line
Auto-populate salaries based on role attributes — like a VLOOKUP that runs whenever a new position is created.

## What Is It?
Rate Cards are compensation band lookup tables that automatically fill in salary data when a position's attributes match a defined rule. For example, if a new "Senior Engineer" position is created in "United States," the rate card can auto-populate the salary as $165,000.

## How to Set It Up
1. **Download the rate card CSV template** from Agentnoon
2. **Fill in your compensation bands** — each row defines a salary for a combination of attributes (e.g., Level + Location + Role Type → Salary)
3. **Upload via Data Management** → map the file
4. **Select independent attributes** (the lookup keys — e.g., Level, Country)
5. **Select the dependent field** (the output — e.g., Salary)
6. The rate card is now active and will auto-populate matching positions

## How to Use It
- When a planner creates a **new position** in a scenario and sets its Level to "Senior" and Location to "US," the salary auto-fills based on the rate card
- **Enable Rate Card display** in Card Content to show the suggested salary alongside the actual salary on every card
- **Group rate card fields** in settings to keep them organized
- **Update rate cards** annually (or as compensation bands change) by uploading a new CSV

## Example Rate Card CSV
| Level | Country | Salary |
|---|---|---|
| Junior | United States | $85,000 |
| Mid | United States | $120,000 |
| Senior | United States | $165,000 |
| Junior | United Kingdom | £55,000 |
| Mid | United Kingdom | £78,000 |
| Senior | United Kingdom | £110,000 |

## Screenshot / Visual
The rate card CSV example alongside a new position card showing the auto-populated salary.

## Speaker Notes
Rate Cards are one of those features that save enormous time once set up. Without them, every new position added in a scenario requires someone to manually look up and enter the correct salary. With them, planners just set the role's level and location, and the salary fills in automatically. This also enforces consistency — everyone uses the same compensation bands, reducing the risk of outlier salaries in planning. Update rate cards at least annually, or whenever your compensation team revises the bands.
