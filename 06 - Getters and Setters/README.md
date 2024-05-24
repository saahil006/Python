### Read only attributes
There can be need of attributes which should not be changeable after creation of the instance

#### @property(self)
This changes the attribute to a read-only property.This can not be set in init method directly 
but only if we attach an underscore before name we can access it.  
To make it inaccessible from outside use double underscore  
However we need not use underscore when using this attribute outside of the class.

#### @propertyName.setter(self,value)
It lets us set value of the property within the class definition.  
This means we will be using underscore before the property name.  
You can also reaise exception if the value is misfit.

