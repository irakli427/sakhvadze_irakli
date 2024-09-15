# begin

a = int(input("enter length of first side:"))

b = int(input("enter length of second side:"))

c = int(input("enter length of third side:"))

P = a +b +c

S = (P/2 * (P/2-a)*(P/2-b)*(P/2-c))**0.5

print(f"პერიმეტრი არის {P}")
print(f"ფართობი არის {S}")

