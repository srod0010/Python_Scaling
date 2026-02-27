"""
any(iterable) and all(iterable) both return a boolean depending on the values returned by iterable.
These functions are equivalent to:

def all(iterable):
  for x in iterable:
    if not x:
      return False
  return True

def any(iterable):
  for x in iterable:
    if x:
      return True
  return False
"""

# Returns False because 0 is False.
print(all([1, 0, 3, 5]))

# Returns True because 1, 3 and 5 are truthy.
print(any([1, 0, 3, 5]))

# These functions are useful for checking whether any or all values satisfy a condition.
mylist = [0, 1, 3, -1]

if all(map(lambda x: x > 0, mylist)):
  print('All items are greater than 0')

if any(map(lambda x: x > 0, mylist)):
  print('At least one item is greater than 0')

# A more practical example with user records.
users = [
  {'name': 'Savior', 'active': True, 'verified': True},
  {'name': 'Alex', 'active': True, 'verified': False},
  {'name': 'Jamie', 'active': True, 'verified': True},
]

print(all(user['active'] for user in users))
print(any(not user['verified'] for user in users))

# Combined checks are often clearer with generator expressions.
print(all(user['active'] and user['verified'] for user in users))
