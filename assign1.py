# -*- coding: utf-8 -*-
"""assign1.ipynb

"""

def internship_days(income, travel_costs, rent, other_expenses):
    disposable_income = income - rent - other_expenses
    cost_per_day = 2 * travel_costs
    max_days = min(30, int(disposable_income / cost_per_day))
    return max_days

internship_days(1000, 12, 300, 100)
