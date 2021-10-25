letter_score =	{
"a": 1,
"i": 2,
"s": 3,
"t": 4,
"e": 5,
"u": 6,
"r": 7,
"n": 8,
"k": 9,
"m": 10,
"o": 11,
"d": 12,
"v": 13,
"p": 14,
"l": 15,
"j": 16,
"z": 17,
"b": 18,
"g": 19,
"c": 20,
"f": 21,
"h": 22
}

def translate(my_string):
    my_string = my_string.lower()
    lat = {"ā": "a", "č": "c", "ē": "e", "ģ": "g", "ī": "i", "ķ": "k", "ļ": "l", "ņ": "n", "š": "s", "ū": "u", "ž": "z"}
    for k, v in lat.items():
        my_string = my_string.replace(k, v)
    print(my_string)

translate("ŽžūĀ")
