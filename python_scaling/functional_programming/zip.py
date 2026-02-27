"""
The zip(iter1 [,iter2 [...]]) takes multiple sequences and combines them into tuples.
It is useful when you need to combine a list of keys and a list of values into a dictionary.
Like the other functions described above, it returns a list in Python 2 and an iterable in Python 3:
"""

keys = ['foobar', 'barzz', 'ba!']

# NOTE: uses len(obj: Sized) -> int as the lambda function -> so created [6, 5, 3]
print(map(len, keys))

print(zip(keys, map(len, keys)))

print(list(zip(keys, map(len, keys))))

print(dict(zip(keys, map(len, keys))))

# zip is useful for pairing two related lists.
names = ['Savior', 'Alex', 'Jamie']
scores = [92, 87, 95]
pairs = list(zip(names, scores))
print(pairs)

# You can also unpack zipped data back into separate sequences.
print("Example unpack zipped data back into sepearte sequences")
top_students = [('Savior', 92), ('Alex', 87), ('Jamie', 95)]
student_names, student_scores = zip(*top_students)
print(student_names)
print(student_scores)
