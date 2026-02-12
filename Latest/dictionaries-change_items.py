thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
    }

thisdict["year"] = 2018
print(thisdict)


# Update
thisdict.update({"year" : 2020})
print(thisdict)

# Adding
thisdict["color"] = "red"
print(thisdict)
