## Problem Statement
The Terre Haute Door Company (THDC) designs three types of steel doors: Standard, High Security, and Maximum Security.

Each door requires different amounts of machine and labor time and has different profit margins; this information is given in the following table.

| Door Type         | M1 Hours | M1 Manpower | M2 Hours | M2 Manpower | Profit Margin |
|-------------------|---------:|------------:|---------:|------------:|--------------:|
| Standard          |       3.5|            5|         4|            6|            $35|
| High Security     |         6|            8|         5|            7|            $45|
| Maximum Security  |         8|           11|         6|            9|            $65|

Each door must go through both machine 1 and machine 2 before it can be sold.

Each worker is assigned to work on only one of the doors, which means they work on both machines. 

In addition, management has decided not to sell more Maximum Security doors than the combined total of Standard and High Security doors sold,
in order to keep demand high for Standard and High Security doors. 

THDC has available to it only 120 hours per week on machine 1 and 100 hours on machine 2 before required maintenance,
and 280 hours of manpower available per week.

If we assume that we can sell every door that we make, how many of each door should be produced each week in order to maximize profit?

## Modelling

### Decision variables
$x_1$ = number of standard doors produced
$x_2$ = number of high security doors produced
$x_3$ = number of maximum security doors produced

### Objective function
maximize profit = $35x_1 + 45x_2 + 65x_3$

### Constraints
- produce non negative amount of doors
  - $x_1, x_2, x_3 \geq 0$ 
- the number of maximum security doors sold should be less than or equal to the combined total of standard and high security doors sold
  - $x_3 \leq x_2 + x_1$
- total machine 1 hours must be less than or equal to 120
  - $3.5x_1 + 6x_2 + 8x_3 \leq 120$ 
- total machine 2 hours must be less than or equal to 100
  - $4x_1 + 5x_2 + 6x_3 \leq 100$
- total manpower hours must be less than or equal to 280
  - $(5 + 6)x_1 + (8 + 7)x_2 + (11 + 9)x_3 \leq 280$
  - $11x_1 + 15x_2 + 20x_3 \leq 280$

### Solution
```shell
Status: Optimal
standard = 9.0322581
high_security = 0.0
maximum_security = 9.0322581
profit =  903.22581
```

Discrete Solution
```shell
Status: Optimal
standard = 9.0
high_security = 0.0
maximum_security = 9.0
profit =  900.0
```
