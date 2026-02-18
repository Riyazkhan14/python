'''
Python Try Except
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:
'''

# The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("An exception occured")

'''
Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error:
'''
# Many Exceptions - You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:


# Example - Print one message if the try block raises a NameError and another for other errors:

try:
    print(x)
except NameError:
    print("Variable x in not defined")
except:
    print("Something else went wrong")

# In this example, the try block does not generate any error:
try:
    print("Hello")
except:
    print("Something Went wrong")
else:
    print("Nothing went wrong")

# Finally - The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print(a)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


# Try to open and write to a file that is not writable:

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


# Raise an exception
c = -1
if c < 0:
    raise Exception("Sorry, no numbers below zero")

d = "hello"

if not type(d) is int:
    raise TypeError("Only integers are allowed")


'''
Challenge: Try...Except
Test your understanding of Python try...except by completing a small coding challenge.

Instructions
Inside the editor, complete the following steps:
Write a try block that tries to print a variable x (which is not defined)
Write an except block that prints "An error occurred"
Write a finally block that prints "Execution complete"
'''

















































