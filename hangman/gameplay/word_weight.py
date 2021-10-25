import syllables

def translate(my_string):
    my_string = my_string.lower()
    lat = {"ā": "a", "č": "c", "ē": "e", "ģ": "g", "ī": "i", "ķ": "k", "ļ": "l", "ņ": "n", "š": "s", "ū": "u", "ž": "z"}
    for k, v in lat.items():
        my_string = my_string.replace(k, v)
    return my_string

def letter_score(my_string):
    my_string = my_string.lower()
    t = translate(my_string)
    score = 0
    letters = {"a": 1,"i": 2,"s": 3,"t": 4,"e": 5,"u": 6,"r": 7,"n": 8,"k": 9,"m": 10,"o": 11,"d": 12,"v": 13,"p": 14,"l": 15,"j": 16,"z": 17,"b": 18,"g": 19,"c": 20,"f": 21,"h": 22}
    for k, v in letters.items():
            for letter in t:
                if letter == k:
                    score = score + v
    return score

def syllables_score(my_string):
    t = translate(my_string)
    initial_score = syllables.estimate(t)
    syllables_score = initial_score * 10
    return syllables_score

def unique_score(my_string):
    t = translate(my_string)
    u = (''.join(set(t)))
    initial_score = len(u)
    unique_score = initial_score * 2
    return unique_score

def len_score(my_string):
    t = translate(my_string)
    len_score  = len(t)
    return len_score

def total_score(my_string):
    l = letter_score(my_string)
    s = syllables_score(my_string)
    u = unique_score(my_string)
    le = len_score(my_string)
    total_score = l + s + u + le
    print(total_score)

total_score("RENTGENIZMEKLĒJUMS")
