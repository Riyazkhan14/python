# the and operator
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both Condition are true")


# not operator

a = 33
b - 200

if not a > b:
    print("a is NOT greater than b")

# Combining Multiple Operators

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount Applies")

#examples - 
# Using Parentheses for Clarity

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")

# User authentication check:
username = "Riyaz"
password = "secret123"
is_varified = True

if username and password and is_varified:
    print("Login successful")
else:
    print("Login Failed")

# Range Checking

score = 85
if score >= 0 and score <= 100:
    print("Valid Score")
else:
    print("Invalid score")


























