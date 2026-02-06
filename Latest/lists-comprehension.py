fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)

newlist1 = [x for x in fruits if "a" in x]
print(newlist1)


apple = [x for x in fruits if x != "apple"]
print(apple)


newlist2 = [x for x in range(10)]
print(newlist2)

newlist3 = [x for x in range(10) if x < 5]
print(newlist3)


newlist4 = [x.upper() for x in fruits]
print(newlist4)

newlist5 = ['hello' for x in fruits]
print(newlist5)

newlist6 = [x if x != "banana" else "orange" for x in fruits]
print(newlist6)
