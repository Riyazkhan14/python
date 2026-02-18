import mymodule
mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

'''
Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module
You can create an alias when you import a module, by using the as keyword:

Example
Create an alias for mymodule called mx:
'''
import mymodule as mx
a = mx.person1["name"]
print(a)


import platform

x = platform.system()
y = platform.processor()
z = dir(platform)
print(x,y)
print(z)

from mymodule import person1
print(person1["country"])
