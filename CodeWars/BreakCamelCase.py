def break_camel_case(s):
    new_word = ""
    for letter in s:
        if letter.isupper():
            new_word += " "
        new_word += letter
    return new_word