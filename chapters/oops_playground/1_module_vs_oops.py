# floating function vs a method attached to a class
emp1 = {"name": "john", "age": 40, "pay": 2000}
emp2 = {"name": "doe", "age": 35, "pay": 2500}


def raise_salary(percent, pay):
    return pay + (pay * (percent / 100))


emp1_raise_pay = raise_salary(5, emp1.get("pay"))
emp2_raise_pay = raise_salary(10, emp2.get("pay"))

emp1["pay"] = emp1_raise_pay
emp2["pay"] = emp2_raise_pay

# emp1, emp2


# method attached to a class
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def raise_salary(self, percent):
        previous_pay = self.pay
        self.pay = self.pay + (self.pay * (percent / 100))
        return f"Pay before raise is {previous_pay}.The new revised pay after {percent} percent raise is {self.pay}"

    def __repr__(self):
        return f"{self.name} aged {self.age}"


emp1_john = Employee("john", 40, 2000)
emp2_doe = Employee("doe", 35, 2500)


emp1_john.raise_salary(5)
emp2_doe.raise_salary(10)

print(emp1_john, emp2_doe)
for emp in [emp1_john, emp2_doe]:
    print(emp.pay)

print(globals())
print("Employee" in globals())
print("emp1_john" in globals(), "emp2_doe" in globals())


# method attached to a class
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def raise_salary(self, percent):
        previous_pay = self.pay
        self.pay = self.pay + (self.pay * (percent / 100))
        return f"Pay before raise is {previous_pay}.The new revised pay after {percent} percent raise is {self.pay}"

    def __repr__(self):
        return f"{self.name} aged {self.age}"


# accidental duck typing experiment
class Contractor:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def raise_salary(self, percent):
        self.pay = self.pay + (10000 * percent)
        return f"{self.pay} i am a contractor and my name is {self.name}"

    def __repr__(self):
        return f"{self.name} is a contractor and my salary is {self.pay}"


emp1 = Contractor("jane", 3000)

s = Employee.raise_salary(emp1, 4)


def func():
    pass


func.pay = 4000

print(Employee.raise_salary(func, 20))

d = dict()
d["pay"] = 2000

print(Employee.raise_salary(d, 20))
