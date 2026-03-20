## Problem Statement
A local manufacturing plant runs 24 hours a day, 7 days a week. During various times throughout the day, different numbers of
workers are needed to run the various machines. Below are the minimum number of people needed to safely run the plant during various times.

| Times      | Employees Needed |
|:----------:|:-----------------|
| 12AM - 4AM |                 8|
|  4AM - 8AM |                 9|
| 8AM - 12PM |                15|
| 12PM - 4PM |                14|
|  4PM - 8PM |                13|
| 8PM - 12AM |                11|

Each worker works two consecutive 4-hour periods. What is the minimum number of workers needed to safely run this plant?

## Modelling

### Decision Variables
This one is a bit tricky, we need to focus on the number of people that begin each shift.

$x_i$ = number of employees beginning their shift at the start of the ith 4-hour period $i = 1, ..., 6$ 

### Objective Function
minimize $x_1 + x_2 + x_3 + ... + x_6$

minimize $\sum_{i = 1}^6 x_i$ 

### Constraints
we need to ensure that we have enough workers for every 4 hour period, we already know the minimum required. 

every 4 hour period will have available workers that started on that 4 hour period and workers that started on the previous 4 hour period

$x_1 + x_6 \geq 8$

$x_2 + x_1 \geq 9$

$x_3 + x_2 \geq 15$

$x_4 + x_3 \geq 14$

$x_5 + x_4 \geq 13$

$x_6 + x_5 \geq 11$

non negativity constraint

$x_i \geq 0, i \in \{1, ..., 6\}$

### Solution
```shelll
Status: Optimal

Shift starts:
12 AM - 4 AM  :     0.00
4 AM - 8 AM   :    11.00
8 AM - 12 PM  :     4.00
12 PM - 4 PM  :    10.00
4 PM - 8 PM   :     3.00
8 PM - 12 AM  :     8.00

min workers   :    36.00

Constraint analysis:
name        slack     shadow
x1          -0.00       1.00
x2          -2.00       0.00
x3          -0.00       1.00
x4          -0.00       0.00
x5          -0.00       1.00
x6          -0.00       0.00
```
