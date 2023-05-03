# Show Ticket Pricing
# 1 to 3 Free
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = int(input("Enter your age : "))

# if age == 0 or age > 0:
#   print("You can't play the game")
# elif istead of if

if 0<age<=3:
    print("Hurray!!! Ticket is free")
elif 3<age<=10:
    print("Ticket Price is 150")
elif 10<age<=60:
    print("Ticket Price is 250")
elif 60<=age:
    print("Ticket Price is 200")
else:
    print("You are not eligible to play games")