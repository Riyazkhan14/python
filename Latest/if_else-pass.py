a = 33
b = 200

if b > a:
    pass

'''
Why Use pass?
The pass statement is useful in several situations:

When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later
'''

age = 16
if age < 18:
    pass # TODO: Add underage logic later
else:
    print("Access granted")


# pass with Multiple Conditions

value = 50

if value < 0:
    print("Negatove Value")
elif value ==0:
    pass # Zero case - No action needed
else:
    print("positive values")

# Pass in Function
def calculcate_discount(price):
    pass
