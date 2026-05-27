# Slide A9 — Formulas (Custom Calculated Fields)

## Title
Formulas

## Lead-line
Create custom calculated fields using logic and math — from severance estimates to cost projections.

## What Is It?
Formulas let you define custom calculated fields that derive values from existing data using natural language logic. These custom fields appear alongside the built-in FX fields (Span of Control, Layer, etc.) and update automatically as data changes.

## How to Set It Up
1. Navigate to **Attributes & Formulas** (in Data Management or Settings)
2. Click to create a new formula
3. **Select variables** from available position and employee fields
4. **Write your logic** using supported functions

## Supported Functions
- **Arithmetic:** +, -, *, / (e.g., Salary * 0.15 for bonus estimate)
- **Conditional:** ifElse(condition, trueValue, falseValue)
- **Membership:** in(value, list) to check if a value matches a set
- **Min/Max:** min(a, b), max(a, b)

## Example: Severance Calculation
```
ifElse(
  state == "RIF",
  ifElse(
    yearsOfService > 10,
    salary * 0.5,
    ifElse(yearsOfService > 5, salary * 0.3, salary * 0.15)
  ),
  0
)
```
This gives: 50% of salary for 10+ years, 30% for 5–10 years, 15% for under 5 years — only for RIF positions.

## Screenshot / Visual
The formula builder interface showing the variable selector, the logic editor, and a preview of the calculated result.

## Speaker Notes
Formulas are an advanced feature that extends Agentnoon's analytical power. They're most commonly used for compensation-related calculations — severance estimates, bonus projections, fully-loaded cost models. Once created, a formula becomes a field that can be displayed on cards, used in Directory columns, included in exports, and analyzed in Workforce Hub charts. Your admin creates the formulas, but all users benefit from the derived data.
