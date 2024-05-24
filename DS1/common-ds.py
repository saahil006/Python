# String
# Python Strings are arrays of bytes representing Unicode characters. In simpler terms, a string is an immutable array of characters. Python does not have a character data type, a single character is simply a string with a length of 1.
#
# Note: As strings are immutable, modifying a string will result in creating a new copy.

# Bytearray
# Python Bytearray gives a mutable sequence of integers in the range 0 <= x < 256.
a = bytearray((12, 8, 25, 2))
print("Creating Bytearray:")
print(a)

# Lists
# Python Lists are just like the arrays, declared in other languages which is an ordered collection of data.
# It is very flexible as the items in a list do not need to be of the same type
# The costly operation is inserting or deleting the element from the beginning of the List as all the elements
# are needed to be shifted.
List = [1, 2,  3, "GFG", 2.3]
print(List)


# Dictionary
# Python dictionary is like hash tables in any other language with the time complexity of O(1).
# It is an unordered collection of data values, used to store data values like a map,
# which, unlike other Data Types that hold only a single value as an element, Dictionary holds the key:value pair.
# Key-value is provided in the dictionary to make it more optimized.
#
# Indexing of Python Dictionary is done with the help of keys.
# These are of any hashable type i.e. an object whose can never change like strings, numbers, tuples, etc.
# We can create a dictionary by using curly braces ({}) or dictionary comprehension.

# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# accessing a element using key
print("Accessing a element using key:")
print(Dict['Name'])

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(1))

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

# TUPLES
# Python Tuple is a collection of Python objects much like a list but Tuples are immutable in nature
# The elements in the tuple cannot be added or removed once created.
# Just like a List, a Tuple can also contain elements of various types.
#
# Tuples can also be created with a single element, but it is a bit tricky.
# Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.

Tuple = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)

# Set
# Python Set is an unordered collection of data that is mutable and does not allow any duplicate element.
# Sets are basically used to include membership testing and eliminating duplicate entries.
# The DS used in this is Hashing, a popular technique to perform insertion, deletion, and traversal in O(1) on average.
#
# If Multiple values are present at the same index position,
# then the value is appended to that index position, to form a Linked List

Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(Set)

# Frozen Sets
# FS are immutable objects
# that only support methods and operators that produce result without affecting the FS or sets to which they are applied.
# While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
#
# If no parameters are passed, it returns an empty frozenset.

frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(frozen_set)

# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# frozen_set.add("h")











