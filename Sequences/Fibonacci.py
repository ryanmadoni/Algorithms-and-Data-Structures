"""
Author: Ryan Adoni
Date: 9/22/2021
Description: The Fibonacci Sequence 
"""

import timeit
import sys

sys.setrecursionlimit(10000)

def recursiveFibonnaci(n):
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

    return recursiveFibonnaci(n - 1) + recursiveFibonnaci(n - 2) # Recurse to return the nth Fibonacci number.


def iterativeFibonnaci(n):
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

    print(timeit.timeit(wrapper(recursiveFibonnaci, 10), number = 100)) # Run and time the recursive definition.
    print(timeit.timeit(wrapper(iterativeFibonnaci, 10), number = 100)) # Run and time the iterative definition.