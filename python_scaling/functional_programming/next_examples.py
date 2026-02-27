"""
next(iterator[, default]) returns the next item from an iterator.

It is especially useful when you want the first matching value from a
generator expression without building a full list in memory.
"""

numbers = [-3, -1, 0, 4, 8]

# Return the first positive number.
print(next(x for x in numbers if x > 0))

# Provide a default to avoid StopIteration when no match exists.
print(next((x for x in numbers if x > 10), 'No number above 10'))

# next also works well with any iterator, not just generator expressions.
tasks = iter(['download data', 'clean data', 'train model'])
print(next(tasks))
print(next(tasks))
print(next(tasks, 'No more tasks'))

# A more realistic example with structured data.
orders = [
    {'id': 101, 'total': 49.99},
    {'id': 102, 'total': 89.50},
    {'id': 103, 'total': 120.00},
]
print(next((order for order in orders if order['total'] >= 100), 'No large orders'))
