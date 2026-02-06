thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


for i in range(len(thislist)):
    print(thislist[i])

p = 0
while p < len(thislist):
    print(thislist[p])
    p += 1
    
print("---------------------------")

[print(x) for x in thislist]
