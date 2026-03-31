import sys

import c

sys.path.append("/Users/balapaudel/programming/learning-python/chapters")
# print(sys.path)

import pybench_runner as run

print(run.defnum)
run.defnum = 199
print(run.defnum)

x = 100
y = [x**2 for x in range(100)]


def func():
    return "I am from b module"


def importc():
    r = c.funcc()
    return f"{r} delivered by c module"


if __name__ == "__main__":
    pass
