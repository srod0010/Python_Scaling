"""
sorted(iterable, key=None, reverse=False) returns a sorted version of iterable. The key argument allows you to provide a function that returns the value to sort on.
"""
print(sorted([10, 5, 20, 30, 25, -5]))

# Sort words by length, then alphabetically for ties.
words = ['pear', 'banana', 'fig', 'apple', 'kiwi']
print(sorted(words, key=lambda word: (len(word), word)))

# Sort records by score descending.
players = [
    {'name': 'Savior', 'score': 92},
    {'name': 'Alex', 'score': 87},
    {'name': 'Jamie', 'score': 95},
]
print(sorted(players, key=lambda player: player['score'], reverse=True))
