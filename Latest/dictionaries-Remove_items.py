thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# Pop Item will remove last insertion
thisdict.popitem()
print(thisdict)

# Remove
del thisdict["brand"]
print(thisdict)

# Delete
del thisdict
print(thisdict) # this will cause error as dictionery is not available.

# Clear
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.clear()
print(thisdict2)
