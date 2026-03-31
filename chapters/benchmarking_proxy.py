x = 10


def out():
    x = 100

    def inner():
        global x

        print(x)

    return inner


out()()
