from datetime import date

year = int(input("დაბადების წელი: "))
if year <=0 or year % 1 != 0:
    print("უნდა შეიყვანოთ მხოლოდ დადეითი რიცხვი")
    exit(1)

month = int(input("დაბადების თვე (ციფრებში) : "))
if month <=0 or month > 12 or month % 1 != 0:
    print("უნდა შეიყვანოთ მხოლოდ ნატურალური რიცხვი 1 დან 12 ის ჩათვლით")
    exit(1)

day = int(input("დაბადების რიცხვი: "))
if day  <=0 or day > 31 or day % 1 != 0:
    print("უნდა შეიყვანოთ მხოლოდ ნატურალური რიცხვი 1 დან 31 ის ჩათვლით")
    exit(1)

birth_date = date(year, month, day)
num_of_weekday = date.weekday(birth_date)

if num_of_weekday == 0:
    week_day ='ორშაბათი'
elif num_of_weekday == 1:
    week_day ='სამშაბათი'
elif num_of_weekday == 2:
    week_day ='ოთხშაბათი'
elif num_of_weekday == 3:
    week_day ='ხუთშაბათი'
elif num_of_weekday == 4:
    week_day ='პარასკევი'
elif num_of_weekday == 5:
    week_day ='შაბათი'
else:
    week_day = 'კვირა'

print(f"დაბადების დღე იყო {week_day}.")