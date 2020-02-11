/*

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
*/


import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
   int divisorSum(int n);
}
class Calculator implements AdvancedArithmetic {
    public int divisorSum(int n) {
        int total = 0;
        for (int i = 1; i < n+1; i++){
            if (n % i == 0) {
                total += i;
            }
            else {
                ;  //ignores the number if it doesn't meet the condition
            }
        }
        return total;
    }
}

