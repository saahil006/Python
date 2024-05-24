## https://www.geeksforgeeks.org/python-data-structures/
### BUILT_IN
STRING - immutable object  
BYTEARRAY - a mutable sequence of integers in the range 0 <= x < 256.  
LIST - ordered collection of data with different datatypes
TUPLE - immutable in nature i.e. the elements in the tuple cannot be added or removed  
SET - unordered collection of data that is mutable and does not allow any duplicate element.  
DICTONARY - an unordered collection of key value pair stored like map  
FROZEN SET - immutable objects that only support methods and operators  

### COLLECTION
Counters - used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents the element in the iterable and value represents the count of that element in the iterable.   
OrderedDict - unlike a dictionary, it remembers the order in which the keys were inserted.  
DefaultDict - dictionary where it provide some default values for the key that does not exist  
ChainMap - encapsulates many dictionaries into a single unit and returns a list of dictionaries.  
NamedTuple - it returns a tuple object with names for each position which the ordinary tuples lack. 
Deque - optimized list for quicker append and pop operations from both sides of the container.   
UserDict - a dictionary-like container that acts as a wrapper around the dictionary objects  
UserList - a list-like container that acts as a wrapper around the list objects. 
UserString - a string-like container and just like UserDict and UserList, it acts as a wrapper around string objects.   

### CUSTOM COLLECTION - built using other collections
LinkedList  
Stack  
Queue  
Priority Queue  
Heap queue (or heapq python module)  
Binary Tree  
Graph  
