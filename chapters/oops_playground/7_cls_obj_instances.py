"""Object Instances"""

""" A regular class is a factory to generate object isntances based on its definition """

# a class inherits all the dunder methods of the primordial object which it can override
# dunder init method populates namespace for an object instances
# dunder call method gives an object a callable capability, which is similar to a function call. convert non callable object into a callable object


# class Animal:
#     def __init__(self, name):  # overrides object's init method
#         self.name = name

#     def __call__(self):  # overrides object's call method
#         return f"Hi, name is {self.name}, did you call me? what can i do for you?"


# cat = Animal("snowy")
# print(cat())


""" Class Instances """
""" A metaclass is a factory to generate class instances based on metaclass's definition. """

# a metaclass inherits all the dunder methods of primordial type metaclass, and inheriting quality is from primordial object(made avaiable to class instances by type via injectin object into instance class's bases attribute) but the inherited methods belong to type

# a custom meta class has to sublclass type which is the first and the origin of all metaclasses and classes
# the dunder method __init__ is to populate the namespace for the class
# dunder method __call__ gives a instance class to behave like a function so that it can then be used to create instance of objects


class Meta(type):
    def __init__(cls, name, bases, namespaces):
        print(f"Meta.__init__ : class {name} is created")
        super().__init__(name, bases, namespaces)

    def __call__(cls, *args, **kwargs):
        print(f"Meta.__call__ : class {cls.__name__} is instantiated")
        return super().__call__(*args, **kwargs)


class Animal(metaclass=Meta):  # subclass the custom metaclass Meta
    def __init__(
        self, name
    ):  # init method to instantiate object instance inherited form primordial object
        self.name = name
        print(f"Animal.__init__ : object {self.name} is instantiated")


cat = Animal("snowy")

"""
class definition  →  type.__new__   # allocates class namespace
                  →  Meta.__init__  # fills class namespace, class now exists

Animal("Snowy")   →  Meta.__call__  # triggered by calling the class
                      → object.__new__   # allocates instance namespace
                      → Animal.__init__  # fills instance namespace
"""
