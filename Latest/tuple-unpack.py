# Packing Tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Unpacking a Tuple
(green, yellow, red) = fruits

print(green, yellow, red, "----")

# Using Asterisk*
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits1

print(green)
print(yellow)
print(red)


(green, *tropic, red) = fruits1
print(green)
print(tropic)
print(red)
