line_1 = 'qwertyuiop'
line_2 = 'asdfghjkl'
line_3 = 'zxcvbnm'
word = ""

enter_action = input("enter action \'e\' (ecryption) or \'d\' (decryption): ")

if enter_action not in "ed":
    print("only \'e\' or \'d\' letters")
    exit(1)
enter_text = input("please text: ").strip()

for letter in enter_text:
    if letter not in line_1 + line_2 + line_3:
        word += letter
    else:
        if line_1.find(letter) != -1:
            line = line_1
        elif line_2.find(letter) != -1:
            line = line_2
        else:
            line = line_3
        _index = line.find(letter)
        if enter_action == "e":
            new_letter = line[_index-len(line)+1]
        if enter_action == "d":
            new_letter = line[_index-1]
        word += new_letter
print(word)
