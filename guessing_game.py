# The computer will choose a random number between 1–100 and ask the user to guess the number

import random
computer_guess = random.randint(0,100)
print(computer_guess)

guess = int(input("guess the number between 1 and 100: "))

# Once the user guesses, the computer will tell the user if their guess was too high or too low

while computer_guess:
    if guess == computer_guess:
        print("your guess is: ", guess, "\n", "computer's guess is: ", computer_guess, "\n")
        print("thats correct!")
        break
    elif guess < computer_guess:
        print("your guess is: ", guess, "\n", "computer's guess is: ", computer_guess, "\n")
        print ("your guess is too low")
        guess = int(input("guess again: "))

    else: 
        print("your guess is: ", guess, "\n", "computer's guess is: ", computer_guess, "\n")
        print ("your guess is too high")
        guess = int(input("guess again: "))

# The game is over once the user guesses the computer’s number. When the game is over, the computer the total number of guesses the user made before getting the right answer.