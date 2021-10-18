from gameplay.game import Game
import getpass
import os
import random

with open('data/words.txt', 'r', encoding='utf-8') as file:
    lines = file.read()
    words = lines.split('\n')

random.shuffle(words)
guessed_words = list()

while True:
    word = words.pop()
    game = Game(word)
    game.play()

    guessed_words.append(''.join(game.try_words))
    print(f"Guessed words: {', '.join(guessed_words)}")

    print('\n' + "_"*70)

