'''
Python Math
Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:
'''

x = min(5,10,25)
y = max(5,10,25)

print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:

z = abs(-7.25)
print(z)

# The pow(x, y) function returns the value of x to the power of y (xy).
a = pow(2,3)
print(a)

'''
The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:

import math
When you have imported the math module, you can start using methods and constants of the module.

The math.sqrt() method for example, returns the square root of a number:
'''

import math
b = math.sqrt(64)
print(b)

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

c = math.ceil(1.4)
d = math.floor(1.4)

print(c)
print(d)

# math Pi

e = math.pi
print(e)


'''
Challenge: Math
Test your understanding of Python math by completing a small coding challenge.

Instructions
Inside the editor, complete the following steps:
Print the lowest value of 5 and 10 using min()
Print the highest value of 5 and 10 using max()
Print the absolute value of -7.25 using abs()
Print the value of 4 to the power of 3 using pow()
'''





























