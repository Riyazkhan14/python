import random
winning_number = random.randint(1, 100)
number = int(input("Guess a number between 1 to 100: "))
guess_number = 1
game_over = False

while not game_over:
    if number == winning_number:
        print(f"you won, you guess the number in {guess_number} times")
        game_over = True
    else:
        if number > winning_number:
            print("Too High")
        else:
            print("Too Low")
        guess_number += 1
        number = int(input("Guess Again: "))