#### Class Methods
Use decorator @classmethod to mark the method as class method
It also gets a default parameter in its params which is cls(class reference). It can be accessed only at class level and not by instantiated objects.
This should also do something that has a relationship with the class, 
but usually, those are used to manipulate different structures of data to primarily instantiate objects.

#### Static Methods
Use decorator @staticmethod to mark the method as static method
It does not get any argument in parameter. It does not work with any instance and could have existed class-less.
This should do something that has a relationship with the class, but not something that must be unique per instance!

