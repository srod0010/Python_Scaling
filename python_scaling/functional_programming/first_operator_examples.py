"""
Using operator + functools.partial with first(...).

This replaces small lambda expressions with built-in operator functions.
"""

import operator
from functools import partial


def first(items, key=None, default=None):
    predicate = key or bool
    return next((item for item in items if predicate(item)), default)


numbers = [-5, -1, 0, 4, 9, 12]

# operator.lt(a, b) means a < b, so partial(operator.lt, 0) becomes 0 < x.
is_positive = partial(operator.lt, 0)
print('Using operator.lt with partial() to find the first positive number:')
print(first(numbers, key=is_positive, default='No positive numbers'))

# operator.lt(10, x) becomes 10 < x.
is_above_ten = partial(operator.lt, 10)
print('\nUsing a different threshold with the same pattern:')
print(first(numbers, key=is_above_ten, default='No number above 10'))

scores = [72, 88, 91, 95]
print('\nUsing next() + filter() with operator instead of lambda:')
print(next(filter(partial(operator.lt, 90), scores), 'No score above 90'))
