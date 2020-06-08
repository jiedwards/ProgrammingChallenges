'''
Problem¶
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

def compress(s):
    letterMap = {}
    outputCompression = ""
    if len(s) < 1:
        return "Invalid input length."
    
    for letter in s:
        if letter in letterMap:
            letterMap[letter] += 1
        else:
            letterMap[letter] = 1
            
    for key, value in letterMap.items():
        outputCompression += key + str(value)

    return outputCompression