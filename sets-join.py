'''
Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

'''

# Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set5 =  set1.union(set2)
print(set5)

# Pipe |
set6 = set1 | set2
print(set6)

# multiple sets
myset = set1.union(set2, set3, set4)
myset1 = set1 | set2 | set3 | set4
print(f"This is union join {myset}")
print(f"this is | sign join {myset1}")

# Join Sets and tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Update
set1.update(set2)
print(set1)

# Intersection
set10 = {"apple", "banana", "cherry"}
set20 = {"google", "microsoft", "apple"}

set30 = set10 & set20
set40 = set10.intersection(set20)
set10.intersection_update(set2)
print(set40)
print(set30)
print(set10)


print("----------")

set11 = {"apple", "banana", "cherry"}
set22 = {"google", "microsoft", "apple"}

# Difference
set33 = set11.difference(set22)
print(set33)

set34 = set11 - set22
print(set34)

set11.difference_update(set22)
print(set11)

# Symmetric Differences : The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set35 = set11.symmetric_difference(set22)
print(set35)

set36 = set11 ^ set22
print(set36)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set11.symmetric_difference_update(set22)
print(set11)















