'''
Python JSON
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.
'''

# Examples
import json

# Parse JSON - Convert from JSON to Python
#If you have a JSON string, you can parse it by using the json.loads() method.
#The result will be a Python dictionary.

# Convert from JSON to Python: 
a = '{"name":"John", "age":30, "city": "New York"}'

b = json.loads(a)

print(b["age"])


# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

c = {
    "name": "Masuma",
    "age": 30,
    "city": "JPR"
    }

d = json.dumps(c)
print(d)


'''
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
'''

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
'''

# Convert a Python object containing all the legal data types:
e = {
    "name": "Maheera",
    "age": 3,
    "married": False,
    "divorced": False,
    "children": ("No", "None"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
        ]
    }
print(json.dumps(e))

# Format the Result
print(json.dumps(e, indent=4))

# Use the separators parameter to change the default separator:
print(json.dumps(e, indent=4, separators=(". ", " - ")))


# Order the Result
print("-----------Order the Result-----------")
print(json.dumps(e, indent=4, sort_keys=True))


'''
Challenge: JSON
Test your understanding of Python json by completing a small coding challenge.

Instructions
Inside the editor, complete the following steps:
Import the json module
Create a variable x with this JSON string: '{"name": "Emil", "age": 30}'
Convert the JSON string into a Python dictionary and store it in y
Print the age from y
'''



















