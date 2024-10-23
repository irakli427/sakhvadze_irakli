from random import uniform
from math import sqrt

n = int(input("please enter the number(more than 1): "))
if n <= 1:
    print("not proper range")
    exit(1)
i = 0
counter = 0
while i <= n:
    a = uniform(0, 1)
    b = uniform(0, 1)
    while a == 0:
        a = uniform(0,1)  #uniform მოიცავს საწყის წერტილს და რომ ავირიდოთ 0
    while b == 0:
        b = uniform(0,1)
    if sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1
    i += 1

result = counter * 4 / n
print(result)
print('ცვლადის მნიშვნელობა უახლოვდება 3,14 (π) რაც n იზრდება')