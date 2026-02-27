"""
Examples for common itertools tools shown in the lesson images.

Each section prints a label and then the resulting values so the file can be
run directly as a learning reference.
"""

import itertools
import operator


print('accumulate with the default + operator:')
sales = [100, 250, 175, 300]
print(list(itertools.accumulate(sales)))

print('\naccumulate with operator.mul:')
growth_factors = [2, 3, 4]
print(list(itertools.accumulate(growth_factors, operator.mul)))

print('\nchain combines multiple iterables:')
print(list(itertools.chain(['map', 'filter'], ['zip'], ['next', 'first'])))

print('\ncombinations creates r-length selections:')
print(list(itertools.combinations(['A', 'B', 'C', 'D'], 2)))

print('\ncompress filters data using a boolean selector mask:')
print(list(itertools.compress('EDUCATIVE', [1, 0, 1, 0, 0, 1, 0, 0, 1]))) # -> ['E', 'U', 'T', 'E']

print('\ncount generates an infinite arithmetic progression (sliced here):')
print(list(itertools.islice(itertools.count(start=5, step=5), 6)))

print('\ncycle repeats an iterable (sliced here so it terminates):')
print(list(itertools.islice(itertools.cycle(['A', 'B', 'C']), 8)))

print('\nrepeat duplicates the same value:')
print(list(itertools.repeat(20, 5)))

print('\ndropwhile skips items until the predicate becomes false:')
print(list(itertools.dropwhile(lambda x: x % 2 == 0, [2, 4, 6, 7, 8, 10, 20])))

print('\ntakewhile keeps items until the predicate becomes false:')
print(list(itertools.takewhile(lambda x: x % 2 == 0, [2, 4, 6, 7, 8, 10, 20])))

print('\ngroupby groups adjacent matching values:')
records = [
    ('A', 1),
    ('A', 2),
    ('B', 3),
    ('B', 4),
    ('C', 6),
    ('C', 7),
]
for key, group in itertools.groupby(records, key=lambda item: item[0]):
    print(key, list(group))

print('\npermutations creates ordered arrangements:')
print(list(itertools.permutations([1, 2, 3], 2)))

print('\nproduct creates the Cartesian product:')
print(list(itertools.product('AB', [1, 2, 3])))
