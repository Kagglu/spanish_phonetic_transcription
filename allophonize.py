consonants = {"b", "d", "f", "g", "k", "l", "m", "n", "p", "r", "s", "t", "x", "tʃ", "ʝ", "θ", "ɲ", "ɾ",
              "β", "ð", "ɣ", "ɟʝ", "ɱ", "ŋ"}
nasals = {"m", "n", "ɲ"}
voiced_stops = {"b", "d", "g"}
complex_onset_consonants = {"b", "d", "f", "g", "k", "p", "t", "β", "ð", "ɣ"}
vowels = {"a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú"}


def allophonize(text):
    new_word = []
    index = 0
    pause = True
    while index < len(text):
        if pause:
            new_word += text[index]
            index += 1
            pause = False
        else:
            current_char = text[index]
            if current_char in nasals and index < len(text) - 1:
                if text[index + 1] == "b" or text[index + 1] == "m":
                    new_word += "m"
                elif text[index + 1] == "f":
                    new_word += "ɱ"
                elif text[index + 1] == "t" or text[index + 1] == "d" or text[index + 1] == "θ":
                    new_word += "n"
                elif text[index + 1] == "tʃ":
                    new_word += "ɲ"
                elif text[index + 1] == "x" or text[index + 1] == "k":
                    new_word += "ŋ"
                else:
                    new_word += text[index]
                index += 1
                pause = True
            elif current_char in voiced_stops:
                match current_char:
                    case "b":
                        new_word += "β"
                    case "g":
                        new_word += "ɣ"
                    case "d":
                        new_word += "ð"
                index += 1
                pause = False
            else:
                new_word += text[index]
                index += 1
                pause = False
    return new_word
