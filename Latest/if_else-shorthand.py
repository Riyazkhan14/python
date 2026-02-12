a = 5
b = 2
if a > b: print("a is greater than b")

# Short Hand if .. Else
print("A") if a > b else print("B")


#Assign a Value With If ... Else
a = 10
b = 20

bigger = a if a > b else b
print("Bigger is", bigger)

# Multiple Conditions on One Line
print("A") if a > b else print("=") if a == b else print("B")

# Ternary operators

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value :", max_value)


username = ""
display_name = username if username else "Guest"
print("Welcome", display_name)
