word = input("please enter the word: ").strip()

for i in word:
    if i not in "aeiou":
        print(i,end="")