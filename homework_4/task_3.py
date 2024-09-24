number = int(input("please enter number (1 to 999): "))

if number < 0 or number > 999:
    print("not from the proper range")
    exit(1)
for divisors in range(1,number+1):
    if number % divisors == 0:
        print(divisors,end=" ")