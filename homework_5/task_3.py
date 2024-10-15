input_number = int(input("please enter number in range(0-19): "))
if input_number < 0 or input_number > 19:
    print("not proper range")
    exit(1)

first_number = 0
second_number = 1

if input_number == first_number:
    print(first_number)
elif input_number == second_number:
    print(first_number,second_number)
else:
    print(first_number,second_number,end=" ")
    while second_number + first_number <= input_number:
        next_variable = first_number + second_number
        temp_variable = second_number
        second_number = next_variable
        first_number = temp_variable
        print(second_number, end=" ")