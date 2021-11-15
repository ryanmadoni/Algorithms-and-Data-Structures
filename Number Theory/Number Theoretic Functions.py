"""
Author: Ryan Adoni
Date: 6/22/2021
Description: Number Theoretic Functions
"""

from math import ceil, sqrt
from operator import mul
from functools import reduce



factorizations = {} # A dictionary to memoize the prime factorizations in the primeFactor function.

def primeFactor(n):
    """
    Takes as input n, then calculates and returns the prime factorization of n.
    """  
    factors = [] # A list to store the prime factorization.
    tempn = n # A variable to hold the original value of n.
    
    # Removes all factors of 2 from the input number, n.
    while n % 2 == 0:
        n >>= 1 # Right shift by 1 bit to quickly divide by 2.
        factors.append(2) # Add 2 to the prime factorization.
      
    # If the input number, n, is now 1, n took the form 2^i, where i is in the set of natural numbers.
    if n == 1:
        return factors # Therefore, return the prime factorization.
    
    factor = 3 # Start at 3, the second prime number as we have dealt with 2 already.
    maxfactor = ceil(sqrt(n)) # Calculate the maximum factor as after this number there are repeats.

    # Loop until we reach the factor or n is not in factorizations.
    while factor <= maxfactor and n not in factorizations:

        # Ff the input number, n, is divisible by the variable factor it means that we have found a new prime factor.
        if n % factor == 0:
            n /= factor # Divide out the prime factor.
            factors.append(factor) # Add the current factor to the prime factorization.
            maxfactor = ceil(sqrt(n)) # Recalculate the maximum factor.
        else:
            factor += 2 # Add 2 as we start on 3, an odd number, and 2 is the only even prime number, so we can skip all even numbers.  This is why we deal with 2 first.
    
    # Check if n is in factorizations, i.e, this was calculated already.
    if n in factorizations:
        factors += factorizations[n] # Append the dictionary value.
        return factors # Return the factors.
    
    factors.append(round(n)) # Add the largest prime factor to the prime factorization list.
    factorizations[tempn] = factors # Set the value of n in to the dictionary.
    
    return factors # Return the prime factorization of n.



def phi(n):
    """
    Takes as input a positive integer, n, then returns phi(n), the number of numbers less than n which are relatively prime to n.
    """
    return round(n * reduce(mul, [1 - (1 / factor) for factor in set(primeFactor(n))])) # Calculate phi(n) using a formula using n's prime factorization.



def d(n):
    """
    Takes as input n, then calculates and returns the sum of all proper divisors of n.
    """
    s = 1 # A counter to store the sum of all the divisors of n.
    
    # Loop through all the numbers up to the square root of n.
    for d in range(2, floor(sqrt(n)) + 1):
        
        # If d | n then d and n // d are divisors of n.
        if n % d == 0:
            s += (d + n // d if d != n // d else d) # Add the divisors to the running sum.
            
    return s # Return the sum of the all the divisors of n.
