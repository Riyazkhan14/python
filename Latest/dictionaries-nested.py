myfamily1 = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily1)

child1 = {
    "name" : "Maheera",
    "year" : 2023
    }
child2 = {
    "name" : "Gungun",
    "year" : 2003
    }
child3 = {
    "name" : "Masuma",
    "year" : 1993
    }

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
    }


print(myfamily)


# Access
print(myfamily1["child2"]["name"])
print(myfamily["child3"]["name"])


#Loop Through Nested Dictionaries
for x, obj in myfamily1.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
