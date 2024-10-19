first = input("please enter the first word/statement: ").strip().lower()
second = input("please enter the second word/statement: ").strip().lower()
output = 'YES'

if len(first) != len(second):
    output = 'NO'
elif len(first) == len(second):
    for letter in first:
        if first.count(letter) != second.count(letter):
            output = 'NO'

print(output)