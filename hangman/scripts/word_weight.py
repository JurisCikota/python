import syllables
import pathlib
import os

class Score:
    def __init__(self, word):
        self.word = word

        cur_dir = pathlib.Path(__file__).parent.absolute()
        parent = cur_dir.parent
        self.viegls = os.path.join(parent, "data", "easy_words.txt")
        self.videjs = os.path.join(parent, "data", "medium_words.txt")
        self.gruts = os.path.join(parent, "data", "hard_words.txt")

    def translate(self):
        """Converts latvian letters with macron and cedilla to regular letter

        Returns:
            converted letter in lower case
        """
        word = self.word.lower()
        lat = {"ā": "a", "č": "c", "ē": "e", "ģ": "g", "ī": "i", "ķ": "k", "ļ": "l", "ņ": "n", "š": "s", "ū": "u", "ž": "z"}
        for k, v in lat.items():
            word = word.replace(k, v)
        return word

    def letter_score(self):
        """Gives score to letter based on letter popularity
        Where most popular letter score 1, second popular 2, etc.
        function goes through letters in word and sum letter scores.

        Returns:
            INTEGER sum of letter score
        """
        t = self.translate()
        score = 0
        letters = {"a": 1,"i": 2,"s": 3,"t": 4,"e": 5,"u": 6,"r": 7,"n": 8,"k": 9,"m": 10,"o": 11,"d": 12,"v": 13,"p": 14,"l": 15,"j": 16,"z": 17,"b": 18,"g": 19,"c": 20,"f": 21,"h": 22}
        for k, v in letters.items():
            for letter in t:
                if letter == k:
                    score = score + v
        return score
 

    def syllables_score(self):
        """Calculate estimate sylalbles in word

        Returns:
            INTEGER sum of syllables in word
        """
        t = self.translate()
        initial_score = syllables.estimate(t)
        syllables_score = initial_score * 10
        return syllables_score

    def unique_score(self):
        """Calculate unique letters in word

        Returns:
            INTEGER unique letter count multiplicate by 2
        """
        t = self.translate()
        u = (''.join(set(t)))
        initial_score = len(u)
        unique_score = initial_score * 2
        return unique_score

    def len_score(self):
        """Calculate length of word

        Returns:
            INTEGER word length
        """
        t = self.translate()
        len_score  = len(t)
        return len_score

    def total_score(self):
        """Calculate total score of word difficulty

        Returns:
            INTEGER sum of letter_score, syllables_score, unique_score, len_score functions
        """
        l = self.letter_score()
        s = self.syllables_score()
        u = self.unique_score()
        le = self.len_score()
        total_score = l + s + u + le
        return total_score

    def save_words(self):
        """Depending on score write word to right file
        """
        if self.total_score() < 100:
            self.write_to_file(self.viegls)
        elif self.total_score() >= 100 and self.total_score() <= 150:
            self.write_to_file(self.videjs)
        else:
            self.write_to_file(self.gruts)
        
    def write_to_file(self, file):
        """write file function so every word ends with new line except last
        """
        if not os.path.exists(file):
            with open(file, 'a', encoding='utf-8') as word_fails:
                word_fails.write(self.word)
                word_fails.close()
        else:
            with open(file, 'a', encoding='utf-8') as word_fails:
                word_fails.write(f"\n{self.word}")
                word_fails.close()