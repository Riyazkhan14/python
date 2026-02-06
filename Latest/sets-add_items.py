# Python - Add Set Items
'''
Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.
'''

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

print("Add Sets -----------------------")

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset, end="\n")

# Add Any Iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print("-------------------------------")
print(thisset)
