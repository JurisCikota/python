from scripts.word_weight import Score
import pathlib
import os

class Diffculty():
    def __init__(self):
        self.cur_dir = pathlib.Path(__file__).parent.absolute()
        self.parent = self.cur_dir.parent
        self.viegls = os.path.join(self.parent, "data", "easy_words.txt")
        self.videjs = os.path.join(self.parent, "data", "medium_words.txt")
        self.gruts = os.path.join(self.parent, "data", "hard_words.txt")
        self.words = list()

    def file_exists(self):
        if os.path.exists(self.viegls):
            os.remove(self.viegls)
        if os.path.exists(self.videjs):
            os.remove(self.videjs)
        if os.path.exists(self.gruts):
            os.remove(self.gruts)


    def write_files(self):    
        path = os.path.join(self.parent, "data", 'words.txt')
        with open(path, 'r', encoding='utf-8') as file:
            li = file.read().split("\n")
            for l in li:
                split = Score(l)
                split.save_words()

    def choose_difficulty(self):
        difficulty = input("\nChoose difficulty (type 1 ,2 ,3):\n 1 Easy\n 2 Normal\n 3 Hard\n")
        while difficulty not in ["1", "2", "3"]:
            difficulty = input("Error "*10 +"\n"+"please (type 1 ,2 ,3):\n 1 Easy\n 2 Normal\n 3 Hard\n")
        difficulty = int(difficulty)
        if difficulty == 1:
            with open(self.viegls, 'r', encoding='utf-8') as file:
                lines = file.read()
                self.words = lines.split('\n')
                return self.words
        if difficulty == 2:
            with open(self.videjs, 'r', encoding='utf-8') as file:
                lines = file.read()
                self.words = lines.split('\n')
                return self.words
        if difficulty == 3:
            with open(self.gruts, 'r', encoding='utf-8') as file:
                lines = file.read()
                self.words = lines.split('\n')
                return self.words    