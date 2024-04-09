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

    # TODO: allophone pass
    allophonized_words = allophonize(utterance)
    print(allophonized_words)

    # TODO: syllabification pass


if __name__ == "__main__":
    generate_phonetic_transcription("../input.txt")
