thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = thisdict["model"]

print(x)

# get
y = thisdict.get("year")
print(y)

z = thisdict.keys()
print(z)

# Update the Keys
thisdict["color"] = "White"
thisdict["year"] = 2004
print(thisdict)

# Get Values
a = thisdict.values()
print(a)


# Get Items - The items() method will return each item in a dictionary, as tuples in a list.

b = thisdict.items()
print(b)


# Check if Key Exists

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the Dict")
