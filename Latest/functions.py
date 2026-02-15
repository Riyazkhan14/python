def my_function():
    print("Hello World!, from function")
    
my_function()

'''
Function Names
Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)
'''

'''
Why need function. So to prevent write same code again and again we can use function to write once
'''

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/ 9

print(fahrenheit_to_celsius(77))


def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

# or
print(get_greeting())

# Non as return

def y_f():
    None

def y():
    pass
