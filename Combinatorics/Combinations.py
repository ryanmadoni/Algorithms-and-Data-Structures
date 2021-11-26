"""
Author: Ryan Adoni
Date: 9/22/2021
Description: Functions relating to combinations.
"""

from math import factorial


def ncr(n, r):
    """
    Takes as input two positive integers, n and r, then calculates
    and returns (n r) = n! / r!(n - r)!
    """

    # Calculate and return (n r).
    return factorial(n) / (factorial(r) * factorial(n - r))
