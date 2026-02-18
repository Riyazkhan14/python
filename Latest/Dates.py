'''
Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

Example
Import the datetime module and display the current date:
'''

import datetime

x = datetime.datetime.now()
print(x)

'''
Date Output
When we execute the code from the example above the result will be:

2026-02-17 15:26:23.380395
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:

Example
Return the year and name of weekday:
'''

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects

y = datetime.datetime(2020, 5, 17)

print(y)

# The strftime() Methods

'''
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
'''

print(y.strftime("%B"))



































