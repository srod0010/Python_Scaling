"""
Using functools.partial to create reusable key functions for first(...).

partial() pre-fills arguments so one general function can be reused for
multiple comparison rules.
"""

from functools import partial


def first(items, key=None, default=None):
    predicate = key or bool
    return next((item for item in items if predicate(item)), default)


def greater_than(number, minimum=0):
    return number > minimum


numbers = [-5, -1, 0, 4, 9, 12, 50]

print('Default greater_than behavior (minimum=0):')
print(first(numbers, key=greater_than))

is_above_ten = partial(greater_than, minimum=10)
print('\nUsing partial() to change the minimum to 10:')
print(first(numbers, key=is_above_ten, default='No number above 10'))

is_above_forty = partial(greater_than, minimum=40)
print('\nReusing the same function with a different threshold:')
print(first(numbers, key=is_above_forty, default='No number above 40'))
