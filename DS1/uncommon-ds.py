#
# Counters
# A counter is a sub-class of the dictionary.
# It is used to keep the count of the elements in an iterable in the form of an unordered dictionary
# where the key represents the element in the iterable and value represents the count of that element in the iterable.
# This is equivalent to a bag or multiset of other languages.

from collections import Counter
# With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))
# with dictionary
count = Counter({'A': 3, 'B': 5, 'C': 2})
print(count)
count.update(['H', 1])
print(count)

# OrderedDict
# An OrderedDict is also a sub-class of dictionary but unlike a dictionary,
# it members the order in which the keys were inserted.
from collections import OrderedDict

print("Before deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)

