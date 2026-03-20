import pulp as pl

model = pl.LpProblem("THDC", pl.LpMaximize)

# continuous variables
x_1 = pl.LpVariable("standard", lowBound = 0)
x_2 = pl.LpVariable("high_security", lowBound = 0)
x_3 = pl.LpVariable("maximum_security", lowBound = 0)

# discrete variables
# x_1 = pl.LpVariable("standard", lowBound = 0, cat="Integer")
# x_2 = pl.LpVariable("high_security", lowBound = 0, cat="Integer")
# x_3 = pl.LpVariable("maximum_security", lowBound = 0, cat="Integer")

# objective
model += 35*x_1 + 45*x_2 + 65*x_3

# constraints
model += x_3 <= x_1 + x_2
model += 3.5*x_1 + 6*x_2 + 8*x_3 <= 120, "machine1"
model += 4*x_1 + 5*x_2 + 6*x_3 <= 100, "machine2"
model += 11*x_1 + 15*x_2 + 20*x_3 <=280, "labor"

# solve
status = model.solve()

# print result
print("Status:", pl.LpStatus[status])
print("standard =", x_1.value())
print("high_security =", x_2.value())
print("maximum_security =", x_3.value())
print("profit = ", pl.value(model.objective))

for name, c in model.constraints.items(): 
    print(name, "slack =", c.slack, "shadow price =", c.pi)
