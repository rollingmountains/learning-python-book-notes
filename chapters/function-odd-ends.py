#  Local variables are detected statistically
x = 300


def func():
    global x
    print(
        x
    )  # to fix this use the global keyword to fromally access enclosing variable inside a function local
    x = 30  # when x is accessed as global any change made will change the global value
    print(x)


# Defaults and Mutable objects
def save(y=[]):  # func accepts a list, and has empty list [] as default value
    y.append(1)  # this is have the x point to [1] appending the empty list
    print(y)


# save()
# save(
#     [2]
# )  # send a list that has a value, python appends it to same list that already has [1] in it
# save()
# save(
#     [3]
# )  # send a list that has a value, python appends it to same list that already has [1] in it
# save()
# save()  # which each call it keeps adding to the same list, doesn't create a new one


# create a new list object when no object is passed so that each function call can work with new list object rather that appending the same default list object
def saved(
    y=None,
):  # by default y is assgined to none which is neither an empty object or nothing, y name is no open to any kind of object assignment
    if y is None:
        y = []  # this will create a new list for each call no more default object manipulation

    y.append(1)
    print(y)


# saved()  # [1]
# saved([3])  # [3,1]
# saved()  # [1]
# saved()  # [1]
# saved([2])  # [2, 1]


# saving object as function attribute
def saver():
    saver.z.append(1)
    print(saver.z)


saver.z = []  # extends the func object to hold a list attribute
alias = saver  # alias points to the same func object
saver = 42  # saver name is rebound to an int object
print(
    alias.z
)  # alias name continues to point to the func object and access the attributes
saver()  # this call will fail becasue saver is now an int object and is not callable
alias()  # this call will invoke the func object for execution but the body of the func object will error at saver.z.append(1) because the the name saver will now resolve to the int object 42
