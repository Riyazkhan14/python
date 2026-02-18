'''
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

Before Python 3.6 we had to use the format() method.

F-Strings
F-string allows you to format selected parts of a string.

To specify a string as an f-string, simply put an f in front of the string literal, like this:
'''

txt = f"The price is 49 dollar"
print(txt)

# Placeholders and Modifiers
price = 49
txt1 = f"The price is {price} dollar"
print(txt1)
'''
A placeholder can also include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
'''

# Example - Display the price with 2 decimals:
txt3 = f"The price is {price:.2f} dollars"
print(txt3)

txt4 = f"the price is {95:.2f} dollar"
print(txt4)

# Perform Operations in F-Strings
txt5 = f"The price is {20 * 59} dollars"
print(txt5)

# You can perform math operations on variables:
tax = 0.25
txt6 = f"The price is {price + (price * tax)} dollars"
print(txt6)

# You can perform if...else statements inside the placeholders:

txt7 = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt7)

# Execute Functions in F-Strings
fruit = "apples"
txt8 = f"I love {fruit.upper()}"
print(txt8)

# The function does not have to be a built-in Python method, you can create your own functions and use them:

def myconverter(e):
    return e * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# More Modifiers
price1 = 59000
txt9 = f"The price is {price1:,} dollar"
print(txt9)

































































































