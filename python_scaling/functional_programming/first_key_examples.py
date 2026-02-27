"""
Using the key argument with a first(...) helper.

This mirrors the lesson where a custom predicate function is passed into
first() instead of writing the condition inline every time.
"""


def first(items, key=None, default=None):
    predicate = key or bool
    return next((item for item in items if predicate(item)), default)


def greater_than_zero(number):
    return number > 0


print('Using first() with the default truthy check:')
print(first([0, False, None, '', 42]))

numbers = [-5, -1, 0, 4, 9]
print('\nUsing key=greater_than_zero:')
print(first(numbers, key=greater_than_zero))


def is_open_high_priority(ticket):
    return ticket['priority'] == 'high' and not ticket['resolved']


tickets = [
    {'id': 101, 'priority': 'low', 'resolved': True},
    {'id': 102, 'priority': 'medium', 'resolved': False},
    {'id': 103, 'priority': 'high', 'resolved': False},
]
print('\nUsing key with dictionaries:')
print(first(tickets, key=is_open_high_priority, default='No urgent open ticket'))
