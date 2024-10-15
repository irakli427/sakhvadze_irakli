from math import ceil,floor
word = input("please enter the word: ").strip()
counter = 0
length = len(word)
middle_letter_index = (length-1)/2
middle_1 = floor(middle_letter_index)
middle_2 = ceil(middle_letter_index)
while counter < 5:
    print(f'first letter is : {word[0]}  ',f'last letter is : {word[-1]}  ',f'middle letter(s) : {word[middle_1:middle_2 + 1]}  ')
    counter += 1