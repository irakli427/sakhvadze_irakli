input_number = int(input("please enter number in range(1-49): "))
if input_number < 0 or input_number > 49:
    print("not proper range")
    exit(1)

for number_of_stairs in range(input_number + 1 ):
   if number_of_stairs == input_number:
        for _floor in range(number_of_stairs):
            print(" ",end="")
        print("|")
   else:
        for _floor in range(input_number- number_of_stairs):
            print(" ",end="")
        for _floor in range(number_of_stairs):
            print("/", end="")
        if number_of_stairs == 0:
            print("*")
        else:
            print("|",end="")
        for _floor in range(number_of_stairs):
            if _floor == number_of_stairs-1:
                print("\\",)
            else:
                print("\\", end="")