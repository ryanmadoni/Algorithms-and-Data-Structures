"""
Author: Ryan Adoni
Date: 9/22/2021
Description: Newton's Method for interpolation.
"""


def NewtonInterpolation(L, x):
    """
    Takes as input a list of 2-tuples, i.e., points, L, then
    interpolates and returns f(x), where f is the unique
    len(L) - 1 degree polynomial containing all points in L.
    Uses Newton Interpolation with Divided Differences.
    """

    def dividedDifferences(L):
        """
        Takes as input a list, L, that contains 2-tuples representing points,
        then applies Newton's Divided Difference formula to create a table
        of divided differences that can be used in Newton Interpolation.
        """
        length = len(L)  # Get the number of points.

        # Instantiate an array of zeros to hold the divided differences.
        DD = [[0] * (length + 1) for _ in range(length)]

        # Loop to add the coordinates from L to
        # the divided difference table, DD.
        for r in range(length):
            DD[r][0], DD[r][1] = L[r]  # Set the correct cells.

        # Loop for every degree in the divided difference table above 1.
        for degree in range(2, length + 1):

            # Loop for every row.
            for r in range(length - degree + 1):

                # Calculate the divided difference.
                numerator = DD[r+1][degree-1] - DD[r][degree-1]
                denominator = DD[r+degree-1][0] - DD[r][0]
                DD[r][degree] = numerator / denominator

        return DD  # Return the table of divided differences.

    def interpolate(DD, x):
        """
        Takes as input a 2D list, DD, that represents a table of divided
        differences (the output from the above dividedDifferences(L)
        formula) and an integer, x, then uses Newton's interpolation
        interpolate the point at x
        """

        # Initialize two variables: one to store the
        # approximation of f(x) and one to store a partial product, p.
        fx, p = 0, 1

        # Loop for all values except the first in the first
        # row of the divided difference table, DD.
        for d in range(1, len(DD[0])):
            fx += DD[0][d] * p  # Add the partial sum to f(x), fx.
            p *= x - DD[d - 1][0]  # Update the partial product.

        return int(fx)  # Return f(x), fx, the interpolation of x.

    return interpolate(dividedDifferences(L), x)  # Return the value of f(x).


if __name__ == "__main__":

    # Test for interpolation on a line.
    print(NewtonInterpolation([(0, 0), (1, 1)], 5))
