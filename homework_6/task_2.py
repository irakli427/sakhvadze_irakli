number = int(input("please enter you number: "))

if number < 1 or number > 1000:
    print("not proper range")
else:
    print(number, end=" ")
    while number != 1:
        if number % 2 == 0:
            number = int(number/2)
            print(number, end=" ")
        elif number % 2 != 0:
            number = number*3 + 1
            print(number, end=" ")