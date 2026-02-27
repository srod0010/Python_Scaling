"""
itertools provides efficient iterator building blocks for working with
streams of data in a functional style.
"""

import itertools


# Build a sequence lazily and take only the first few values.
print(list(itertools.islice(itertools.count(start=10, step=5), 4)))

# chain combines multiple iterables into one iterator.
print(list(itertools.chain(['apples', 'bananas'], ['carrots', 'dates'])))

# combinations is useful for generating pairings without nested loops.
print(list(itertools.combinations(['map', 'filter', 'zip'], 2)))

# groupby groups adjacent matching values, so sorting first is common.
statuses = sorted(['new', 'done', 'new', 'in_progress', 'done', 'done'])
grouped_statuses = {
    status: len(list(group))
    for status, group in itertools.groupby(statuses)
}
print(grouped_statuses)
