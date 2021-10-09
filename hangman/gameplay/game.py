import getpass

class Game:
    def __init__(self, word):
        self.word = word.upper()
        self.progress = "-" * len(word)
        self.lives = 6
        self.flag = False
        self.try_letters = list()
        self.try_words = list()
        self.progress = list(self.progress)
        self.text_progress = ''.join(self.progress)
        self.text = "Tev vēl ir {} dzīvības, progress: {}"

    def play(self):
        self.word_length()
        while self.lives > 0 and self.flag == False:
            print("\n")
            print(self.text.format(self.lives, self.text_progress))
            letter = input("Ievadiet minamo burtu: ").upper()

            if len(letter) == 1 and letter.isalpha():
                print("Burts atbilst prasībām!")
                if letter in self.word:
                    print("Burts atrodas minētajā vārdā!")
                    self.try_letters.append(letter)
                    for index, burts in enumerate (self.word):
                        if burts == letter:
                            self.progress[index] = letter
                            self.text_progress = ''.join(self.progress)
                        if "".join(self.progress) == self.word:
                           print("Vārds ir uzminēts!")
                           print(self.word)
                           self.flag = True
                           break
                else:
                    print("Burts neatrodas minētajā vārdā " + self.text_progress)
                    self.lives = self.lives -1
                    self.try_letters.append(letter)
                    if self.lives == 0:
                        print("Vārds nav uzminēts, spēle zaudēta!")

            elif len(letter) == len(self.word) and letter.isalpha():
                if letter == self.word:
                    print("Vārds ir uzminēts!")
                    print(self.word)
                    self.flag = True
                    break
                elif letter != self.word:
                    for index, find_letter in enumerate (letter):
                        if self.word.find(find_letter) != -1:
                            print("Vārds nav uzminēts, bet daži burti sakrīt")
                            break
                elif letter != self.word:
                    print("Ievadītais vārds nesakrīt ar minamo vārdu!")
                    self.lives = self.lives -1

            else:
                print("Burts neatbilst prasībām!")

    def word_length(self):
        while len(self.word) < 6:
            print("Ievadītais vārds ir pārāk īss!")
            self.word = getpass.getpass('Ievadiet minamo vārdu: ').upper()
            self.progress = "-" * len(self.word)
            self.progress = list(self.progress)
            self.text_progress = ''.join(self.progress)