computer_choice = "rock"

user_choice = input("Which do you choose? rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print ("computer chose " + computer_choice)
    print("tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print ("computer chose " + computer_choice)
    print("user wins!")
elif user_choice == "scissors" and computer_choice == "paper":
    print ("computer chose " + computer_choice)
    print("user wins!")
elif user_choice == "paper" and computer_choice == "rock":
    print ("computer chose " + computer_choice)
    print("user wins!")
else:
    print ("computer chose " + computer_choice)
    print("computer wins")


    