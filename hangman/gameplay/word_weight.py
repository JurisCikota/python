import syllables

class Score:
    def __init__(self, word):
        self.word = word

    def translate(self):
        word = self.word.lower()
        lat = {"ā": "a", "č": "c", "ē": "e", "ģ": "g", "ī": "i", "ķ": "k", "ļ": "l", "ņ": "n", "š": "s", "ū": "u", "ž": "z"}
        for k, v in lat.items():
            word = word.replace(k, v)
        return word

    def letter_score(self):
        t = self.translate()
        score = 0
        letters = {"a": 1,"i": 2,"s": 3,"t": 4,"e": 5,"u": 6,"r": 7,"n": 8,"k": 9,"m": 10,"o": 11,"d": 12,"v": 13,"p": 14,"l": 15,"j": 16,"z": 17,"b": 18,"g": 19,"c": 20,"f": 21,"h": 22}
        for k, v in letters.items():
            for letter in t:
                if letter == k:
                    score = score + v
        return score

    def syllables_score(self):
        t = self.translate()
        initial_score = syllables.estimate(t)
        syllables_score = initial_score * 10
        return syllables_score

    def unique_score(self):
        t = self.translate()
        u = (''.join(set(t)))
        initial_score = len(u)
        unique_score = initial_score * 2
        return unique_score

    def len_score(self):
        t = self.translate()
        len_score  = len(t)
        return len_score

    def total_score(self):
        l = self.letter_score()
        s = self.syllables_score()
        u = self.unique_score()
        le = self.len_score()
        total_score = l + s + u + le
        print(total_score)