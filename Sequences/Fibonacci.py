"""
Author: Ryan Adoni
Date: 9/22/2021
Description: 
"""

def recursiveFibonnaci(n):
    """
    An implementation of the Fibonacci sequence using recursion (a pretty poor implementation).  Takes in a
    positive integer or zero, n, and returns the nth Fibonacci number.
    """

    # Make sure a valid n was entered.
    if n < 0: 
        return None # Return None if a number less than 1 was entered.

    # The base case for the recursion
    if n <= 2:
        return 0 if n == 0 else 1 # return 1 for the first and second Fibonacci number.  Return 0 for the zeroth Fibonacci number.

    return recursiveFibonnaci(n - 1) + recursiveFibonnaci(n - 2) # Recurse to return the nth Fibonacci number.


if __name__ == "__main__":
    print(recursiveFibonnaci(10))