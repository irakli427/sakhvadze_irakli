from random import randint

n = int(input("please enter n (1 to 29): "))
number = 0

if n < 1 or n > 29:
    print("not from the proper range")
    exit(1)
else:
    for i in range(n):
        number_new = randint(0,1001)
        if number_new > number:
            number = number_new
    print(number)