---
description: Create and apply custom formulas to using your own data fields.
icon: superscript
metaLinks:
  alternates:
    - https://app.gitbook.com/s/FQHYLeH687WAkUobefnf/data-import/formulas
---

# Formulas

### Overview

Custom formulas in Agentnoon allow you to define new calculated fields using existing attributes in your data - such as compensation - in natural language. These formulas can be used to model costs, estimate severance, apply benchmarks, or capture any custom logic specific to your planning needs. Formulas help turn raw data into actionable metrics.

### Setting up a Custom Formula

1. **Creating a formula:** Navigate to the Attributes and Formulas section and click Add New Formula. Give your formula a clear, recognizable name.
2. **Use variables from your data:** From the Available Variables panel, select the data fields you want to include - such as Level, Service\_Years, or Full\_Compensation.
3. **Write your formula logic:**
   * Use basic math operations, existing variables, and conditional logic to define your formula. Conditional logic allows you to apply different rules based on specific conditions.
   * You can use supported functions like ifElse, in, min, max, and arithmetic operations.

<figure><img src="../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

**Example:**\
\
Suppose you need to calculate severance for employees marked as "RIF" (Reduction in Force).\
The formula could be structured as:\
ifElse(in("RIF", \[scenarioState]), max(min(\[Service\_Years], 25), ifElse(\[Level] <= 7, 5, ifElse(\[Level] <= 12, 7, 19))), 0) \* (\[Full\_Compensation] / 25)\
\
This formula considers service years and employee level to determine the severance amount, ensuring precise calculations based on your specific criteria.

<figure><img src="https://19874675.fs1.hubspotusercontent-na1.net/hubfs/19874675/image-png-Dec-12-2024-04-52-34-8159-PM.png" alt=""><figcaption></figcaption></figure>
