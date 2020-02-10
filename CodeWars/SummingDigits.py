"""

https://www.codewars.com/kata/52f3149496de55aded000410/train/python

Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. For example:

  sum_digits(10)  # Returns 1
  sum_digits(99)  # Returns 18
  sum_digits(-32) # Returns 5
Let's assume that all numbers in the input will be integer values.


"""

def sum_digits(number):
    sum = 0
    
    for each in str(abs((number))):
        sum += int(each)
    return sum