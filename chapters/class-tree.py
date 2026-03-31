# building a skeleton tree with just class and instance object with no attributes
# superclass inherited by C1
class C2: ...


# superclass inherited by C1
class C3: ...


# sublcass that inherits C2 and C3 in that order
class C1(C2, C3): ...


# instances created out of class C1
I1 = C1()
I2 = C2()


# add attribute to the subclass C1
class C1(C2, C3):
    def setname(self, who):
        self.name = who

    def __repr__(self):
        return self.name


# create instances out of C1 class
I1 = C1()
I2 = C1()

# both the instances want to access the setname method @ C1
I1.setname("Instance 1")
I2.setname("Instance 2")

print(I1, I2)


# C1.setname = 10
I2.setname = "I2 setting the name"
print(C1.setname, I2.setname, I1.setname)
