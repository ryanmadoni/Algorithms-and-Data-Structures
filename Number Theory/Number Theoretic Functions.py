"""
Author: Ryan Adoni
Date: 6/22/2021
Description: Number Theoretic Functions
"""

from math import ceil, sqrt, floor
from operator import mul
from functools import reduce


# A dictionary to memoize the prime factorizations
# in the primeFactor function.
factorizations = {}


def primeFactor(n):
    """
    Takes as input n, then calculates and returns the prime factorization of n.
    """
    factors = []  # A list to store the prime factorization.
    tempn = n  # A variable to hold the original value of n.

    # Removes all factors of 2 from the input number, n.
    while n % 2 == 0:
        n >>= 1  # Right shift by 1 bit to quickly divide by 2.
        factors.append(2)  # Add 2 to the prime factorization.

    # If the input number, n, is now 1, n took the form
    # 2^i, where i is in the set of natural numbers.
    if n == 1:
        return factors  # Therefore, return the prime factorization.

    factor = 3  # Start at 3, the second prime number.
    maxfactor = ceil(sqrt(n))  # Calculate the maximum factor.

    # Loop until we reach the factor or n is not in factorizations.
    while factor <= maxfactor and n not in factorizations:

        # If the input number, n, is divisible by the variable
        # factor it means that we have found a new prime factor.
        if n % factor == 0:
            n /= factor  # Divide out the prime factor.
            factors.append(factor)  # Append the current factor to factors.
            maxfactor = ceil(sqrt(n))  # Recalculate the maximum factor.
        else:
            # Add 2 as we start on 3, an odd number, and 2 is the only
            # even prime number, so we can skip all even numbers.
            # This is why 2 is dealt with first.
            factor += 2

    # Check if n is in factorizations, i.e, this was calculated already.
    if n in factorizations:
        factors += factorizations[n]  # Append the dictionary value.
        return factors  # Return the factors.

    factors.append(round(n))  # Append the largest prime factor to factors.
    factorizations[tempn] = factors  # Set the value of n in to the dictionary.

    return factors  # Return the prime factorization of n.


def phi(n):
    """
    Takes as input a positive integer, n, then returns phi(n),
    the number of numbers less than n which are relatively
    prime to n.  Phi is known as Euler's Totient Function.
    """

    # Calculate phi(n) using a formula using n's prime factorization.
    factors = [1 - (1 / factor) for factor in set(primeFactor(n))]
    return round(n * reduce(mul, factors))


def little_omega(n):
    """
    Takes as input a positive integer, n, then returns the number
    of distinct primes in the prime factorization of n.
    """

    # Return the number of distinct primes
    # in the prime factorization of n.
    return len(set(primeFactor(n)))


def big_omega(n):
    """
    Takes as input a positive integer, n, then returns the number
    of non-distinct primes in the prime factorization of n.
    """

    # Return the number of non-distinct primes
    # in the prime factorization of n.
    return len(primeFactor(n))


def d(n):
    """
    Takes as input n, then calculates and returns
    the sum of all proper divisors of n.
    """
    s = 1  # A counter to store the sum of all the divisors of n.

    # Loop through all the numbers up to the square root of n.
    for d in range(2, floor(sqrt(n)) + 1):

        # If d | n then d and n // d are divisors of n.
        if n % d == 0:
            s += (d + n // d if d != n // d else d)  # Add divisors to the sum.

    return s  # Return the sum of the all the divisors of n.


if __name__ == "__main__":

    print(primeFactor(100))  # Get the prime factoriation of 100.
    print(phi(100))  # The number of numbers coprime to 100.
    print(little_omega(100))  # The number of distinct prime factors of 100.
    print(big_omega(100))  # The number of non-distinct prime factors of 100.

    # Convert this file to a .ipynb and show formulas for number
    # theoretic functions.
