"""
The operator module contains ready-made functions for common operations.

It is often useful together with functools.partial when you want to replace
simple lambda expressions with reusable, named behavior.
"""

import operator
from functools import partial


numbers = [-3, -1, 0, 2, 7]

# operator.lt(a, b) returns a < b, so this becomes: 0 < x
is_positive = partial(operator.lt, 0)
print(list(filter(is_positive, numbers)))

# Use operator helpers for common sorting and lookup tasks.
players = [
    {'name': 'Savior', 'score': 92},
    {'name': 'Alex', 'score': 87},
    {'name': 'Jamie', 'score': 95},
]
print(sorted(players, key=operator.itemgetter('score'), reverse=True))

# Find the first score above 90 without writing a lambda.
print(next(filter(partial(operator.lt, 90), [72, 88, 91, 95]), 'No score above 90'))
