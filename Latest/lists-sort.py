#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print(thislist1)

#Sort Descending
thislist2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist2.sort(reverse = True)
print(thislist2)

thislist3 = [100, 50, 65, 82, 23]
thislist3.sort(reverse = True)
print(thislist3)

print("#Customize Sort Function")
def myfunc(n):
    return abs(n - 50)

thislist4 = [100, 50, 65, 82, 23]
thislist4.sort(key = myfunc)
print(thislist4)

#Case Insensitive Sort
thislist5 = ["banana", "Orange", "Kiwi", "cherry"]
thislist5.sort()
print(thislist5)

thislist6 = [item.upper() for item in thislist5]
print(thislist6)

print("--------------------------")
thislist5.sort(key = str.lower)
print(thislist5)

#Reverse Order
thislist5.reverse()
print(thislist5)
