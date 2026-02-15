def my_function(fname):
    print(fname + " Akhtar")


my_function("Masuma")
my_function("Maheera")

'''
Parameters vs Arguments
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.
'''

def myfunction(name): # name is parameter
    print("Hello", name)

myfunction("Maheera") # Maheera is argument

# Number of Arguments
# By default, a function must be called with the correct number of arguments.
# If your function expects 2 arguments, you must call it with exactly 2 arguments.

def myfunc(fname, lname):
    print(fname, lname)

myfunc("Maheera", "Riyaz")

# we can call it with 1 argument
#myfunc("Hello")

# Default Parameter Values

def my_func(name = "Maheera"):
    print("Hello", name)

my_func()
my_func("Riyaz's MJ")


def county(country = "India"):
    print("I'm from", country)

county()
county("Brazil")
county("Sweden")

# Keyword Arguments
def ani_name(animal, name):
    print("I've a", animal)
    print("My", animal+"'s name is", name)

ani_name(animal="dog", name="Buddy")
ani_name(name="Buddy", animal="dog") # order doesn't matters

''' Positional Arguments
When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:
'''

ani_name("cat", "Maheera")
ani_name("Maheera","cat") # order matters in positional argument

# Mixing Positional and Keyword Arguments

def mix_posi(animal, name, age):
    print("I have a", age, "year old", animal, "name", name)
mix_posi("dog", name = "Buddy", age =5)


# Passing Different Data Types
def diff_data(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "Cherry"]
diff_data(my_fruits)

# AS Dictinary
def my_dict(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name" : "Mahee", "age" : 3}
my_dict(my_person)

# Return Values
def Ret_val(x,y):
    return x + y

result = Ret_val(5,3)
print(result)

# Returning Different Data Types

# List
def dif_data():
    return ["apple", "banana", "cherry"]

fruits = dif_data()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Tuple
def tup_r():
    return (10, 20)

x, y = tup_r()
print("x:", x)
print("y:", y)

'''
Positional-Only Arguments
You can specify that a function can have ONLY positional arguments.

To specify positional-only arguments, add , / after the arguments:
'''

def p_only(name, /):
    print("Hello", name)

p_only("Maau")

# p_only(name = "Maau") will not work


# Keyword-Only Arguments - To specify that a function can have only keyword arguments, add *, before the arguments:

def k_only(*, name):
    print("Hello", name)

k_only(name = "Masuma")

# Combining Positional-Only and Keyword-Only
'''
You can combine both argument types in the same function.

Arguments before / are positional-only, and arguments after * are keyword-only:
'''
def cp_only_k_only(a,b, /, *, c, d):
    return a+b+c+d

result = cp_only_k_only(5,10,c=15, d=20)
print(result)







































