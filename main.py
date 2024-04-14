from phonologize import phonologize
from syllabification import place_stress, syllabize
from allophonize import allophonize


def generate_phonetic_transcription(filename):
    f = open(filename, "r")
    text = f.read()
    words = text.split()

    # Phonological pass - convert list of orthographic characters into phonemic ones
    phonologized_words = list(map(phonologize, words))

    # Stress pass - place stress in words
    stressed_words = list(map(place_stress, phonologized_words))

    utterance = []
    for word in stressed_words:
        utterance += word

    allophonized_words = allophonize(utterance)

    final_words = syllabize(allophonized_words)

    utterance = ""
    unstress_vowel = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u"
    }
    for word in final_words:
        new_word = ""
        for c in word:
            new_word += c
        index = max(new_word.find("á"), new_word.find("é"), new_word.find("í"), new_word.find("ó"), new_word.find("ú"))
        if index >= 0:
            new_word = "'" + new_word[0:index] + unstress_vowel[new_word[index]] + new_word[index + 1:]
        utterance += new_word + "."

    utterance = utterance.replace("ʃ", "tʃ")
    utterance = utterance.replace("ɟ", "ɟʝ")
    utterance = utterance.replace(" ", " | ")

    # TODO: replace E and O semivowels and fix syllable breaks around pauses
    print(utterance)

if __name__ == "__main__":
    generate_phonetic_transcription("../input.txt")
