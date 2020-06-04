import unittest
'''
Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
'''

def anagram(s1,s2):
    my_dict = {}
    
    #Remove all whitespace and uppercasing
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    
    #Preliminary check to ensure input isn't empty
    if len(s1) == 0 or len(s2) == 0:
        return IndexError("Incorrect input length.")
    
    if len(s1) != len(s2):
        return False
    
    for each in s1:
        if each in my_dict:
            my_dict[each] += 1
        else:
            my_dict[each] = 1
    
    #Iterate through each letter/number and return false if it doesn't exist in dictionary
    for each in s2:
        if each in my_dict:
            my_dict[each] -= 1
        else:
            return False
        
    return True