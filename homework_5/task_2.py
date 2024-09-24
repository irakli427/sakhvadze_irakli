begging_number = 1

while begging_number < 10:
    second_number = 1
    while second_number <= begging_number:
        if second_number == begging_number:
            print(f'{second_number} * {begging_number} = {begging_number*second_number}')
        else:
            print(f'{second_number} * {begging_number} = {begging_number * second_number}',end= "  ")
        second_number +=1
    begging_number +=1