'''
Unique Characters in String
Problem
Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
'''
def uni_char(s):
    uniqueLetters = set()
    
    if len(s) < 1:
        return 'Invalid input length'
    
    for letter in s:
        if letter in uniqueLetters:
            return False
        else:
            uniqueLetters.add(letter)
    return True