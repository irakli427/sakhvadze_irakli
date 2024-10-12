from random import randint

comp_number = randint(0,100)
attempt_counter = 0
while attempt_counter <= 10:
    guess_number = int(input("what is your guess: "))
    if guess_number > comp_number:
        print("high")
        attempt_counter += 1
    elif guess_number < comp_number:
        print("low")
        attempt_counter += 1
    else:
        print("you are winner")
        attempt_counter += 1
        break
if attempt_counter > 10:
    print("comp is winner")