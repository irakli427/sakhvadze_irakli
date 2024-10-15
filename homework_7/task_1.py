word = input("please enter the word: ").strip()

for i in word[0::2]:
    if i != "e":
        print(i,end="")