from phonologize import phonologize
from syllabification import place_stress, syllabize


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

    print(syllabize(utterance))

    # TODO: allophone pass

    # TODO: syllabification pass


if __name__ == "__main__":
    generate_phonetic_transcription("../input.txt")
