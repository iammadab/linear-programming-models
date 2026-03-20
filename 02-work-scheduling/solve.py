import pulp as pl

model = pl.LpProblem("Work_Schedule", pl.LpMinimize)

# decision variables
# each represents the number of workers that start each 4 hour period
x_1 = pl.LpVariable("x1", lowBound=0)
x_2 = pl.LpVariable("x2", lowBound=0)
x_3 = pl.LpVariable("x3", lowBound=0)
x_4 = pl.LpVariable("x4", lowBound=0)
x_5 = pl.LpVariable("x5", lowBound=0)
x_6 = pl.LpVariable("x6", lowBound=0)

# objective function
model += x_1 + x_2 + x_3 + x_4 + x_5 + x_6

# constraints
model += x_1 + x_6 >= 8, "x1"
model += x_2 + x_1 >= 9, "x2"
model += x_3 + x_2 >= 15, "x3"
model += x_4 + x_3 >= 14, "x4"
model += x_5 + x_4 >= 13, "x5"
model += x_6 + x_5 >= 11, "x6"

status = model.solve()

print("Status:", pl.LpStatus[status])

labels = [
    ("12 AM - 4 AM", x_1.value()),
    ("4 AM - 8 AM", x_2.value()),
    ("8 AM - 12 PM", x_3.value()),
    ("12 PM - 4 PM", x_4.value()),
    ("4 PM - 8 PM", x_5.value()),
    ("8 PM - 12 AM", x_6.value()),
]

print("\nShift starts:")
for label, value in labels:
    print(f"{label:<13} : {value:>8.2f}")

print(f"\n{'min workers':<13} : {pl.value(model.objective):>8.2f}")

print("\nConstraint analysis:")
print(f"{'name':<6} {'slack':>10} {'shadow':>10}")
for name, c in model.constraints.items():
    print(f"{name:<6} {c.slack:>10.2f} {c.pi:>10.2f}")
