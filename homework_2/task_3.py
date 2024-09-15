number = int(input("please choose the whole number between 0 and 10: "))

list = []

whole_division_2 = number // 2
whole_division_3 = number // 3
whole_division_5 = number // 5
whole_division_7 = number // 7

if number <= 0 or number > 10:
    print("not correct range")
else:
    if whole_division_2 ==number/2:
        list.append(2)
    if whole_division_3 ==number/3:
        list.append(3)
    if whole_division_5 ==number/5:
        list.append(5)
    if whole_division_7 ==number/7:
        list.append(7)

if len(list) > 1:
    print(list[0],list[1])
elif len(list) == 1:
    print(list[0])
else:
    print("empty space")