"""
Author: Ryan Adoni
Date: 9/18/2021
Description: A file containing different sieves to find prime numbers.
"""

import timeit

def sieveOfEratosthenes(n):
    """
    Takes as input a positive integer, n, then calculates and returns all primes less than n using the 
    Sieve of Eratosthenes.
    """
    prime = [1] * n # Create a list for the Sieve of Eratosthenes.
    prime[0] = prime[1] = 0 # Set the first two numbers to not prime.
    p = 2 # Start the counter at 2 as 1 would cross off all numbers.
    
    # Use the Sieve of Eratosthenes.
    while p * p <= n:
        
        # Check if p is prime.
        if prime[p]:
              
            # Remove all multiples of p from being prime.
            for i in range(p * 2, n, p):
                prime[i] = 0 # Set the value to false since it is not prime.

        p += 1 # Increment p by 1.
         
    return [p for p in range(n) if prime[p]] # Return a list of all primes less than n.



def sieveOfSundaram(n):
    """
    Takes as input a positive integer, n, then calculates and returns all primes less than n using the 
    Sieve of Sundaram.
    """
    k = ((n - 2) >> 1) + 1 # Set the value k to the floor(n - 2) + 1.
    prime = [1] * k # Set a list for the possible prime numbers.

    # Loop for all k values.
    for i in range(1, k):
        j = i # Set i equal to j.

        # Loop until i+j + 2*i*j >= k.
        while (v := i + j + (i * j << 1)) < k:
            prime[v] = 0 # Set the value in the prime list to 0.
            j += 1 # Increment j.

    return ([2] if n > 2 else []) + [2 * p + 1 for p in range(1, k) if prime[p]] # Return a list of all the primes less than n.

    

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

    # print(sieveOfEratosthenes(100)) # Find all primes less then 100.
    # print(sieveOfSundaram(100)) # Find all primes less then 100.

    print(timeit.timeit(wrapper(sieveOfEratosthenes, 1000), number = 10)) # Run and time the recursive definition.
    print(timeit.timeit(wrapper(sieveOfSundaram, 1000), number = 10)) # Run and time the matrix definition.

    # My implementations of the Sieve of Eratosthenes runs faster 2x faster than my implemntation of
    # the Sieve of Sundaram.

    