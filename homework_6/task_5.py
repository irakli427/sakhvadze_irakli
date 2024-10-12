number = int(input("please enter you number(0,10): "))

if int(number) < 1 or int(number) >= 10:
    print("not proper range")
    exit(1)

counter_1 = 0
counter_2 = 0

while counter_1 <= number:
    print("  "*(number-counter_1),end=" ")
    counter_2 = 0
    while counter_2 <= counter_1*2:
        print(abs(counter_2-counter_1),end=" ")
        counter_2 +=1
    print(" "*(number-counter_1))
    counter_1 += 1