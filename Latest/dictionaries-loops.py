thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# keys
for x in thisdict:
    print(x)

for m in thisdict.keys():
    print(m)

# values
for y in thisdict:
    print(thisdict[y])

for z in thisdict.values():
    print(z)

# look through both keys and values using items
for r,r1 in thisdict.items():
    print(f"key {r} and value {r1}")
