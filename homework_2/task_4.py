speed = int(input("please enter the speed: "))

if speed >= 120:
    print("very fast")
elif speed >= 60:
    print("fast")
elif speed >= 30:
    print("moderate")
else:
    print("slow")