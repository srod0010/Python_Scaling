"""
Coding challenge:

Given a list of integers, compute the sum of the squares of all elements
that are less than 50.

Constraint:
- Do not use explicit loops.
- Solve it in a functional style.

This file shows:
1. A clear functional solution using filter -> map -> sum
2. An alternative generator-based solution

It also avoids lambda by using small named functions, which is usually easier
to read and reuse.
"""

import operator
from functools import partial


# partial(operator.gt, 50) creates a function that checks: 50 > x
# which is equivalent to: x < 50
is_less_than_50 = partial(operator.gt, 50)


def square(number):
    """Return the square of a number."""
    return number * number


def compute(numbers):
    """
    Functional pipeline:
    1. filter values below 50
    2. map each value to its square
    3. sum the squared values
    """
    less_than_50 = filter(is_less_than_50, numbers)
    squared_values = map(square, less_than_50)
    return sum(squared_values)


def compute_with_generator(numbers):
    """
    A concise alternative that is still functional in style.

    This uses a generator expression instead of separate filter/map calls.
    """
    return sum(square(number) for number in numbers if number < 50)


sample_numbers = [10, 3, 52, 79]

print('Sample input:')
print(sample_numbers)

# Show the intermediate functional steps for clarity.
numbers_below_50 = list(filter(is_less_than_50, sample_numbers))
print('\nNumbers less than 50:')
print(numbers_below_50)

squared_numbers = list(map(square, numbers_below_50))
print('\nSquares of numbers less than 50:')
print(squared_numbers)

print('\nSum of the squares (filter -> map -> sum):')
print(compute(sample_numbers))

print('\nSum of the squares (generator expression alternative):')
print(compute_with_generator(sample_numbers))
