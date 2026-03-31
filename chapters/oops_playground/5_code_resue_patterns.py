"""OOP's biggest marketing is its ability to provide code resue in a way modules and functions cannot. Particularly:
1. the inheritance search chain via subclassing
2. multiple object instances from a single class
3. ability to adapt another class's behviour by instantiting the class in its __init__ method and using a specific behaviour

Code Reuse and Design Patterns:
Desgin pattern in the context of OOP exists to solve programming challenges (mostly how to organize data and behaviours in order to effectively apply the behaviour on the data)

These patterns are common across programming languages because they are not specific to a language but to programming in general. And each language adopts these design patterns in either the way the language implementations(underlying machinery will take care of the pattern for example the object model makes everything in python an object, a function and class can also passed around as behaviours) are desinged or explicit components (explicitly use features that implemtnt the pattern.)

Python largely has adopted these pattern via its idioms and code structures. Some patterns are adopted explicitly and some needs an exclusive implementation that lies outside the scope of idioms and explicit way and entirely on the programmer.

The language implemented pattern hides the pattern and makes it look like regular code. For example, the 'Stratergy' pattern.


"""

# A requirement where depending on the choice of algorithm we apply that behaviour on the data. Here algorithm is strategy


# alogrithm or strategies
def quicksort(data):
    return "i am quick sort"


def bubblesort(data):
    return "i am bubble sort"


# making strategies work on the data using procedural non pattern way
# def if_process(data, algorithm):
#     if algorithm == quicksort:
#         return algorithm(data)
#     if algorithm == bubblesort:
#         return algorithm(data)
#     return "Sorry no algorithm matched"


# making the strategies directly applied on the data without evluating the behaviour names
def interface_process(data, algorithm):
    return algorithm(data)


q = interface_process("test", quicksort)
b = interface_process("test", bubblesort)
print(q, b)
