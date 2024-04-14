consonants = {"b", "d", "f", "g", "k", "l", "m", "n", "p", "r", "s", "t", "x", "ʃ", "ʝ", "θ", "ɲ", "ɾ",
              "β", "ð", "ɣ", "ɟ", "ɱ", "ŋ"}
voiced_consonants = {"b", "d", "g", "l", "m", "n", "x", "ʝ", "ɲ"}
vowels = {"a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú"}
stressed_vowel = {"á", "é", "í", "ó", "ú"}
height = {"a": 1, "á": 1, "e": 2, "é": 2, "i": 3, "í": 3, "o": 2, "ó": 2, "u": 3, "ú": 3}
vowel_to_semivowel = {"e": "E", "i": "j", "o": "O", "u": "w"}


def allophonize(text):
    new_word = []
    index = 0
    while index < len(text):
        previous_char = " "
        if index != 0:
            previous_char = text[index - 1]

        current_char = text[index]

        next_char = " "
        if index < len(text) - 1:
            next_char = text[index + 1]

        if current_char == "n":
            if next_char == "b" or next_char == "m" or next_char == "p":
                new_word += "m"
            elif next_char == "f":
                new_word += "ɱ"
            elif next_char == "t" or next_char == "d" or next_char == "θ":
                new_word += "n"
            elif next_char == "ʃ" or next_char == "ʝ":
                new_word += "ɲ"
            elif next_char == "x" or next_char == "k" or next_char == "g":
                new_word += "ŋ"
            else:
                new_word += text[index]
            index += 1
        elif current_char == "b":
            if previous_char != " " and previous_char != "n" and previous_char != "m":
                new_word += "β"
            else:
                new_word += "b"
            index += 1
        elif current_char == "g":
            if previous_char != " " and previous_char != "n" and previous_char != "m":
                new_word += "ɣ"
            else:
                new_word += "g"
            index += 1
        elif current_char == "d":
            if previous_char != " " and previous_char != "n" and previous_char != "m" and previous_char != "d":
                new_word += "ð"
            else:
                new_word += "d"
            index += 1
        elif current_char == "θ":
            if next_char in voiced_consonants:
                new_word += "ð"
            else:
                new_word += "θ"
            index += 1
        elif current_char == "s":
            if next_char in voiced_consonants:
                new_word += "z"
            else:
                new_word += "s"
            index += 1
        elif current_char == "ʝ":
            if previous_char == " " or previous_char == "n" or previous_char == "m" or previous_char == "ɲ":
                new_word += "ɟ"
            else:
                new_word += "ʝ"
            index += 1
        elif current_char in vowels and next_char in vowels:
            if current_char in stressed_vowel and next_char in stressed_vowel:
                new_word += current_char
                index += 1
            elif (current_char == "i" or current_char == "u") and next_char in stressed_vowel:
                new_word += vowel_to_semivowel[current_char] + next_char
                index += 2
            elif current_char in stressed_vowel and (next_char == "i" or next_char == "u"):
                new_word += current_char + vowel_to_semivowel[next_char]
                index += 2
            elif current_char in stressed_vowel or next_char in stressed_vowel:  # stressed vowel but no sandhi
                new_word += current_char
                index += 1
            else:
                print("CURRENT:", current_char, "NEXT:", next_char)
                if current_char == next_char:
                    new_word += current_char
                elif height[current_char] >= height[next_char]:
                    new_word += vowel_to_semivowel[current_char] + next_char
                else:
                    new_word += current_char + vowel_to_semivowel[next_char]
                index += 2
        else:
            new_word += text[index]
            index += 1

    return new_word
