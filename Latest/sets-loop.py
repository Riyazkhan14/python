thisset = {'mango', 'apple', 'cherry', 'orange', 'pineapple', 'banana', 'papaya'}

for x in thisset:
    print(x)

'''
i = 0
while i < len(thisset):
    print(thisset(i))
    i += 1
    '''

items = list(thisset)
i = 0

while i < len(items):
    print(items[i], end=", ")
    i += 1
