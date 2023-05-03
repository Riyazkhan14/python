user_input = int(input("Guess a number between 1 to 100 : "))

winning_number = 27

if user_input == winning_number:
    print("You Won !!!")
else:
    if user_input < winning_number:
        print("Too low")
    else:
        print("Too High")
