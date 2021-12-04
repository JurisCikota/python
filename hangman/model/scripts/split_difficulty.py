from scripts.word_weight import Score
import pathlib
import os


class Diffculty():
    """Create dificulty files from origin file.

    Takes origin file and create three difficulty files
    using Score class.
    level as viegls or videjs or gruts.
    Difficulty class opens these difficulty files
    and reads file content.

    dfclty = Diffculty()
    dfclty.generate_difficulty(level)
    """

    def __init__(self):
        self.cur_dir = pathlib.Path(__file__).parent.absolute()
        self.parent = self.cur_dir.parent
        self.viegls = os.path.join(self.parent, "data", "easy_words.txt")
        self.videjs = os.path.join(self.parent, "data", "medium_words.txt")
        self.gruts = os.path.join(self.parent, "data", "hard_words.txt")
        self.words = list()

    def file_exists(self):
        """Check if file exists.
        If file exists it removes existing file
        """
        if os.path.exists(self.viegls):
            os.remove(self.viegls)
        if os.path.exists(self.videjs):
            os.remove(self.videjs)
        if os.path.exists(self.gruts):
            os.remove(self.gruts)

    def write_files(self):
        """Opens origin file and calls Score class
        to calculate word difficulty and saves it to file.
        """
        path = os.path.join(self.parent, "data", 'words.txt')
        with open(path, 'r', encoding='utf-8') as file:
            li = file.read().split("\n")
            for l in li:
                split = Score(l)
                split.save_words()

    def generate_difficulty(self, level):
        """Function used to return word based on difficulty.

        Args:
            take level argument
            level can only be: viegls, videjs, gruts

        Returns:
            chosen difficulty word

        Raises:
            FileNotFoundError
        """
        if level == "viegls":
            try:
                with open(self.viegls, 'r', encoding='utf-8') as file:
                    lines = file.read()
                    self.words = lines.split('\n')
                    return self.words
            except FileNotFoundError:
                print("\n" + "-" * 70
                      + "\nFails neeksistē!\n" + "-" * 70 + "\n")
                raise
        if level == "videjs":
            try:
                with open(self.videjs, 'r', encoding='utf-8') as file:
                    lines = file.read()
                    self.words = lines.split('\n')
                    return self.words
            except FileNotFoundError:
                print("\n" + "-" * 70
                      + "\nFails neeksistē!\n" + "-" * 70 + "\n")
                raise
        if level == "gruts":
            try:
                with open(self.gruts, 'r', encoding='utf-8') as file:
                    lines = file.read()
                    self.words = lines.split('\n')
                    return self.words
            except FileNotFoundError:
                print("\n" + "-" * 70
                      + "\nFails neeksistē!\n" + "-" * 70 + "\n")
                raise