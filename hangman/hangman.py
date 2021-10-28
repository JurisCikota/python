from gameplay.game import Game
from scripts.split_difficulty import Diffculty
import os
import random

os.system('cls')
print('\n' + "_"*90)
print("\n" + " "*30 + "Welcome to Hangman game!\n")
print('\n' + "_"*90)
difficulty = Diffculty()
difficulty.file_exists()
difficulty.write_files()
words = difficulty.choose_difficulty()

random.shuffle(words)
guessed_words = list()
print_words = ''

while True:
    word = words.pop()
    game = Game(word)
    game.play()
    n = 0
    

    if len(game.try_words) > 0:
        guessed_words.append(''.join(game.try_words))
        if len(guessed_words) > n:
            print_words = ', '.join(guessed_words)
            n = n + 1
    print(f"\nGuessed word: {print_words}")

    print('\n' + "_"*70)
    play_again = input("\nVai vēlies spēli turpināt? \nyes / no\n")
    if play_again not in ["yes", "ye", "y"]:
        break
    else:
        words = difficulty.choose_difficulty()