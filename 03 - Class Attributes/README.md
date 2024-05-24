### Instance attributes and methods
#### We can dynamically assign an attribute to an instance from this magic method, which is called  double underscore in it.  we  were able to assign the attributes dynamically.  And we already know that the  object itself passed as an argument. So that's why we receive self.
 We have to validate the datatypes of the values that we  are passing in. So there are a couple of ways to achieve this. And one way is by using typing's in  the parameters that you're declaring inside here, so a great starter will be, for example, to  declare that a name must be a string. Now, let me  first take this back and change those to integer  and then go here and design those parameters. So in order to specify a typing, then you should  go ahead and create a colon sign, followed by the  type of the datatype that you expect to receive  here. 

### Class attributes
 A class attribute is an attribute that is going to be belong to the class itself. But  however, you can also access this attribute from the instance level as well.

### Built-n magic attribute 
#### _dict_
This magic  attribute is actually responsible to take all the attributes in a class and convert this to a dictionary.
#### _repr_
A text reprsentaion of the class, that can be accessed from the instance of the class.
