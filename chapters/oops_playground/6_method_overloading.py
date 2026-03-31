# when a child class overrides a function attribute it inherited from a parent class it's method overloading

"""Example 1 of method overriding"""

# most common method that gets overriden is the __init__ method of the supercalss type

# a class without __init__ overriding
# class Animal:
#     pass


# cat = Animal()
# print(vars(cat)) # --> {} it's empty because the namespace of the instance object was constructed by the metaclass type. type is responsible for construction of namespace, the populating of attributes belongs to the hiearchy of customization via inheritance which is supported by object implicitly

# customizing init


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat = Animal("Snowy", 10)
# print(
#     vars(cat)
# )  # --> {'name': 'snowy', 'age': 10}, now the namespace is filled thanks to the customized init function in subclass Animal. Here Animal inherits from class type during the class creation, and doesn't need explicit Animal(type). type injects itself into Animal.__class__ = 'type' attribute during class creation

# print(Animal.__class__)


"""Example 2 of method overriding"""


# class PaymentProcess overrides two methods 1. __init__ and the __call__, call method makes an instance object callable like a function
class PaymentProcess:
    def __init__(self, name):
        self.name = name

    def __call__(self, amount):
        return f"payment processed for the amount {amount} using {self.name}"


# instance object stripe is created with the ability to be called and passed an amount
stripe = PaymentProcess("stripe")


# process the amount thorough stripe gateway
def process(amount, pay_gateway):
    return pay_gateway(amount)


print(process(100, stripe))
