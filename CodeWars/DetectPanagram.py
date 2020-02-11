"""

https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""

import string

def is_pangram(s):
    characters = set()
    s = s.lower()
    
    
    for each in s:
        if each.isalpha():
           characters.add(each)
        else:
            pass


    if len(characters) == 26:
        return True
    else:
        return False