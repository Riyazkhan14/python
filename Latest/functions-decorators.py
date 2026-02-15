'''
Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.

Basic Decorator
Define the decorator first, then apply it with @decorator_name above the function.
'''
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"

print(myfunction())

# Multiple Decorator Calls
@changecase
def otherfunction():
    return "I am speed!"

print(otherfunction())

# Arguments in the Decorated Function
def changecase1(func):
    def myinner1(x):
        return func(x).upper()
    return myinner1

@changecase1
def myfunc1(nam):
    return "Hello " + nam
print(myfunc1("John"))

# *args and **kwargs

def changecase2(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner

@changecase2
def myfunc2(nam):
    return "Hello " + nam
print(myfunc2("Masuma"))

# Decorator With Arguments
## Decorators can accept their own arguments by adding another wrapper level.

## Example
# A decorator factory that takes an argument and transforms the casing based on the argument value.


def changecase_a(n):
    def changecase_a(func):
        def myinner_a():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner_a
    return changecase_a

@changecase_a(1)
def myfunc3():
    return "Hello Linux"

print(myfunc3())

'''
Multiple Decorators
You can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.

Decorators are called in the reverse order, starting with the one closest to the function.
'''

def changecase_b(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + ", Have a good day!"
    return myinner

@changecase_b
@addgreeting
def myfunc4():
    return "Tobias"

print(myfunc4())

# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

def myfunc5():
    return "Have a great day!"

print(myfunc5.__name__)
print(myfunc5.__doc__)

'''
But, when a function is decorated, the metadata of the original function is lost.

Example
Try returning the name from a decorated function and you will not get the same result:


def changecase_c(func):
    def myinner():
        return func().upper()
    return myinner

@changecase_c
def myfunc6():
    return "Have a greate day!"

print(myfunc6.__name__)
'''

'''
To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
'''

import functools
def changecase_c(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()
    return myinner

@changecase_c
def myfunc6():
    return "Have a greate day!"

print(myfunc6.__name__)























