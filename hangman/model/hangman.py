from gameplay.game import Game
from scripts.split_difficulty import Diffculty
import os
import random
import requests


os.system('cls')
print('\n' + "_" * 90)
print("\n" + " " * 30 + "Welcome to Hangman game!\n")
print('\n' + "_" * 90)
difficulty = Diffculty()
difficulty.file_exists()
difficulty.write_files()

words_viegls = difficulty.generate_difficulty("viegls")
words_videjs = difficulty.generate_difficulty("videjs")
words_gruts = difficulty.generate_difficulty("gruts")

random.shuffle(words_viegls)
random.shuffle(words_videjs)
random.shuffle(words_gruts)
guessed_words = list()
print_words = ''

while True:

    n = 0

    difficulty = input("\nChoose difficulty (type 1 ,2 ,3, 4):"
                       + "\n 1 Easy   - Latvian word from words.txt"
                       + "\n 2 Normal - Latvian word from words.txt"
                       + "\n 3 Hard   - Latvian word from words.txt"
                       + "\n 4 Random - English word from random-word-api\n")
    while difficulty not in ["1", "2", "3", "4"]:
        difficulty = input("Error " * 10 + "\n"
                           +"please (type 1 ,2 ,3, 4):"
                           + "\n 1 Easy   - Latvian word from words.txt"
                           + "\n 2 Normal - Latvian word from words.txt"
                           + "\n 3 Hard   - Latvian word from words.txt"
                           + "\n 4 Random - English word from random-word-api\n")
    difficulty = int(difficulty)

    os.system('cls')

    if difficulty == 1:
        try:
            word_viegls = words_viegls.pop()
        except IndexError:
            print("\n" + "-" * 70
                  + "\nIzvēlētajā grūtības failā ir beigušies vārdi!\n"
                  + "-"*70 + "\n")
            raise
        game_viegls = Game(word_viegls)
        game_viegls.play()
        if len(game_viegls.try_words) > 0:
            guessed_words.append(''.join(game_viegls.try_words))
            if len(guessed_words) > n:
                print_words = ', '.join(guessed_words)
                n = n + 1
        print(f"\nGuessed word: {print_words}")
        if game_viegls.lives != 0:
            try:
                word_videjs = words_videjs.pop()
            except IndexError:
                print("\n" + "-" * 70
                      + "\nIzvēlētajā grūtības failā ir beigušies vārdi!\n"
                      + "-"*70 + "\n")
                raise
            game_videjs = Game(word_videjs)
            game_videjs.play()
            if len(game_videjs.try_words) > 0:
                guessed_words.append(''.join(game_videjs.try_words))
                if len(guessed_words) > n:
                    print_words = ', '.join(guessed_words)
                    n = n + 1
            print(f"\nGuessed word: {print_words}")
            if game_videjs.lives != 0:
                try:
                    word_gruts = words_gruts.pop()
                except IndexError:
                    print("\n" + "-" * 70
                          + "\nIzvēlētajā grūtības failā ir beigušies vārdi!\n"
                          + "-"*70 + "\n")
                    raise
                game_gruts = Game(word_gruts)
                game_gruts.play()
                if len(game_gruts.try_words) > 0:
                    guessed_words.append(''.join(game_gruts.try_words))
                    if len(guessed_words) > n:
                        print_words = ', '.join(guessed_words)
                        n = n + 1
                print(f"\nGuessed word: {print_words}")
                while game_gruts.lives != 0:
                    try:
                        word_gruts = words_gruts.pop()
                    except IndexError:
                        print("\n" + "-" * 70
                              + "\nIzvēlētajā grūtības failā ir beigušies vārdi!\n"
                              + "-"*70 + "\n")
                        raise
                    game_gruts = Game(word_gruts)
                    game_gruts.play()
                    if len(game_gruts.try_words) > 0:
                        guessed_words.append(''.join(game_gruts.try_words))
                        if len(guessed_words) > n:
                            print_words = ', '.join(guessed_words)
                            n = n + 1
                    print(f"\nGuessed word: {print_words}")
    if difficulty == 2:
        try:
            word_videjs = words_videjs.pop()
        except IndexError:
            print("\n" + "-" * 70
                  + "\nIzvēlētajā grūtības failā ir beigušies vārdi!\n"
                  + "-"*70 + "\n")
            raise
        game_videjs = Game(word_videjs)
        game_videjs.play()
        if len(game_videjs.try_words) > 0:
            guessed_words.append(''.join(game_videjs.try_words))
            if len(guessed_words) > n:
                print_words = ', '.join(guessed_words)
                n = n + 1
        print(f"\nGuessed word: {print_words}")
        if game_videjs.lives != 0:
            try:
                word_gruts = words_gruts.pop()
            except IndexError:
                print("\n" + "-" * 70
                      + "\nIzvēlētajā grūtības failā ir beigušies vārdi!\n"
                      + "-"*70 + "\n")
                raise
            game_gruts = Game(word_gruts)
            game_gruts.play()
            if len(game_gruts.try_words) > 0:
                guessed_words.append(''.join(game_gruts.try_words))
                if len(guessed_words) > n:
                    print_words = ', '.join(guessed_words)
                    n = n + 1
                print(f"\nGuessed word: {print_words}")
                while game_gruts.lives != 0:
                    try:
                        word_gruts = words_gruts.pop()
                    except IndexError:
                        print("\n" + "-" * 70
                              + "\nIzvēlētajā grūtības failā ir beigušies vārdi!\n"
                              + "-"*70 + "\n")
                        raise
                    game_gruts = Game(word_gruts)
                    game_gruts.play()
                    if len(game_gruts.try_words) > 0:
                        guessed_words.append(''.join(game_gruts.try_words))
                        if len(guessed_words) > n:
                            print_words = ', '.join(guessed_words)
                            n = n + 1
                    print(f"\nGuessed word: {print_words}")
    if difficulty == 3:
        try:
            word_gruts = words_gruts.pop()
        except IndexError:
            print("\n" + "-" * 70
                  + "\nIzvēlētajā grūtības failā ir beigušies vārdi!\n"
                  + "-"*70 + "\n")
            raise
        game_gruts = Game(word_gruts)
        game_gruts.play()
        if len(game_gruts.try_words) > 0:
            guessed_words.append(''.join(game_gruts.try_words))
            if len(guessed_words) > n:
                print_words = ', '.join(guessed_words)
                n = n + 1
            print(f"\nGuessed word: {print_words}")
            while game_gruts.lives != 0:
                try:
                    word_gruts = words_gruts.pop()
                except IndexError:
                    print("\n" + "-" * 70
                          + "\nIzvēlētajā grūtības failā ir beigušies vārdi!\n"
                          + "-"*70 + "\n")
                    raise
                game_gruts = Game(word_gruts)
                game_gruts.play()
                if len(game_gruts.try_words) > 0:
                    guessed_words.append(''.join(game_gruts.try_words))
                    if len(guessed_words) > n:
                        print_words = ', '.join(guessed_words)
                        n = n + 1
                print(f"\nGuessed word: {print_words}")
    if difficulty == 4:
        word_random = requests.get('https://random-word-api.herokuapp.com/word?number=1')
        wr = word_random.json()[0].upper()
        game_random = Game(wr)
        game_random.play()
        if len(game_random.try_words) > 0:
            guessed_words.append(''.join(game_random.try_words))
            if len(guessed_words) > n:
                print_words = ', '.join(guessed_words)
                n = n + 1
        print(f"\nGuessed word: {print_words}")

    print('\n' + "_" * 70)
    play_again = input("\nVai vēlies spēli turpināt? \nyes / no\n")
    if play_again not in ["yes", "ye", "y"]:
        break