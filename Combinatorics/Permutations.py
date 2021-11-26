"""
Author: Ryan Adoni
Date: 7/29/2021
Description: Functions relating to permutations.
"""


from itertools import permutations


def nextLexicographicPermutations(s):
    """
    Takes as input s, a string, and generates the next lexicographic
    permutation of s.  The next permutation is yielded and a generator
    can be used to continuously generate the subsequent permutations.
    """
    s = list(s)  # Convert the string passed in into a list.

    # Loop until there are no more permutations.
    while True:
        i = j = len(s) - 1  # Set i and j to the last index of the list.

        # Loop from the end of the list representing the string to the
        # beginning to find the non-increasing suffix.
        while i > 0 and s[i - 1] >= s[i]:
            i -= 1  # Decrement the looping variable.

        # Check if i <= 0.  If this is true, there are no more
        # lexicographic permutations.
        if i <= 0:
            return  # Stop the generator.

        # Loop through from the end of the list representing the
        # string to the beginning to find the successor to pivot.
        while s[j] <= s[i - 1]:
            j -= 1  # Decrement the looping variable.

        s[i - 1], s[j] = s[j], s[i - 1]  # Swap the i-1th and jth elements.
        s[i:] = s[len(s)-1: i-1: -1]  # Reverse the suffix.

        yield "".join(s)  # Yield the result after converting to a string.


def nthLexicographicPermutationPython(s, n):
    """
    Takes as input a string, s, and a number, n, and return the nth
    lexicographic permutation of s if it exists.  Returns None otherwise.
    Uses Native Python.
    """

    # Use the built in lexicographic permutation finder in Python,
    # then return the nth permutation if it exists.
    perms = sorted(''.join(c) for c in permutations(s))
    return None if len(perms) < n - 1 else perms[n - 1]
