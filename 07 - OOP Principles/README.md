### OOPS principles https://www.freecodecamp.org/news/object-oriented-programming-in-python/
#### ENCAPSULATION
Restricting direct access to some of attributes in class, but still creating functions which can help in 
changing values of these properties. **GETTER AND SETTER** methods
Private attributes are inaccessible attributes, and information hiding is the process of making particular attributes private. 
You use two underscores to declare private characteristics.  

#### ABSTRACTION  
There can be methods within class that should not be used by clients/child classes, like setting config,db connection.
But since all methods are accessible from instance, we should guard these methods by making them private by adding double
underscore before their name  and adding decorator **@abstractmethod**

Abstraction isn't supported directly in Python. Calling a magic method, on the other hand, allows for abstraction.
If an abstract method is declared in a superclass, 
subclasses that inherit from the superclass must have their own implementation of the method.
A superclass's abstract method will never be called by its subclasses. 
But the abstraction aids in the maintenance of a similar structure across all subclasses.  

#### INHERITANCE  
A mechanism to reuse code across classes.  


#### POLYMORPHISM
Ability to have different scenarios when calling the same entity.
Same attribute can be overwritten to a different value in different classes.


#### METHOD OVERLOADING
Python doesn't support Method Overloading by default.

#### METHOD OVERRIDING
When a method with the same name and arguments is used in both a derived class and a base or super class, we say that the derived class method "overrides" the method provided in the base class.
When the overridden method gets called, the derived class's method is always invoked. The method that was used in the base class is now hidden.  


