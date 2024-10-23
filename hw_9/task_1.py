n = int(input("please enter the number(more than 1): "))
if n <= 1:
    print("not proper range")
    exit(1)

i = 1
x = 0
sign = 1
while i <= n:
    x += (1/(2*i-1))*(sign)
    i += 1
    sign *= -1
x = x * 4
print(x)
print('ცვლადის მნიშვნელობა უახლოვდება 3,14 (π) რაც n იზრდება')