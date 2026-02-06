#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Add tuple to a tuple.
z = ("mango",)
thistuple += z
print(thistuple)

#Remove Items
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Delete tuple
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
