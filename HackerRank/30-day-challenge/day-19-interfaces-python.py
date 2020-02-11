"""
https://www.hackerrank.com/challenges/30-interfaces/problem

Objective
Today, we're learning about Interfaces. Check out the Tutorial tab for learning materials and an instructional video!

Task
The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are provided for you in the editor below.

Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. The implementation for the divisorSum(n) method must return the sum of all divisors of .

Sample Input

6
Sample Output

I implemented: AdvancedArithmetic
12

"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        total = 0
        for divisor in range(1,n+1):
            if n % divisor == 0:
                total += divisor
            else:
                pass
        return total