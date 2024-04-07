consonants = {"b", "d", "f", "g", "k", "l", "m", "n", "p", "r", "s", "t", "x", "tʃ", "ʝ", "θ", "ɲ", "ɾ",
              "β", "ð", "ɣ", "ɟʝ", "ɱ", "ŋ"}
complex_onset_consonants = {"b", "d", "f", "g", "k", "p", "t", "β", "ð", "ɣ"}

# TODO: complete list of (phonological transcriptions of) function words
function_words = {"el", "la", "del", "al", "un", "ke", "me", "te", "se", "lo", "le", "nos", "os", "les", "los", "las"}

stressed = {
    "a": "á",
    "e": "é",
    "i": "í",
    "o": "ó",
    "u": "ú"
}


# Syllabizes a word or words. Returns a list of syllables.
def syllabize(text):
    syllables = []
    index = len(text) - 1
    while index >= 0:
        current_syllable = []
        if text[index] == " ":
            index -= 1
        if text[index] == "s":
            current_syllable += text[index]
            index -= 1
        if index >= 0 and text[index] in consonants:
            match text[index]:
                case "k":
                    current_syllable += "g"
                case "p":
                    current_syllable += "b"
                case "t":
                    current_syllable += "d"
                case _:
                    current_syllable += text[index]
            index -= 1
        if index >= 0 and text[index] in ["j", "w"]:  # semivowel
            current_syllable += text[index]
            index -= 1
        if index >= 0 and text[index] in ["a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú"]:  # nucleus
            current_syllable += text[index]
            index -= 1
        if index >= 0 and text[index] in ["j", "w"]:  # semivowel
            current_syllable += text[index]
            index -= 1
        if index >= 0 and text[index] in consonants:
            current_syllable += text[index]
            index -= 1
        if index >= 0 and text[index - 1] in ["l", "ɾ"] and text[index] in complex_onset_consonants:
            current_syllable += text[index]
            index -= 1
        syllables += [current_syllable[::-1]]
    return syllables[::-1]


def place_stress(word):
    # Function words have no stress
    word_string = ""
    for character in word:
        word_string += character
    if word_string in function_words:
        return word

    # Handle double stress in -mente adverbs
    if word_string[-5:] == "mente" and len(word_string) > 5:
        return place_stress(word[:-5]) + place_stress("mente")

    # No need to calculate stress if we already know where it is
    if "á" in word or "é" in word or "í" in word or "ó" in word or "ú" in word:
        return word

    # Find stressed syllable and replace vowel with stressed vowel
    syllables = syllabize(word)
    if syllables[-1][-1] in ["a", "e", "i", "o", "u", "n", "s"] and len(syllables) > 1:  # llano
        syllables[-2] = stress_nucleus(syllables[-2])
    else:
        syllables[-1] = stress_nucleus(syllables[-1])

    # Return list of letters instead of syllables
    letters = []
    for syllable in syllables:
        letters += [*syllable]
    return letters


def stress_nucleus(syllable):
    word = ""
    for letter in syllable:
        word += letter
    index = max(word.find("a"), word.find("e"), word.find("i"), word.find("o"), word.find("u"))
    syllable[index] = stressed[syllable[index]]
    return syllable
