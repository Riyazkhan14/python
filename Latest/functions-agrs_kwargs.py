'''
*args and **kwargs
By default, a function must be called with the correct number of arguments.

However, sometimes you may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept a unknown number of arguments.

Arbitrary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly:
'''
def arbt_arg(*kids):
    print("The youngest child is " + kids[2])

arbt_arg("Emi", "Tobias", "linus")

'''
What is *args?
The *args parameter allows a function to accept any number of positional arguments.

Inside the function, args becomes a tuple containing all the passed arguments:
'''

def arbt_agr1(*args):
    print("Type:", type(args))
    print("First Argument:", args[0])
    print("Second Argument:", args[1])
    print("All arguments:", args)

arbt_agr1("Emil", "Tobias", "Linus")

# Using *args with Regular Arguments

def args_reg(greeting, *names):
    for name in names:
        print(greeting, name)

args_reg("Hello", "Emil", "Tobias", "Linus")


# Practical with *args calculate the sum of any numbers of the values
def my_exam(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_exam(1,2,3))
print(my_exam(10,20,30,40))
print(my_exam(5))

# Finding the maximum value




def find_max(*numbs):
    if len(numbs) == 0:
        return None
    max_num = numbs[0]
    print(f"this is max_num values {max_num}")
    for num in numbs:
        if num > max_num:
            #max_num = num
            y = num
    return y
print(find_max(3,7,2,9,1))

# Arbitrary Keyword Arguments - **kwargs
'''If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

This way, the function will receive a dictionary of arguments and can access the items accordingly:'''

def my_func(**kid):
    print("His last name is " + kid["lname"])
my_func(fname= "Tobias", lname = "Refsnes")


# What is **kwargs?
'''
The **kwargs parameter allows a function to accept any number of keyword arguments.

Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
'''
def my_func1(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_func1(name= "Tobias", age = 30, city = "Bergen")

# Using ** kwargs with Regular Arguments
# You can combine regular parameters with **kwargs.
# Regular parameters must come before **kwargs:

def reg_args1(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

reg_args1("emil123", age = 25, city = "Oslo", hobby = "Coding")

# Combining *args and *kwrgs -  You can use both *agrs and **kwargs in the same function.
''' The order must be:
1. regular parameters
2. *args
3. **kwargs
'''

def arg_kwarg(title, *args, **kwargs):
    print("Title:", title)
    print("Position arguments:", args)
    print("Keyword arguments:", kwargs)

arg_kwarg("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Unpacking Arguments as List
'''
The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

Unpacking Lists with *
If you have values stored in a list, you can use * to unpack them into individual arguments:
'''

def un_args(a,b,c):
    return a+b+c
numbers = [1,2,3]
result = un_args(*numbers) #same as: my_func(1,2,3)
print(result)

# Unpacking Disctionary with **
def unpack_dict(fname, lname):
    print("Hello,", fname, lname)
person = {"fname": "Emil", "lname": "Refsnes"}
unpack_dict(**person) #same as: my_func(fname="emil", lname="Refsens")












