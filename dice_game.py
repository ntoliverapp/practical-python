import random

def roll_dice():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    # dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_1, dice_2

def player_names(players):
    print(players, "Lets get started")

def main():
    player_one = input("Enter Player One's name: ")
    player_names(player_one)
    player_two = input("Enter Player Two's name: ")
    player_names(player_two)

    roll_1 = roll_dice()
    roll_2 = roll_dice()

    print(player_one, " rolled ", roll_1)
    print(player_two, " rolled ", roll_2)

    if roll_1 > roll_2:
        print(player_one, "wins!")
    elif roll_1 == roll_2:
        print(player_one, " and ", player_two, " tied.")
    else:
        print(player_two, " wins!")

main()