"""
Author: Ryan Adoni
Date: 18/15/2021
Description: The Collatz Sequence 
"""

def collatzSequenceLength(n):
    """
    Takes as input n, then computes and returns the length of the Collatz Sequence starting at n.
    """
    
    # If n is 1, then terminate.
    if n == 1:
        return 1 # Return 1.
    
    return 1 + collatzSequenceLength(3 * n + 1 if n % 2 else n / 2) # Return the 1 plus the length of the Collatz Sequence starting at the next number. n -> n / 2 if n is even and n -> 3 * n + 1 otherwise.


def memoizedCollatzSequenceLength(n, d):
    """
    Takes as input n, then calls the helper function to do the work to 
    compute and return the length of the Collatz Sequence starting at n.
    """
    def memoizedCollatzSequenceLengthHelper(n):
        """
        Takes as input n, then computes and returns the length of the Collatz Sequence starting at n.
        """
        
        # If n is 1, then terminate.
        if n == 1:
            return 1 # Return 1.
        
        # If n is divisible by 2 (even), then terminate.
        if n % 2 == 0:
            
            # If n / 2 is in the dictionary, then return the value already calculated that has been stored.
            if n / 2 in d:
                return d[n / 2] # Return the calculated value that has been stored.

            d[n / 2] = 1 + memoizedCollatzSequenceLengthHelper(n / 2) # Calculate and store in the dictionary, d, 1 plus the length of the Collatz Sequence starting at the next number. n -> n / 2 since n is odd.
            return d[n / 2] # Return the calculated value that has been stored.
        
        # If 3n + 1 is in the dictionary, then return the value already calculated that has been stored.
        if 3 * n + 1 in d:
            return d[3 * n + 1] # Return the calculated value that has been stored.
        
        d[3 * n + 1] = 1 + memoizedCollatzSequenceLengthHelper(3 * n + 1) # Calculate and store in the dictionary, d, 1 plus the length of the Collatz Sequence starting at the next number. n -> 3n + 1 since n is odd.
        return d[3 * n + 1] # Return the calculated value that has been stored.
    
    return memoizedCollatzSequenceLengthHelper(n), d # Return the helpers return value, the length of the Collatz Sequence starting at n.
