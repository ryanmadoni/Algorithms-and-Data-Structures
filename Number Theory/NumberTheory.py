"""
Author: Ryan Adoni
Date: 9/18/2021
Description: 
"""

def sieveOfEratosthenes(n):
    """
    Takes as input n, then calculates and returns all primes less than n using the Sieve of Eratosthenes
    """
    prime = [True for _ in range(n)] # create a list for the Sieve of Eratosthenes
    prime[0] = prime[1] = False # set the first two numbers to not prime
    p = 2 # start the counter at 2 as 1 would cross off all numbers
    
    # use the Sieve of Eratosthenes
    while p * p <= n:
        
        # check if p is prime
        if prime[p]:
              
            # remove all multiples of p from being prime
            for i in range(p * 2, n, p):
                prime[i] = False # set the value to false since it is not prime
        p += 1 # increment p by 1
         
    return [p for p in range(len(prime)) if prime[p]] # return a list of all primes less than n



if __name__ == "__main__":
    print(sieveOfEratosthenes(100)) # Find all primes less then 100.
    