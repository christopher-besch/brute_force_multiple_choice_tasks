from itertools import product


def get_options(*args):
    # for example this:
    # (("01", "02", "03", "04", "05"),
    # ("11", "12", "13", "14", "15"))
    # gets turned into this:
    # (("01", "11"),
    # ("02", "12"),
    # ("03", "13"),
    # ("04", "14"),
    # ("05", "15"))
    zipped_chars = zip(*args)

    # yield every option of picking one of each entry in zipped_chars
    for option_tuple in product(*zipped_chars):
        yield "".join(option_tuple)


def get_german_word_list():
    # from http://www.netzmafia.de/software/wordlists/deutsch.txt
    with open("german_words.txt", "r", encoding="utf-8") as file:
        # everything to upper case and cut at line breaks
        german_words = file.read().upper().split("\n")

    umlauts = {
        "AE": "Ä",
        "OE": "Ö",
        "UE": "Ü",
        "SS": "ß"
    }
    new_german_words = []
    # add copy with umlauts changed
    for german_word in german_words:
        # testing for every umlaut
        for umlaut in umlauts:
            # from other form to umlaut
            if umlaut in german_word:
                new_german_words.append(german_word.replace(umlaut, umlauts[umlaut]))
            # other way around
            elif umlauts[umlaut] in german_word:
                new_german_words.append(german_word.replace(umlauts[umlaut], umlaut))
    return german_words + new_german_words


if __name__ == "__main__":
    # one entry per option (true/false)
    with open("chars.txt", "r", encoding="utf-8") as file:
        # list with a list of chars for each option (e.g. true/false)
        char_options = [list(line) for line in file.read().split("\n")]

    options = get_options(*char_options)

    words = get_german_word_list()

    # going through every option
    print("possible solutions are:")
    for option in options:
        if option in words:
            print(option)
    input()
