"""
functools.partial lets you pre-fill some arguments of a function and create
a new function with a simpler interface.
"""

from functools import partial


def first(items, key=None, default=None):
    predicate = key or bool
    return next((item for item in items if predicate(item)), default)


def greater_than(number, minimum=0):
    return number > minimum


numbers = [-5, -1, 0, 7, 11]

# Create reusable predicates from one general function.
is_positive = partial(greater_than, minimum=0)
is_above_ten = partial(greater_than, minimum=10)

print(list(filter(is_positive, numbers)))
print(first(numbers, key=is_above_ten, default='No number above 10'))

# partial also works well with business rules.
monthly_sales = [120, 450, 700, 980]
is_vip_sale = partial(greater_than, minimum=500)
print(list(filter(is_vip_sale, monthly_sales)))
