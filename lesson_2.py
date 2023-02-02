word = input()
glasnye = 0
soglasnye = 0
for i in word:
    letter = i.lower()
    if letter == "a" or letter == "e" or \
            letter == "i" or letter == "o" or \
            letter == "u" or letter == "y":
        glasnye += 1
    else:
        soglasnye += 1

glasnye = round(glasnye / len(word) * 100, 2)
print("glasnye", glasnye)
print("soglasnye", round(100 - glasnye, 2))
