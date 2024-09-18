number_one = int(input("please enter first number:"))
number_two = int(input("please enter second number:"))

whole_division = number_one // number_two
division = number_one / number_two

if division >= 1 and division == whole_division:
    print("პირველი რიცხვი მორეს ჯერადია")
else:
    print("პირველი რიცხვი არ არის მეორეს ჯერადი")
