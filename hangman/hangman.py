from gameplay.game import Game
import os
import random

#TODO
# 1 import os atlasīt tagadējo direktoriju
# 2 play again papildināt ar grūtību izvēlni!

cur_dir = os.path.dirname(__file__)
path = os.path.join(cur_dir, "data", 'words.txt')

with open(path, 'r', encoding='utf-8') as file:
    lines = file.read()
    words = lines.split('\n')

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