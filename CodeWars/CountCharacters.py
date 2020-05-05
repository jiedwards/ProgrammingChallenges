def count(string):
    letterMap = {}
    for letter in string:
        if letter in letterMap:
            letterMap[letter] += 1
        else:
            letterMap[letter] = 1
    return letterMap