# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
thisset.discard("apple")
print(thisset)


# pop
thisset1 = {'mango', 'apple', 'cherry', 'orange', 'pineapple', 'banana', 'papaya'}
x = thisset1.pop()
print(x)
print(thisset1)


# clear
thisset1.clear()
print(thisset1)

thisset2 = {'mango', 'apple', 'cherry', 'orange', 'pineapple', 'banana', 'papaya'}
del thisset2
print(thisset2)
