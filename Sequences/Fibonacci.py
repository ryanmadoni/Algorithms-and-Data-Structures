"""
Author: Ryan Adoni
Date: 9/22/2021
Description: The Fibonacci Sequence 
"""

import timeit
import sys
from math import sqrt
import numpy as np

sys.setrecursionlimit(10000) # Set the recursion limit to some high number for testing for the recursive function.



def recursiveFibonacci(n):
    """
    An implementation of the Fibonacci sequence using recursion (a pretty poor implementation).  Takes in a
    positive integer or zero, n, and returns the nth Fibonacci number.
    """

    # Make sure a valid n was entered.
    if n < 0: 
        return None # Return None if a number less than 0 was entered.

    # The base case for the recursion
    if n <= 2:
        return 0 if n == 0 else 1 # return 1 for the first and second Fibonacci number.  Return 0 for the zeroth Fibonacci number.

    return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2) # Recurse to return the nth Fibonacci number.



def iterativeFibonacci(n):
    """
    An implementation of the Fibonacci sequence using iteration (a pretty poor implementation).  Takes in a
    positive integer or zero, n, and returns the nth Fibonacci number.
    """

    # Make sure a valid n was entered.
    if n <= 0: 
        return None if n < 0 else 0 # Return None if a number less than 0 was entered and 0 if 0 was entered.

    n0, n1 = 0, 1 # Set two variables representing the nth and n+1th Fibonacci numbers.

    # Loop until n is 0 and decrement n each iteration.
    while (n := n - 1):
        temp = n1 # Save n1 as a temporary variable
        n0, n1 = temp, n0 + n1 # Set n0 to n1 and n1 to the sum of the previous two numbers.

    return n1 # return n0, the nth Fibonacci number.


def matrixFibonacci(N):
    """
    """
    A = np.array([[1, 1], [1, 0]])

    def helper(n, F):
        """
        """

        if n == N:
            return F[0][0]
        
        return helper(n + 1, A @ F)

    return helper(0, np.array([[0], [1]]))



def binetFibonacci(n):
    """
    An implementation of the Fibonacci sequence using the Binet formula, the fact that the nth Fibonacci number
    satisfies the following equation: Fn =  [phi^n / sqrt(5)] where phi = (1 + sqrt(5)) / 2 and [] represents
    the closets integer function.  Takes in a positive integer or zero, n, and returns the nth Fibonacci number.
    """
    return round(((1 + sqrt(5)) / 2) ** n / sqrt(5)) # Use a simplfied version of the Binet formula to calculate and return the nth Fibonacci number.



def fibonacciGenerator():
    """
    A generator to generate numbers in the Fibonacci sequence sequentially
    """
    nFib = 1 # set the nth Fibonacci number
    nPlusOnefib = 1 # set the n+1th Fibonacci number
    
    # loop forever
    while True:
        yield nFib #yield the nth Fibonacci number
        nPlusTwoFib = nFib + nPlusOnefib # calculate the n+2th Fibonacci number
        nFib = nPlusOnefib # update the nth Fibonacci number
        nPlusOnefib = nPlusTwoFib # update the n+1th Fibonacci number



def wrapper(func, *args, **kwargs):
    """
    Define a wrapper to pass functions to the timeit function
    """
    def wrapped():
        """
        A helper function.
        """
        return func(*args, **kwargs) # Call and return the wrapped function.

    return wrapped # Return the wrapper.


if __name__ == "__main__":

    # print(recursiveFibonacci(25))
    # print(iterativeFibonacci(25))
    print(binetFibonacci(25))
    print(matrixFibonacci(25))

    # print(timeit.timeit(wrapper(recursiveFibonacci, 25), number = 10)) # Run and time the recursive definition.
    # print(timeit.timeit(wrapper(iterativeFibonacci, 1000), number = 100)) # Run and time the iterative definition.
    # print(timeit.timeit(wrapper(binetFibonacci, 1000), number = 100)) # Run and time the Binet definition.

    # The Binet calculation scales better with larger n as it is theta(1) while the iterative is still better
    # than the recrusive definition even though both are close to theta(n) since the overhead for the recursion
    # is extremely expensive.
                               