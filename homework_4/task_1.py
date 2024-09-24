from random import randint

player_numbers = int(input("please enter player numbers: "))

if player_numbers < 1:
    exit(1)
else:
    for i in range(1,player_numbers+1):
        dice_one = randint(1, 6)
        dice_two = randint(1, 6)
        print(f"player {i}: ",dice_one, dice_two)