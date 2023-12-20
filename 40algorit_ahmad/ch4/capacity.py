"""
Application of Linear Programming to solve a capacity planning problem.

Here is the scenario:
Robot A and B are manufactured by a company. A yield $4,200 in profit, while B
yields $2,800 in profit. 

The requirements to make A are:
    3 days of Technician time, 4 days of AI specialist time, and
    4 days of Engineer time

The requirements to make B are:
    2 days of Technician time, 3 days of AI specialist time, and
    3 days of Engineer time

The company has 1 technician, 1 AI specialist, and 2 engineers. In the next
30 days, the technician needs 10 days off, and each engineer needs 8 days off.

The equations for this problem become:
profit = 4200 x A + 2800 x B
Subject to
    A >= 0, B >= 0,
    3A + 2B <= 20 (for the technician)
    4A + 3B <= 30 (for the AI specialist)
    4A + 3B <= 44 (for the engineers)
"""

# Imports ---------------------------------------------------------------------
import pulp

# Functions -------------------------------------------------------------------

# Main ------------------------------------------------------------------------
def main():
    model = pulp.LpProblem("Profit maximization", pulp.LpMaximize)

    A = pulp.LpVariable('A', lowBound = 0, cat = 'Integer')
    B = pulp.LpVariable('B', lowBound = 0, cat = 'Integer')

    # Profit function
    model += 4800 * A + 2400 * B

    # Time constraints
    model += 3*A + 2*B <= 20
    model += 4*A + 3*B <= 30
    model += 4*A + 3*B <= 44

    # Solve equation
    model.solve()

    print(f"Optimal number of robot A to make: {A.varValue}")
    print(f"Optimal number of robot B to make: {B.varValue}")

    return model

if __name__ == '__main__':
    # Run calculation
    model = main()

    print(pulp.LpStatus[model.status])
    print(pulp.value(model.objective))