'''
Scope
A variable is only available from inside the region it is created. This is called scope.

Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
'''

def my_scope():
    x = 300
    print(x)
my_scope()

# Function inside Function
def myscope():
    x = 400
    def myinfunc():
        print(x)
    myinfunc()
myscope()

# Global Scope
'''
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.
'''

y = 100
def myscope1():
    print(y)
myscope1()
print(y)


'''
Naming Variables
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
'''
myscope2var = 700
def myscope2():
    myscope2var = 800
    print(myscope2var)
myscope2()
print(myscope2var)

# Global Keyword : It can be use inside and outside on the function

def myscope3():
    global myv
    myv = "this is global variable"

myscope3()
print(myv)

# Also, use the global keyword if you want to make a change to a global variable inside a function.

myv1 = "value1"
def myscope4():
    global myv1
    myv1 = "Value1 change inside Func"

myscope4()
print(myv1)

'''
Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function.
'''
def myscope5():
    x = "Jane"
    def myfunc():
        nonlocal x
        x = "hello"
    myfunc()
    return x
print(myscope5())

'''
The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace
'''

myv5 = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()
print("Global:", myv5)





























