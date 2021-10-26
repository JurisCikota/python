import os
from .word_weight import Score

# TODO
# 1) minamie burti: A == Ā, C == Č, utt. (Taisīt translate no klases, kas atrodas failā: word_weight)
# 2) izvadīt zīmējumu karātavas! (ar progressu dzīvības)


class Game:
    def __init__(self, word):
        self.original_word = word
        self.word = word.upper()
        self.progress = "-" * len(word)
        self.lives = 6
        self.flag = False
        self.try_letters = list()
        self.try_words = list()
        self.progress = list(self.progress)
        self.text_progress = ''.join(self.progress)
        self.text = "Tev vēl ir {} dzīvības, progress: {}"
        self.letter = ''

    def play(self):
        os.system('cls')
        print (f"\nTev jāuzmin vārds, kura garums ir {len(self.word)} simboli!")
        while self.lives > 0 and self.flag == False:
            print("\n")
            print(self.text.format(self.lives, self.text_progress))
            self.letter = input("Ievadiet minamo burtu: ").upper()

            if self.letter in self.try_letters:
                print(f"Šādu burtu {self.letter} Tu jau minēji!" + " Esi uzmanīgāks")
            
            elif len(self.letter) == 1 and self.letter.isalpha():
                print("Burts atbilst prasībām!")
                if self.letter in self.word:
                    print("Burts atrodas minētajā vārdā!")
                    self.try_letters.append(self.letter)
                    print("Minētie burti: " + str(self.try_letters))
                    for index, burts in enumerate (self.word):
                        if burts == self.letter:
                            self.progress[index] = self.letter
                            self.text_progress = ''.join(self.progress)
                        if "".join(self.progress) == self.word:
                            print("Vārds ir uzminēts!")
                            self.try_words.append(self.word)
                            self.flag = True
                            break
                else:
                    
                    print("Burts neatrodas minētajā vārdā")
                    self.lives = self.lives -1
                    self.try_letters.append(self.letter)
                    print("Minētie burti: " + str(self.try_letters))
                    if self.lives == 0:
                        print(f"Vārds <> {self.original_word} <> nav uzminēts, spēle zaudēta!")

            elif len(self.letter) == len(self.word) and self.letter.isalpha():
                if self.letter == self.word:
                    print("Vārds ir uzminēts!")
                    self.try_words.append(self.word)
                    self.flag = True
                    break

                elif self.letter != self.word:
                    for index, find_letter in enumerate (self.letter):
                        if self.word.find(find_letter) != -1:
                            print("Vārds nav uzminēts, bet daži burti sakrīt")
                            break
                elif self.letter != self.word:
                    print("Ievadītais vārds nesakrīt ar minamo vārdu!")
                    self.lives = self.lives -1

            else:
                print("Burts neatbilst prasībām!")