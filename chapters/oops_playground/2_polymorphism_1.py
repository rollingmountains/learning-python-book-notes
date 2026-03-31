# A database app to keep employee records

# A superclass called Employee that defines what it means to be an employee in the organisation
class Employee:
    def __init__(self, name):
        self.name = name

    def computeSalary(self):
        return "Salary from Employee class."

    def raiseSalary(self): ...
    def retire(self): ...

    def __repr__(self):
        return f"I am {self.name}"


# create actual employee record form the superclass definition
sue = Employee("sue")
bob = Employee("bob")
# print(sue.computeSalary(), sue.computeSalary())

# there is a department called Egineering where the salary is computed in way different from the one defined in the Employee class


# to solve that we can now subclass from Employee and re-define the computeSalary method in the subclass
# the overriding of bheviour using the same name or interface is called polymorphism
class Engineer(Employee):
    def computeSalary(self):
        return "Salary from the Engineer class"


# create an Employee from the Engineer class, it inhertis all the methods from Employee, overriding just the computeSalary
john = Engineer("john")
# print(john.computeSalary())

# all the 3 objects then can be collected in a container and can be processed based on the common interface computeSalary
# for emp in [sue, john, bob]:
#     print(emp.computeSalary())

# common interface is, again, polymorphism in action, a single face or idea or function computeSalary that performs different behviours depending on the object it's operating on


# the inheritance search always starts with the instance object first, and its parent class and above. That's the tree chain. so for sue it's sue->Employee->primordial object, john it's john -> Engineer -> Employee -> primordial object.
# the search stops when python finds the first occurances of the name in the chain. sue stops at Employee, john at Engineer.


# extending the above idea of collection of instance object inside another custom function mapping to real world scenario

# for example each employee might belong to different department within the company, we can the create department class to keep the department data and behviour in a single place unlike list and dict which can also do it but the data and behaviour would be scattered


class Department:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_employee(self, *employee):
        self.members.extend(employee)

    def compute_all_salaries(self):
        return [member.computeSalary() for member in self.members]

    def list_employees(self):
        return [emp for emp in self.members]


engineering = Department("Engineering")
engineering.add_employee(john)

finance = Department("Finance")
finance.add_employee(*[sue, bob])
lst = finance.list_employees()
# for item in lst:
#     print(item)

print(dir(Engineer.computeSalary.__code__))
