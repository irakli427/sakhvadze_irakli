import re
input_date = input("please enter date: ") #input_date = "2024-03-22T19:17:42.956376+00:00"
pattern = r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\.\d+\+?([-+]\d{2}):(\d{2})"

match = re.match(pattern, input_date)

year = match.group(1)
month = match.group(2)
day = match.group(3)
hour = match.group(4)
minute = match.group(5)
second = match.group(6)
timezone = match.group(7)[0::2]

new_date = f"{day}-{month}-{year} {int(hour)}:{minute}:{second} {timezone}"

print(new_date)