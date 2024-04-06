from phonologize import phonologize


def generate_phonetic_transcription(filename):
    f = open(filename, "r")
    text = f.read()
    words = text.split()
    phonologized_words = []
    for word in words:
        # convert list of orthographic characters into phonemic ones
        phonologized_words.append(phonologize(word))

    print(phonologized_words)

    # TODO: allophone pass

    # TODO: syllabification pass


if __name__ == "__main__":
    generate_phonetic_transcription("../input.txt")
