glaa = 0
soog = 0
while True:
    word = input('введите слово:').lower()
    if word == 'stop':
        break
    for i in word:
        letter = i.lower()
        if letter == "a" or letter == "e" or \
                letter == "i" or letter == "o" or \
                letter == "u" or letter == "y" or \
                letter == "а" or letter == "я" or \
                letter == "у" or letter == "ю" or \
                letter == "о" or letter == "е" or \
                letter == "ё" or letter == "э" or \
                letter == "и" or letter == "ы":
            glaa += 1

        else:
            soog += 1

    b = soog + glaa  # вычесление количество слов

    print(f'слово: {word}\n'
          f'согласные буквы: {soog}\n'
          f'гласные буквы: {glaa}\n'
          f'количество букв: {soog + glaa}\n')
    glaa = round(glaa / len(word) * 100, 2)  # вычесление гласных букв

    print("гласные/согласные:", glaa, "% /", round(100 - glaa, 2), "%")  # вычесление согласных букв
