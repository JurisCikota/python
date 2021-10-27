from word_weight import Score
import pathlib
import os

cur_dir = pathlib.Path(__file__).parent.absolute()
parent = cur_dir.parent
path = os.path.join(parent, "data", 'words.txt')
with open(path, 'r', encoding='utf-8') as file:
    li = file.read().split("\n")
    for l in li:
        split = Score(l)
        split.save_words()