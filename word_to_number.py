def text2int(textnum, numwords={}):
    if not numwords:
        units = {
            "zero": 0, "unu": 1, "una": 1, "un": 1, "o": 1, "doi": 2, "doua": 2, "trei": 3, "patru": 4, "cinci": 5,
            "sase": 6, "sapte": 7, "opt": 8,
            "noua": 9, "zece": 10, "unsprezece": 11, "doisprezece": 12, "treisprezece": 13, "paisprezece": 14,
            "cincisprezece": 15,
            "saisprezece": 16, "saptesprezece": 17, "optsprezece": 18, "nouasprezece": 19}
        units1 = [
            "un ", "o", "noua"
        ]
        units2 = [
            "zero", "unu", "doi", "doua", "trei", "patru", "cinci", "sase",
            "sapte", "opt ", "noua", "zece", "unsprezece", "doisprezece", "treisprezece",
            "paisprezece", "cincisprezece", "saisprezece", "saptesprezece", "optsprezece", "nouasprezece", "sute", "mie"
        ]

        tens = ["", "", "douazeci", "treizeci", "patruzeci", "cincizeci", "saizeci", "saptezeci", "optzeci", "nouazeci"]

        scales = {"suta": 2, "sute": 2, "mie": 3, "mii": 3, "milioane": 6, "milion": 6, "miliarde": 9, "miliard": 9,
                  "trilioane": 12, "trilion": 12, "quatralioane": 15, "quatralion": 15}

        for idx, word in enumerate(units):  numwords[word] = (1, units[word])
        for idx, word in enumerate(tens):   numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** scales[word], 0)

    ordinal_words = {'primul': 1, 'aldoilea': 2, 'altreilea': 3, 'alcincilea': 5, 'aloptulea': 8, 'alnoulea': 9,
                     'aldoisprecelea': 12}
    ordinal_endings = [('lea', ''), ('a', 'a')]

    textnum = textnum.replace('si', ' ')
    textnum = textnum.replace('de', ' ')
    textnum = textnum.replace('lei', ' ')

    # units {
    textnum = textnum.replace('zero', 'zero ')
    textnum = textnum.replace('unu', 'unu ')

    textnum = textnum.replace('doi', 'doi ')

    textnum = textnum.replace('opt', 'opt')
    textnum = textnum.replace('noua', 'noua')
    # textnum = textnum.replace('sute', ' sute ')
    # textnum = textnum.replace('suta', ' suta ')
    #
    # textnum = textnum.replace('zece', 'zece ')
    # textnum = textnum.replace('mii', ' mii ')
    # textnum = textnum.replace('zeci', 'zeci ')
    # textnum = textnum.replace('mie', ' mie ')
    for idx, word in enumerate(scales):  textnum = textnum.replace(word, ' '+word+' ')

    # }

    current = result = 0
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (0, ordinal_words[word])
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                raise Exception("Cuvantul: '" + word + "', nu este recunoscut!")

            scale, increment = numwords[word]

        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    number = result + current

    return number
x = str(text2int("douamii"))
print("Numarul este: " + x)
