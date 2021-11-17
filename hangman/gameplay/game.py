import os
from scripts.word_weight import Score
<<<<<<< HEAD
from scripts.timer import timer
# TODO
# izvadīt zīmējumu karātavas! (ar progressu dzīvības)
# pulkstenis
from gameplay.graphics import Graphics

# TODO
# izvadīt zīmējumu karātavas! (ar progressu dzīvības)
# pulkstenis
# increase level if word has been guessed
# janis izmainas 11:18
#  print self.lives = Graphics()
#GRleft = Graphics(self.lives)
=======
import msvcrt
import time
from gameplay.graphics import Graphics

class Game:
    """Main game class, use to execute game.

    Create class using one word as atribute, this word will be needed to guess.
    To play game need to execute play() function!

    Typical usage example:

    game1 = Game(word)
    game1.play()
    """
>>>>>>> e343c4154a761d5b0b295d800001ec1064f59c2e

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
<<<<<<< HEAD
        

    def play(self):
        os.system('cls')
=======
    
    def countdown(self):
        self.a = ''
        self.t = 20
        print("Tev ir dotas 20 sekundes, lai uzminētu burtu!\nIevadiet minamo burtu!")
        while self.t:
            if msvcrt.kbhit(): #msvcrt - MS VC++ runtime
                self.a = msvcrt.getwch()
                break
            print(f"{self.t}", end=' ', flush=True)
            time.sleep(1)
            self.t -= 1
        if self.t == 0:
            print("\nLaiks ir beidzies!")
            self.lives = self.lives -1
        os.system('cls')
        return self.a

    """Prints out countdown.

    Print out countdown. countdown can be interupted with keyboard key press,
    when this behaviour happens it reads what key has been pressed.

    Returns:
        keyboard pressed key in unicode format
    """
        

    def play(self):
>>>>>>> e343c4154a761d5b0b295d800001ec1064f59c2e
        GRleft = Graphics()
        translate = Score(self.word)
        tr = translate.translate()
        if translate.total_score() < 100:
            print (f"\nTev jāuzmin vārds, kura garums ir {len(self.word)} simboli! Viegls vārds!")
        elif translate.total_score() >= 100 and translate.total_score() <= 150:
            print (f"\nTev jāuzmin vārds, kura garums ir {len(self.word)} simboli! Vidēji grūts vārds!")
        else:
            print (f"\nTev jāuzmin vārds, kura garums ir {len(self.word)} simboli! Grūts vārds!")
        while self.lives > 0 and self.flag == False:
            print('\n' + "_"*70 + "\n")
            print(self.text.format(self.lives, self.text_progress))
<<<<<<< HEAD
            #laiks = timer()
            #laiks.time()
            GRleft.printGR(self.lives)
            self.letter = input("Ievadiet minamo burtu: ").upper()
=======
            GRleft.printGR(self.lives)
            self.countdown()
            if self.lives == 0:
                GRleft.printGR(self.lives)
            self.letter = self.a.upper()
>>>>>>> e343c4154a761d5b0b295d800001ec1064f59c2e
            
            if self.letter in self.try_letters:
                print(f"Šādu burtu {self.letter} Tu jau minēji!" + " Esi uzmanīgāks")
                print("Minētie burti: " + str(self.try_letters))
            elif self.letter == '':
                print(f"\nLaiks ir beidzies! Mēģini iekļauties 20 sekunžu minēšanas laikā!")
                print("Minētie burti: " + str(self.try_letters))
            elif len(self.letter) == 1 and self.letter.isalpha():
                print("Burts atbilst prasībām!")
                if self.letter in str(tr).upper():
                    print("Burts atrodas minētajā vārdā!")
                    self.try_letters.append(self.letter)
                    print("Minētie burti: " + str(self.try_letters))
                    for index, burts in enumerate (self.word):
                        burts_translate = Score(burts)
                        btr = burts_translate.translate()
                        if str(btr).upper() == self.letter:
                            self.progress[index] = burts
                            self.text_progress = ''.join(self.progress)
                        if "".join(self.progress) == self.word:
                            print("Vārds ir uzminēts!")
                            self.try_words.append(self.word)
                            self.flag = True
                            break
                else:
                    
                    print("Burts neatrodas minētajā vārdā")
                    self.lives = self.lives -1
          #         print self.lives = Graphics()
                    self.try_letters.append(self.letter)
                    print("Minētie burti: " + str(self.try_letters))
                    if self.lives == 0:
                        GRleft.printGR(self.lives)
                        print(f"\nVārds <> {self.original_word} <> nav uzminēts, spēle zaudēta!")

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
   