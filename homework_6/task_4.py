number = int(input("please enter you number(0,10): "))

if int(number) < 1 or int(number) >= 10:
    print("not proper range")
    exit(1)
counter_1 = 1
counter_2 = 1

while counter_1 < number:
    counter_2 = 1
    while counter_2 <= counter_1:
        if counter_2 != counter_1:
            print(counter_2,end= " ")
        else:
            print(counter_2)
        counter_2 +=1
    counter_1+=1
while counter_1 <= number:
    counter_2 = 1
    while counter_2 <= counter_1:
        if counter_2 != counter_1:
            print(counter_2,end= " ")
        else:
            print(counter_2)
        counter_2 +=1
    counter_1 -=1