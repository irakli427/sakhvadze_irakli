statement = input("please enter you word/statement: ")
letters = 'abcdefghijklmnopqrstuvwxyz'

for letter in statement:
    if letter not in letters and letter not in letters.upper():
        statement = statement.replace(letter,"")

statement = statement.lower()
if statement[0:] == statement[-1::-1]:
    print('Is palindrome')
else:
    print('Is not palindrome')