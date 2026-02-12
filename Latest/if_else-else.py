a = 200
b = 33
if  b > a:
    print(" b is Big")
else:
    print("B is not Big")

# Else Without Elif
number = 7

if number % 2 ==0:
    print("this number is even")
else:
    print("This number is odd")

# Complete If-Elif-Else Chain
temp = 22
if temp > 30:
    print("It's hot outside!")
elif temp > 20:
    print("it's Warm Outside")
elif temp > 10:
    print("It's Cool outside")
else:
    print("It's Cold Outside")

# Else as Fallback
username = "Emil"
if len(username) > 0:
    print(f"Welcome, {username}")
else:
    print("Error: Username cannot be empty")
