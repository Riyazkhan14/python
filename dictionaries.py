# Dictionaries
'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:
'''

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "Year" : 1964,
    "colors" : ["red", "white", "blue"]
    }
print(thisdict)


# Dictionary Items
print(thisdict["brand"])


print(len(thisdict))

print(type(thisdict))


# The dict() Constructor

thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)
