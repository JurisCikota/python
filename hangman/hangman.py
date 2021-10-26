from gameplay.game import Game
import os #atlasīt tagadējo direktoriju
import random

with open('data/words.txt', 'r', encoding='utf-8') as file:
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