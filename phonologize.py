def phonologize(word):
    # set word to lower case, handle special cases, split into list of characters
    word = [*(word.lower().replace("mexi", "meji").replace("méxi", "méji")
              .replace("texa", "teja").replace("oaxa", "oaja"))]

    new_word = []
    while len(word) > 0:
        match word:
            case ["c", "h", *rest]:  # <ch> -> /tʃ/
                new_word += ["tʃ"]
                word = rest
            case ["l", "l", *rest]:  # <ll> -> /ʝ/
                new_word += "ʝ"
                word = rest
            case ["q", "u", ("é" | "e" | "í" | "i") as ei, *rest]:  # <qu> -> /k/ | _ {<e> | <i>}
                new_word += "k" + ei
                word = rest
            case ["g", "u", ("é" | "e" | "í" | "i") as ei, *rest]:  # <gu> -> /g/ | _ {<e> | <i>}
                new_word += "g" + ei
                word = rest
            case ["r", "r", *rest]:  # <rr> -> /r/
                new_word += "r"
                word = rest
            case [("l" | "m" | "n" | "s" | "x" | "z") as consonant, "r", *rest]:
                # <r> -> /r/ | {<l> | <m> | <n> | <s> | <x> | <z>} _
                new_word += consonant + "r"
                word = rest
            case ["á", *rest]:
                new_word += "á"
                word = rest
            case ["a", *rest]:
                new_word += "a"
                word = rest
            case ["b", *rest]:
                new_word += "b"
                word = rest
            case ["c", ("é" | "e" | "í" | "i") as ei, *rest]:
                new_word += "θ" + ei
                word = rest
            case ["c", *rest]:
                new_word += "k"
                word = rest
            case ["d", *rest]:
                new_word += "d"
                word = rest
            case ["é", *rest]:
                new_word += "é"
                word = rest
            case ["e", *rest]:
                new_word += "e"
                word = rest
            case ["f", *rest]:
                new_word += "f"
                word = rest
            case ["g", ("é" | "e" | "í" | "i") as ei, *rest]:
                new_word += "x" + ei
                word = rest
            case ["g", *rest]:
                new_word += "g"
                word = rest
            case ["h", *rest]:  # h is always silent
                word = rest
            case ["í", *rest]:
                new_word += "í"
                word = rest
            case ["i", *rest]:
                new_word += "i"
                word = rest
            case ["j", *rest]:
                new_word += "x"
                word = rest
            case ["k", *rest]:
                new_word += "k"
                word = rest
            case ["l", *rest]:
                new_word += "l"
                word = rest
            case ["m", *rest]:
                new_word += "m"
                word = rest
            case ["n", *rest]:
                new_word += "n"
                word = rest
            case ["ñ", *rest]:
                new_word += "ɲ"
                word = rest
            case ["ó", *rest]:
                new_word += "ó"
                word = rest
            case ["o", *rest]:
                new_word += "o"
                word = rest
            case ["p", "s", *rest] if len(new_word) == 0:  # word initial <ps> -> /s/
                new_word += "s"
                word = rest
            case ["p", *rest]:
                new_word += "p"
                word = rest
            case ["q", *rest]:
                new_word += "k"
                word = rest
            case ["r", *rest]:
                if len(new_word) == 0:  # word initial <r> -> /r/ (trill)
                    new_word += "r"
                else:
                    new_word += "ɾ"
                word = rest
            case ["s", *rest]:
                new_word += "s"
                word = rest
            case ["t", *rest]:
                new_word += "t"
                word = rest
            case ["ú", *rest]:
                new_word += "ú"
                word = rest
            case ["ü", *rest]:
                new_word += "u"
                word = rest
            case ["u", *rest]:
                new_word += "u"
                word = rest
            case ["v", *rest]:
                new_word += "b"
                word = rest
            case ["w", *rest]:  # ignoring possible /b/ like in "wagneriano"
                new_word += "u"
                word = rest
            case ["x", *rest]:
                if len(new_word) == 0:  # word initial <x> -> /s/
                    new_word += "s"
                else:
                    new_word += "gs"
                word = rest
            case ["y", ("á" | "a" | "é" | "e" | "í" | "i" | "ó" | "o" | "ú" | "u") as vowel, *rest]:
                new_word += "ʝ" + vowel
                word = rest
            case ["y", *rest]:
                new_word += "i"
                word = rest
            case ["z", *rest]:
                new_word += "θ"
                word = rest
            case [("..." | "." | "," | "?" | "!" | ":" | ";" | "(" | ")"), *rest]:
                new_word += " "
                word = rest
            case [other, *rest]:
                print("unrecognized character:", other)
                word = rest
    return new_word

