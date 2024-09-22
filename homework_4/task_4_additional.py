n = int(input("pleaase enter integer number (1 to 19): "))

list = []

if n < 0 or n > 19:
    print("not from the proper range")
    exit(1)
else:
    for i in range(n+1):
        if i < 2:
            next_number = i
        else:
            next_number = list[i-1] + list[i-2]
        list.append(next_number)
    print(f' მიმდევრობის მე-{n} წევრია: {list[n]}')
