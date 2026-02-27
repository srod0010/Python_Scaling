"""
enumerate(iterable[, start]) 
returns an iterable enumerate object that yields a sequence of tuples,
each consisting of an integer index (starting with start, if provided) and the corresponding item in iterable.
It is useful when you need to write code that refers to array indexes. For example, instead of writing this:

i = 0
while i < len(mylist):
    print('Item %d: %s' % (i, mylist[i]))
    i += 1
"""
mylist = [1, 2, 3]
for i, item in enumerate(mylist):
    print('Item %d: %s' % (i, item))

print(list(enumerate(mylist)))

# start lets you shift the displayed index.
for position, item in enumerate(['alpha', 'beta', 'gamma'], start=1):
    print('Position %d: %s' % (position, item))

# enumerate is helpful when you need both a rank and a value.
scores = ['92 pts', '87 pts', '95 pts']
ranked_scores = [f'Rank {index}: {score}' for index, score in enumerate(scores, start=1)]
print(ranked_scores)
