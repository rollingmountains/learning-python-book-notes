"""Module by nature is a singleton, meaning only one copy exists and it's shared. Which also means the namespace of a module is also shared. Class however can generate multiple objects generated from a shared template but carry their own state meaning each objects have their own namespace."""

# example a config module file
# config_value = 200

# if two files import the same config.py module life, the name config_value is accessed by both and could be changed by anyone of them, the value is shared
# if this file does something like this


# import config

"""
config.config_value = 200  # current file resets the shared value

"""

# import test  # test file also imports the config module below is the test file code

"""
import config

print(config.config_value) --> this gives 200, the value set by this current file
"""


"""Implement the same idea using a class within the module. Because module is the object that can be imported across files. And the class inside the module (defined at top level) can piggy back on module object as its attribute and make itself visible to another file, and make the independent state available. Essentially class is working its way through singleton module to distribute its template and an independent state object can then be instatiated in the importing file."""

# code in the config.py file below
"""
class Config:
    def __init__(self, value):
        self.value = value
"""
# current file imports class in config module directly
from config import Config

config = Config(200)  # current file sets its own value
print(f"I am config from current file, my value is {config}")

# another file test.py also sets its own value

"""
from config import Config

config = Config(300)

"""
import test

"""
The output for the class based template sharing but idependent state objects is 
I am config from current file, my value is 200
I am config from test file, my value is 300
"""


"""
Conclusion: A moudle is a singletone, meaning it can only have on instance. That instance is shared among all importing files. Any changes to its attribute via module_object.attributes = new_value mutates the module namespace and its shared by all other attribute. If the attribute is directly accessed via from moudle import attribute and attribute = new_value then the moudle name space isn't mutated.   
A class on the other hand can generate multiple object with idependant state based on a shared template. The independent state then gives the importing file the ability to work by defining and owning the independent state without worrying about it being shared by other files or modules. This is the flexibility class provides over modules. Importantly, class delivers this capability through the module - a singletone object - and not bypassing singleton. 

"""
