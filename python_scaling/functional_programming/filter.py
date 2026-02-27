"""
filter(function or None, iterable) filters the items in iterable based on the result returned by the function
Note: Returns either:
- a list in Python 2 or earlier,
- an iterable filter object in Python 3:
"""
phrases = ['I think', 'I\'m good', 'I agree', 'Maybe later']

print(filter(lambda x: x.startswith('I '), phrases))

# Wrap it in list(...) to inspect the matches.
print(list(filter(lambda x: x.startswith('I '), phrases)))

# A more useful example: keep only even numbers above a threshold.
numbers = [3, 8, 12, 15, 22, 27, 34]
print(list(filter(lambda number: number > 10 and number % 2 == 0, numbers)))

# filter can also be used with collections of dictionaries.
users = [
    {'name': 'Savior', 'active': True, 'score': 92},
    {'name': 'Alex', 'active': False, 'score': 87},
    {'name': 'Jamie', 'active': True, 'score': 95},
]
print(list(filter(lambda user: user['active'] and user['score'] >= 90, users)))
