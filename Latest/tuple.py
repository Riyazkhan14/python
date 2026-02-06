mytuple = ("apple", "banana", "cherry")
print(mytuple)

'''
Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
'''
#Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length
print(len(thistuple))

#Create Tuple With One Item
thistuple1 = ("apple",)
print(type(thistuple1))

#NOT a tuple
thisisnottuple = ("apple")
print(type(thisisnottuple))

#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

print(tuple1, tuple2, tuple3, tuple4)

#The tuple() Constructor
thistuple5 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple5)
