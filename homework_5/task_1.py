number = int(input("please enter number in range(1-49): "))

if number < 1 or number > 49:
    print('not proper range')
    exit(1)

number_1 = 1
divisor = 1

while number_1 <= number:
        print(number_1,end="- ")
        count_of_divisors = 1
        divisor = 1
        while divisor <= number_1 and count_of_divisors < 4:
            if number_1 % divisor == 0:
                if count_of_divisors !=3 and divisor != number_1:
                    print(divisor,end= " ")
                else:
                    print(divisor)
                count_of_divisors += 1
            divisor +=1
        number_1 +=1