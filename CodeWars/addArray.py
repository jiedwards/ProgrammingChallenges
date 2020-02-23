"""
https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

"""
def up_array(arr):
    a = ""
    value = 0
    for each in arr:
        if each < 0 or each > 9:
            return None
        else:
            a += str(each).strip()
            
    try:
        value = int(a)
    except:
        return None
    
    value += 1
    return [int(i) for i in str(value)]