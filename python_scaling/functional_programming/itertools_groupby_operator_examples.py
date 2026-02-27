"""
Using operator.itemgetter with itertools.groupby.

This mirrors the lesson showing how operator can replace a small lambda
such as lambda item: item['foo'].
"""

import itertools
import operator


records = [
    {'foo': 'bar', 'value': 1},
    {'foo': 'bar', 'value': 42},
    {'foo': 'baz', 'value': 43},
    {'foo': 'baz', 'value': 99},
]

print('Raw groupby object converted to a list of pairs:')
grouped = itertools.groupby(records, key=operator.itemgetter('foo'))
print([(key, list(group)) for key, group in grouped])

print('\nGrouping again and summarizing each group:')
for key, group in itertools.groupby(records, key=operator.itemgetter('foo')):
    items = list(group)
    values = [item['value'] for item in items]
    print(f'{key}: {values}')

print('\nNote: groupby only groups adjacent items, so related records should be pre-sorted.')
