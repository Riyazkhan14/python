x = 12 # 42

if x > 10:
    print("Above ten, ", end="")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


# Example

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")


# Multiple Levels of Nesting

score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Passed with good standing")
        else:
            print("Passed but missing assignment")
    else:
        print("Passed but low attendance")
else:
    print("Failed")


# Nested If vs Logical Operators

tempreture = 25
is_sunny = True

if tempreture > 20:
    if is_sunny:
        print("perfect Beach Weather!")
        

if tempreture > 20 and is_sunny:
    print("Perfect beach weather using and operator")

# Login validation with nested checks

uname = "Emil"
passwd = "python123"

is_active = True

if uname:
    if passwd:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password required")
else:
    print("Username required")



# Grade Calculator

scr = 92
extra_credit = 5

if score >= 90:
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A Grade")
elif score >= 80:
    print("B grade")
else:
    print("C grade")























