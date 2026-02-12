'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)


for y in "banana":
    print(y)

# Break
for z in fruits:
    print(z)
    if z == "banana":
        break

for a in fruits:
    if a == "banana":
        break
    print(a)

print("-------------Continues Starts")
# Continue

for m in fruits:
    if m == "banana":
        continue
    print(m)

for n in fruits:
    if n == "banana":
        print(n)
    continue

# Range

for h in range(6):
    print(h)


for g in range(2, 6):
    print(g)

for d in range(2, 30, 3):
    print(d)

# Else
for t in range(6):
    print(t)
else:
    print("Finally Finished")

# Break will not execute
for s in range(6):
    if s == 3: break
    print(s)
else:
    print("Finally Finished")
