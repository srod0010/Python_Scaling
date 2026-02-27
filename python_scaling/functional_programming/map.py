"""
map(function, iterable) applies the function to each item in iterable

NOTE IMPORTANT:
returns either:
- Python 2: -> List
- Python 3: -> an iterable map object
"""

phrases = ['I think', 'I\'m good']

# In Python 3, map returns an iterator-like map object.
print(map(lambda x: x + ' bzz!', phrases))

# Wrap it in list(...) to see the transformed values.
print(list(map(lambda x: x + ' bzz!', phrases)))

# A slightly more realistic example: convert raw prices into formatted prices with tax.
prices = [19.99, 5.5, 120.0]
print(list(map(lambda price: round(price * 1.08, 2), prices)))

# map is also useful for reshaping data.
users = [
    {'name': 'savior', 'score': 92},
    {'name': 'alex', 'score': 87},
    {'name': 'jamie', 'score': 95},
]
print(list(map(lambda user: f"{user['name'].title()}: {user['score']}", users)))
