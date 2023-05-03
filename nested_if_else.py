winning_number = 27
user_input = int(input("Guess a numbe between 1 to 100 : "))
if user_input == winning_number:
    print("You WON !!!")
else:
    if user_input > winning_number:
        print("Too High Number")
    else:
        print("Too Low")
