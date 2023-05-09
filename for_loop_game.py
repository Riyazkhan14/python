# you can use Random library to assign the random number .

winning_number = 43
guess = 1
number = int(input("Guess a number between 1 and 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"you win, you huessed this number in {guess} times")
        game_over = True
    else:
        if number > winning_number:
            print("Too High")
            guess += 1
            number = int(input("Guess Again: "))
        else:
            print("Too Low")
            guess += 1
            number = int(input("Guess Again: "))