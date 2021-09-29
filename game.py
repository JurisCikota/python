# Mainīgie

word = input('Ievadiet minamo vārdu: ').upper()
progress = "-" * len(word)
flag = False
lives = 6
try_letters = list()
try_words = list()

text = "Tev vēl ir {} dzīvības, progress: {}"

# Spēles loģika

while len(word) < 6:
    print("Ievadītais vārds ir pārāk īss!")
    word = input('Ievadiet minamo vārdu: ').upper()
    progress = "-" * len(word)
    progress = list(progress)
    text_progress = ''.join(progress)

while lives > 0 and flag == False:
    progress = list(progress)
    text_progress = ''.join(progress)
    print("\n")
    print(text.format(lives, text_progress))
    letter = input("Ievadiet minamo burtu: ").upper()
    if len(letter) == 1 and letter.isalpha():
        print("Burts atbilst prasībām!")
        if letter in word:
            print("Burts atrodas minētajā vārdā!")
            try_letters.append(letter)
            for index, burts in enumerate (word):
                if burts == letter:
                    progress[index] = letter
                    text_progress = ''.join(progress)
                if "".join(progress) == word:
                    print("Vārds ir uzminēts!")
                    print(word)
                    flag = True
        else:
            print("Burts neatrodas minētajā vārdā " + text_progress)
            lives = lives -1
            try_letters.append(letter)
            if lives == 0:
                print("Vārds nav uzminēts, spēle zaudēta!")
    elif len(letter) == len(word) and letter.isalpha():
        if letter == word:
            print("Vārds ir uzminēts!")
            print(word)
            flag = True
            break
        elif letter != word:
            for index, find_letter in enumerate (letter):
                if word.find(find_letter) != -1:
                    print("Vārds nav uzminēts, bet daži burti sakrīt")
                    break
        elif letter != word:
            print("Ievadītais vārds nesakrīt ar minamo vārdu!")
            lives = lives -1
    else:
        print("Burts neatbilst prasībām!")


     