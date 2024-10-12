number = input("please enter you number(0,1000): ")

if int(number) < 1 or int(number) >= 1000:
    print("not proper range")
    exit(1)

print(f"entered number is : {number}")
counter = 0
length = len(number)
sum_counter = 0
print("reversed number is :", end=" ")

while counter < length:
    digit = number[length - counter - 1]
    if counter != length - 1:
        print(digit,end="")
    else:
        print(digit)
    counter += 1
    sum_counter += int(digit)
print(f"sum of digits : {sum_counter}")