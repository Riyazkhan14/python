'''
Python range
The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

This set of numbers has its own data type called range.

Note: Immutable means that it cannot be modified after it is created.
Creating ranges
The range() function can be called with 1, 2, or 3 arguments, using this syntax:
range(start, stop, step)
'''

x = range(10)
y = range(3, 10)
z = range(3,10,2)

print(f"Single argument range {list(x)}")
print(f"Two argument range {list(y)}")
print(f"Three argument range {list(z)}")


# Using ranges - Ranges are often used in for loops to iterate over a sequence of numbers.

for i in range(10):
    print(i)

# Using List to Display Ranges - The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.
# Therefore, ranges are often converted to lists for display.

print(list(range(5)))
print(list(range(1,6)))
print(list(range(5,20,3)))

r = range(10)
print(r[2])
print(r[:3])

# Membership Testing
# using 'in' operatot - The return value is True when the number is present in the range, and False when it is not.

r = range(0, 10, 2)
print(6 in r)
print(7 in r)

# Range supports len function
r = range(0,10,2)
print(len(r))

'''
Challenge: Range
Test your understanding of Python range by completing a small coding challenge.

Instructions
Inside the editor, complete the following steps:
Use a for loop with range(6) to print numbers 0 through 5
Use a for loop with range() to print numbers 2 through 5
'''



























