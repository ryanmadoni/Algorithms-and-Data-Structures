"""
Author: Ryan Adoni
Date: 8/29/2021
Description: Functions relating to binary trees and binary search trees.
"""

from itertools import groupby, chain
from operator import itemgetter
import unittest


class BinaryTree:
    """
    A class to represent a binary tree and
    functions that can be applied to them.
    """

    def __init__(self, data, left=None, right=None):
        """
        The constructor for the BinaryTree class that represents a binary tree.
        By default the left and right subtree are None values, i.e., leaves.
        """

        # Initialize the variables for the data,
        # the left subtree, and the right subtree.
        self.data, self.left, self.right = data, left, right

    def preOrder(self):
        """
        Takes self as input, then returns a list representing
        the preorder traversal of the nodes in the binary tree.
        """

        # Return the data of self plus the recursion
        # on the left and right subtrees if they are
        # not None, i.e., they are not leaves.
        left = (self.left.preOrder() if self.left is not None else [])
        right = (self.right.preOrder() if self.right is not None else [])
        return [self.data] + left + right

    def inOrder(self):
        """
        Takes self as input, then returns a list representing
        the inorder traversal of the nodes in the binary tree.
        """

        # Return the recursion on the left subtree plus the
        # data of self plus the recursion on the right
        # subtree.  Recurse only if the left and right
        # subtrees are not None, i.e., they are not leaves.
        left = (self.left.inOrder() if self.left is not None else [])
        right = (self.right.inOrder() if self.right is not None else [])
        return left + [self.data] + right

    def postOrder(self):
        """
        Takes self as input, then returns a list representing
        the postorder traversal of nodes in the binary tree.
        """

        # Return the recursion on the left subtree plus the recursion
        # on the right subtree plus the data of self.  Recurse only if
        # the left and right subtrees are not None, i.e., they are not leaves.
        left = (self.left.postOrder() if self.left is not None else [])
        right = (self.right.postOrder() if self.right is not None else [])
        return left + right + [self.data]

    def levelOrder(self):
        """
        Takes self as input, then returns a list representing
        the level order traversal of nodes in the binary tree.
        """
        def helper(binaryTree, level):
            """
            A helper function to help get the level order of self.  This
            function gets the preorder traversal of self, but each node's
            value is put into a two-tuple pair with its current level.
            """
            left = (helper(binaryTree.left, level+1) if
                    binaryTree.left is not None else [])
            right = (helper(binaryTree.right, level+1) if
                     binaryTree.right is not None else [])
            return [(level, binaryTree.data)] + left + right

        # Use itertools.groupby to group the preorder traversal obtained
        # from the helper to group each level, then trim the level metadata
        # and chain the final list of lists.  This is an extremely Pythonic
        # way of coding this function.  A preorder traversal is arbitrarily
        # used here to simply traverse the binary tree, but it could be any
        # traversal: preorder, inorder, or postorder.
        grouped = groupby(sorted(helper(self, 0),
                                 key=itemgetter(0)), lambda p: p[0])
        levels = [[pair[1] for pair in group] for _, group in grouped]
        return list(chain.from_iterable(levels))

    def inverse(self):
        """
        Takes as input self, then returns the inverse
        or mirror of the binary tree, self
        """

        # Invert/Mirror each subtree recursively if the left and
        # right subtrees are not None, i.e., they are not leaves.
        left = self.right.inverse() if self.right is not None else None
        right = self.left.inverse() if self.left is not None else None
        return BinaryTree(self.data, left, right)

    def numberOfNodes(self):
        """
        Takes as input self, then returns the
        number of nodes in the binary tree, self
        """

        # Check if the current node is a leaf, i.e.,
        # both its left and right branches are None.
        if self.left is None and self.right is None:
            return 1  # Return 1 since a leaf has been found.

        # Return the number of nodes on the left and
        # right branches of self if they are not None
        # and add 1 to count the current node.
        left = (self.left.numberOfNodes() if self.left is not None else 0)
        right = (self.right.numberOfNodes() if self.right is not None else 0)
        return left + right + 1

    def numberOfLeaves(self):
        """
        Takes as input self, then returns the number
        of leaves in the binary tree, self
        """

        # Check if the current node is a leaf, i.e.,
        # both its left and right branches are None.
        if self.left is None and self.right is None:
            return 1  # Return 1 since a leaf has been found.

        # Return the number of leaves on the left and
        # right branches of self if they are not None.
        left = (self.left.numberOfLeaves() if self.left is not None else 0)
        right = (self.right.numberOfLeaves() if self.right is not None else 0)
        return left + right

    def numberOfInternalNodes(self):
        """
        Takes as input self, then returns the number
        of internal nodes in the binary tree, self.
        """

        # Returns the number of internal nodes, i.e.,
        # the number of total nodes minus the number
        # of leaves.  This can also be done without
        # these helper functions by mimicking the format
        # of the two functions numberOfNodes() and
        # numberOfLeaves(), but returning 0 when the
        # base case is reached, i.e., a leaf is reached.
        return self.numberOfNodes() - self.numberOfLeaves()

    def paths(self):
        """
        Takes as input self, then returns a list of lists
        representing all possible simple paths from the root
        to every leaf in self.
        """

        def helper(binaryTree, path):
            """
            A helper to help find all the paths from
            the root to every leaf in binaryTree.
            """

            # Check if the current node is a leaf, i.e.,
            # both its left and right branches are None.
            if binaryTree.left is None and binaryTree.right is None:

                # Return the path since a leaf has been reached.
                return [path + [binaryTree.data]]

            # Recurse to return the paths on the
            # left and right subtrees of binaryTree.
            newPath = path + [binaryTree.data]
            left = (helper(binaryTree.left, newPath) if
                    binaryTree.left is not None else [])
            right = (helper(binaryTree.right, newPath) if
                     binaryTree.right is not None else [])
            return left + right

        # Call the helper to execute the work and get all possible
        # simple paths from the root to every leaf in self.
        return helper(self, [])

    def pathSum(self, n):
        """
        Takes as input self and an integer n, then returns a list
        representing the first simple path-if one exists in self
        such that the path's sum is equal to n.  Returns an empty
        list, [], if the sum cannot be made.
        """

        # Try to execute the following line of code,
        # which can raise a ValueError if n is not
        # in the call to paths(), paths.
        try:

            # return paths indexed at the index
            # of n if n is in the list where paths
            # is mapped to the sum function.
            return (paths := self.paths())[list(map(sum, paths)).index(n)]

        # Catch the ValueError.
        except ValueError:

            # Return [] since the call to
            # index() returned a ValueError.
            return []

    def contains(self, subtree):
        """
        Takes as input self and a BinaryTree, subtree, then returns a boolean
        value denoting if the subtree, subtree, is contained in the binary
        tree, self.  Returns True if subtree is contained and False otherwise.
        """

        # Return whether the tree rooted as self is equal to
        # subtree, then or that result with the recursion of
        # the left and right branches of self if they are not None.
        left = (self.left.contains(subtree) if
                self.left is not None else False)
        right = (self.right.contains(subtree) if
                 self.right is not None else False)
        return self == subtree or left or right

    def height(self):
        """
        Takes as input self and returns the height, or maximum depth, of the
        binary tree, self.  Height can be defined as either the number of
        nodes or number of connections between nodes.  This function will
        measure height in nodes.
        """

        # Check if the current node is a leaf, i.e.,
        # both its left and right branches are None.
        if self.left is None and self.right is None:
            return 1  # Return 1 since a leaf has been found.

        # Return the max of the number of leaves on the left and right branches
        # of self if they are not None, i.e., the height of the binary tree,
        # self, then add one for the current node.
        q1 = self.left.height() if self.left is not None else 0
        q2 = self.right.height() if self.right is not None else 0
        return max(q1, q2) + 1

    def width(self, level):
        """
        Takes as input self and a non-negative integer, level, then returns
        the width of the level, level, in the binary tree, self.  The width
        of a level in a binary tree is the number of nodes in a certain level.
        """

        def helper(binaryTree, level):
            """
            A helper function to help get the width of a specific level of
            self.  This function gets the preorder traversal of self, but each
            node's value is put into a two-tuple pair with its current level.
            """
            left = (helper(binaryTree.left, level+1) if
                    binaryTree.left is not None else [])
            right = (helper(binaryTree.right, level+1) if
                     binaryTree.right is not None else [])
            return [(level, binaryTree.data)] + left + right

        # Use itertools.groupby to group the preorder traversal obtained
        # from the helper to group each level, then get the length of the
        # specific level if it exists.  This is an extremely Pythonic way of
        # coding this function.  A preorder traversal is arbitrarily used
        # here to simply traverse the binary tree, but it could be any
        # traversal: preorder, inorder, or postorder.
        grouped = groupby(sorted(helper(self, 0)), lambda p: p[0])
        L = [list(group) for _, group in grouped]
        return len(L[level]) if level < len(L) else 0

    def maxWidth(self):
        """
        Takes as input self, then returns the
        maximum width of the tree, self.
        """
        def helper(binaryTree, level):
            """
            A helper function to help get the max width of
            self.  This function gets the preorder traversal
            of self, but each node's value is put into a
            two-tuple pair with its current level.
            """
            left = (helper(binaryTree.left, level + 1) if
                    binaryTree.left is not None else [])
            right = (helper(binaryTree.right, level + 1) if
                     binaryTree.right is not None else [])
            return [(level, binaryTree.data)] + left + right

        # Use itertools.groupby to group the preorder traversal
        # obtained from the helper to group each level, then
        # get the max width of the binary tree, self.  This is
        # an extremely Pythonic way of coding this function.  A
        # preorder traversal is arbitrarily used here to simply
        # traverse the binary tree, but it could be any traversal:
        # preorder, inorder, or postorder
        grouped = groupby(sorted(helper(self, 0)), lambda p: p[0])
        return max([len(list(group)) for _, group in grouped])

    def diameter(self):
        """
        Takes as input self, then returns the diameter of the binary
        tree, self.  The diameter of a binary tree is defined as the
        number of nodes on the longest path between any two leaves in
        the binary tree.
        """

        # Return the height of the left and right subtrees
        # plus 1 for the current node if it is not None.
        left = (self.left.height() if self.left is not None else 0)
        right = (self.right.height() if self.right is not None else 0)
        return left + 1 + right

    def isLeftSkewed(self):
        """
        Takes as input self, then returns a boolean value denoting
        if the binary tree, self, is left skewed.  Returns True if
        the binary tree, self, is left skewed and False otherwise.
        A binary tree is left skewed if every node has exactly one
        child and every node does not have right children.
        """

        # Check if the current node is a leaf, i.e.,
        # both its left and right branches are None.
        if self.left is None and self.right is None:
            return True  # Return True since a leaf has been reached.

        # Return whether a left subtree of self is
        # left skewed and self has no right children.
        return False if self.right is not None else self.left.isLeftSkewed()

    def isRightSkewed(self):
        """
        Takes as input self, then returns a boolean value denoting
        if the binary tree, self, is right skewed.  Returns True if
        the binary tree, self, is right skewed and False otherwise.
        A binary tree is right skewed if every node has exactly one
        child and every node does not have left children.
        """

        # Check if the current node is a leaf, i.e.,
        # both its left and right branches are None.
        if self.left is None and self.right is None:
            return True  # Return True since a leaf has been reached.

        # Return whether a right subtree of self is
        # right skewed and self has no left children.
        return False if self.left is not None else self.right.isRightSkewed()

    def isDegenerate(self):
        """
        Takes as input self, then returns a boolean value denoting
        if the binary tree, self, is degenerate.  Returns True if
        the binary tree, self, is degenerate (a.k.a. pathological)
        and False otherwise.  A binary tree is degenerate or pathological
        if every node has exactly one child, i.e., the binary tree
        degenerates to a linked list.
        """

        # Check if the current node is a leaf, i.e.,
        # both its left and right branches are None.
        if self.left is None and self.right is None:
            return True  # Return True since a leaf has been reached.

        # Check if the binary tree, self, only has one child, a left child.
        if self.left is not None and self.right is None:

            # Recurse down the left branch of the binary tree, self.
            return self.left.isDegenerate()

        # Check if the binary tree, self, only has one child, a right child.
        if self.left is None and self.right is not None:

            # Recurse down the right branch of the binary tree, self.
            return self.right.isDegenerate()

        # Return False because the binary
        # tree, self, has two children.
        return False

    def isBalanced(self):
        """
        Takes as input self, then returns a boolean value denoting if
        the binary tree, self, is balanced.  Returns True if the binary
        tree, self, is balanced and False otherwise.  A balanced binary
        tree is a binary tree in which the heights of every left and right
        subtree can differ by at most 1.
        """

        # Return whether the absolute difference of the binary tree's left
        # and right subtrees' heights is less than one and whether the left
        # and right subtrees of the binary tree, self, are balanced if they
        # exist.
        leftHeight = (self.left.height() if self.left is not None else 0)
        rightHeight = (self.right.height() if self.right is not None else 0)
        difference = abs(leftHeight - rightHeight)
        leftBalanced = (self.left.isBalanced() if
                        self.left is not None else True)
        rightBalanced = (self.right.isBalanced() if
                         self.right is not None else True)
        return difference <= 1 and leftBalanced and rightBalanced

    def isFull(self):
        """
        Takes as input self, then returns a boolean value denoting
        if the binary tree, self, is full.  Returns True if the binary
        tree, self, is full and False otherwise.  A full binary tree
        is a binary tree if every node has 0 or 2 children.
        """

        # Check if the current node is a leaf, i.e.,
        # both its left and right branches are None.
        if self.left is None and self.right is None:
            return True  # Return True since a leaf has been reached.

        # Check if the current node has two children, i.e.,
        # both its left and right branches are not None.
        if self.left is not None and self.right is not None:

            # Return the recursion of the left and right subtrees.
            return self.left.isFull() and self.right.isFull()

        # Return False since the binary
        # tree, self, has one child.
        return False

    def level(self, level):
        """
        Takes as input self and a non-negative integer, then returns
        a list representing the corresponding level in self.
        """
        def helper(binaryTree, level):
            """
            A helper function to help get the level of self.  This
            function gets the preorder traversal of self, but each
            node's value is put into a two-tuple pair with its current level.
            """
            left = (helper(binaryTree.left, level + 1) if
                    binaryTree.left is not None else [(level + 1, None)])
            right = (helper(binaryTree.right, level + 1) if
                     binaryTree.right is not None else [(level + 1, None)])
            return [(level, binaryTree.data)] + left + right

        # Use itertools.groupby to group the preorder traversal obtained
        # from the helper to group each level, then get the level desired
        # if that level exists.  This is an extremely Pythonic way of coding
        # this function.  A preorder traversal is arbitrarily used here to
        # simply traverse the binary tree, but it could be any traversal:
        # preorder, inorder, or postorder
        grouped = groupby(sorted(helper(self, 0), key=itemgetter(0)),
                          lambda p: p[0])
        levels = [[pair[1] for pair in list(group)] for _, group in grouped]
        return levels[level] if level < self.height() else []

    def isComplete(self):
        """
        Takes as input self, then returns a boolean value denoting if the
        binary tree, self, is complete.  Returns True if the binary tree,
        self, is complete and False otherwise.  A complete binary tree is
        a binary tree in which all levels are completely filled except possibly
        the last level and the last level has all keys as left as possible.
        """

        # Instantiate two variables: one to keep track of the current level
        # and a boolean keeping track if the binary tree is complete.
        level, complete = 0, True

        # Loop until the call to level yields an empty list, [].
        while (values := self.level(level)) != []:

            # Check if None is in values.
            if None in values:

                # Instantiate a boolean to see if a None
                # has been found in the list, values.
                found = False

                # Loop for each value in values.
                for value in values:

                    # Check if a None has been found.
                    if value is None:
                        found = True  # Set the boolean, found, to True.

                    # Check to see if a None has been found and a non None
                    # value is after it, i.e., the binary tree is incomplete.
                    if found and value is not None:
                        complete = False  # Set complete to False.

            level += 1  # Increment the level.

        # Return a boolean denoting whether
        # the binary tree, self is complete.
        return complete

    def isPerfect(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is perfect.
        Returns True if the binary tree, self, is perfect and False otherwise.  A perfect binary tree is
        a binary tree in which all internal nodes have two children and all leaves are at same level.
        """
        return self.numberOfNodes() == 2 ** self.height() - 1  # Check if the number of nodes equals 2 ^ (height) - 1, i.e., the binary tree, self, is perfect.

    def isBinarySearchTree(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is a binary
        search tree.  Returns True if the binary tree, self, is a binary search tree and False otherwise.
        A binary search tree is a binary tree that fulfills the following invariant: every left node's value
        and its childrens' values are less than its parent's value and every right node's value and its
        childrens' values are greater than its parent's value.
        """

        # Check if the binary search tree invariant is upheld and recurse to see if the children of self are
        # also binary search trees.
        return (all([node < self.data for node in self.left.preOrder()]) if self.left is not None else True) and \
               (all([self.data < node for node in self.right.preOrder()]) if self.right is not None else True) and \
               (self.left.isBinarySearchTree() if self.left is not None else True) and \
               (self.right.isBinarySearchTree() if self.right is not None else True)

    def binaryTreeString(self, level=0):
        """
        A function that takes as input a default value, level, that is used to space the string representation
        of the binary tree stored in self.  the variable level should not be used by the used by the caller and
        should be  left at its default value.
        """

        # Print the data stored in self, then initialize a variable, spacing, to hold the whitespace needed
        # to format the string, then recurse to print the left and right binary subtrees.
        return str(self.data) + (spacing := "\n" + (level + 1) * "  ") + (self.left.binaryTreeString(level + 1) if self.left is not None else "None") + spacing + (self.right.binaryTreeString(level + 1) if self.right is not None else "None")

    def __eq__(self, obj):
        """
        An overriden version of the object's equal method.  This function returns True if self and obj represent
        the same binary tree and return False otherwise.
        """

        # Check if obj is a BinaryTree and if they have the same preorder traversal, i.e.,
        # they represent the same binary tree.   A preorder traversal is arbitrarily used
        # here, but it could be any traversal: preorder, inorder, or postorder
        return isinstance(obj, BinaryTree) and self.preOrder() == obj.preOrder()


class BinarySearchTree(BinaryTree):
    """
    A class to represent a binary search tree and functions that can be applied to them.  This class is a child
    of the binary tree class, BinaryTree, above.  A binary search tree is a binary tree that fulfills the
    following invariant: every left nodes' value and its childrens' values are less than its parent's value
    and every right nodes' value and its childrens' values are greater than its parent's value.
    """

    def __init__(self, data):
        """
        The constructor for the BinarySearchTree class that represents a binary search tree.  Initializes the
        root data to data.
        """
        super().__init__(data)  # Call to super, i.e., parent's constructor, to initialize the root node to data.

    def insert(self, data):
        """
        Takes as input self and an integer, data, then adds data to
        the binary search tree, self, maintaining the binary search
        tree invariant; if the value data is not already inside the
        binary search tree, self, then it is added and True is returned;
        if the value is already inside the binary search tree, no value
        is added and False is returned.
        """

        # Check if the data is less than self's data.
        if data < self.data:

            # Check if the left subtree of self is empty.
            if self.left is None:
                self.left = BinarySearchTree(data)  # Add a new subtree with the value data.
                return True  # Return True since the value was added succesfully.

            return self.left.insert(data)  # Recurse down the left branch of the tree to add data to the binary search tree, self.

        # Check if the data is greater than self's data.
        if self.data < data:

            # Check if the rigth subtree of self is empty.
            if self.right is None:
                self.right = BinarySearchTree(data)  # Add a new subtree with the value data.
                return True  # Return True since the value was added succesfully.

            return self.right.insert(data)  # Recurse down the right branch of the tree to add data to the binary search tree, self.

        return False  # Return False since data and self's data are equal.

    def delete(self, data):
        """
        Takes as input self and an integer, data, then deletes data to the binary search tree, self, maintaining the
        binary search tree invariant; if the value data is inside the binary search tree, self, then it is
        deleted and True is returned; if the value is not inside the binary search tree, no value is deleted and
        False is returned.
        """

        def helper(self, data, parent, left):
            """
            A helper function to aid in the deletion of data.  Takes in the same variables as the outer function
            and additionally two other variables: parent, the parent node of self and left, a boolean denoting
            if the child of parent, self, is the left child of parent.  If the value data is inside the binary
            search tree, self, then it is deleted and True is returned; if the value is not inside the binary
            search tree, no value is deleted and False is returned.
            """

            # Check if the data of self is the
            # data that needs to be deleted.
            if self.data == data:

                # Check if self has two children
                if self.left is not None and self.right is not None:
                    self.data = min(self.right.preOrder())  # Set self's data to the smallest value in the right subtree of self (alternatively, this could have been the largest value in the left subtree).
                    return helper(self.right, self.data, self, False)  # Recurse to delete self.data in the right subtree to remove the duplicate value.

                # Check if self is a leaf.
                if self.left is None and self.right is None:
                    if left:
                        parent.left = None  # Set the left child of parent to None if left is True.
                    else:
                        parent.right = None  # Set the right child of parent to None if left is False.

                # Check if self has no right child and a has a left child.
                elif self.left is not None and self.right is None:
                    if left:
                        parent.left = self.left  # Set the left child of parent to the left child of self if left is True.
                    else:
                        parent.right = self.left  # Set the right child of parent to the left child of self if left is False.

                # Else, self has no left child and a has a right child.
                else:
                    if left:
                        parent.left = self.right  # set the left child of parent to the right child of self if left is True.
                    else:
                        parent.right = self.right  # set the right child of parent to the right child of self if left is False.

                return True  # Return True since a value has been deleted successfully.

            # Check if data is in the left subtree of self.
            elif self.left is not None and self.left.search(data):
                return helper(self.left, data, self, True)  # Recurse using the helper into the left subtree.

            # Check if data is in the right subtree of self.
            elif self.right is not None and self.right.search(data):
                return helper(self.right, data, self, False)  # Recurse using the helper into the right subtree.

            return False  # Return False since data is not conatained in self.

        return helper(self, data, None, None)  # Call the helper function to execute the work and return its result.

    def search(self, data):
        """
        Takes as input self and an integer, data, then returns True if data is
        contained within the Binary Search Tree, self; returns False otherwise.
        """

        # Recurse down the left and right subtrees if they are non None.
        # Then return if self.data is equal to data or the recursions.
        left = (self.left.search(data) if self.left is not None else False)
        right = (self.right.search(data) if self.right is not None else False)
        return self.data == data or right or left

    def inverse(self):
        """
        Override the inverse function since inverse cannot
        be applied to a binary search tree without breaking
        the binary search tree invariant.
        """
        pass  # Pass to remove functionality from the parent class, BinaryTree.


class TestBinaryTreeMethods(unittest.TestCase):
    """
    A class extending the unittest.TestCase class used to test the binary
    tree and binary search tree classes and their component functions above.
    """

    @classmethod
    def setUpClass(self):
        """
        The setUpClass function that will instantiate a few binary trees and
        binary search trees to work with for the testing of the functions.
        """

        # Define 9 binary trees to test the binary tree functions.
        self.binaryTree1 = BinaryTree(3,
                                      BinaryTree(2,
                                                 BinaryTree(1),
                                                 None),
                                      BinaryTree(4,
                                                 BinaryTree(2),
                                                 None))
        self.binaryTree2 = BinaryTree(1,
                                      BinaryTree(2,
                                                 BinaryTree(5),
                                                 BinaryTree(9)),
                                      BinaryTree(3,
                                                 BinaryTree(2,
                                                            BinaryTree(2),
                                                            None),
                                                 None))
        self.binaryTree3 = BinaryTree(1,
                                      BinaryTree(2,
                                                 None,
                                                 BinaryTree(3,
                                                            BinaryTree(4,
                                                                       BinaryTree(5),
                                                                       None),
                                                            None)),
                                      None)
        self.binaryTree4 = BinaryTree(1,
                                      BinaryTree(2),
                                      BinaryTree(3,
                                                 BinaryTree(4),
                                                 BinaryTree(4)))
        self.binaryTree5 = BinaryTree(1,
                                      BinaryTree(2,
                                                 BinaryTree(3,
                                                            BinaryTree(8),
                                                            BinaryTree(9)),
                                                 BinaryTree(4,
                                                            BinaryTree(10),
                                                            None)),
                                      BinaryTree(5,
                                                 BinaryTree(6),
                                                 BinaryTree(7)))
        self.binaryTree6 = BinaryTree(7,
                                      BinaryTree(3,
                                                 BinaryTree(1),
                                                 BinaryTree(5)),
                                      BinaryTree(10,
                                                 BinaryTree(8),
                                                 None))
        self.binaryTree7 = BinaryTree(7,
                                      BinaryTree(3,
                                                 BinaryTree(1),
                                                 BinaryTree(5)),
                                      BinaryTree(10,
                                                 BinaryTree(8),
                                                 None))
        self.binaryTree8 = BinaryTree(17,
                                      BinaryTree(8,
                                                 BinaryTree(3),
                                                 BinaryTree(14)),
                                      BinaryTree(25,
                                                 BinaryTree(20),
                                                 BinaryTree(30)))
        self.binaryTree9 = BinaryTree(17,
                                      BinaryTree(8,
                                                 BinaryTree(3),
                                                 BinaryTree(14)),
                                      BinaryTree(25,
                                                 BinaryTree(20),
                                                 None))

    def testBinaryTreeString(self):
        """
        A function to test the functionality of the
        class BinaryTree's binaryTreeString() function.
        """

        # The expected output of binaryTree1's
        # and binaryTree2's call to binaryTreeString().
        test1 = ("3\n  2\n    1\n      None\n      None\n    "
                 "None\n  4\n    2\n      None\n      None\n    None")
        test2 = ("1\n  2\n    5\n      None\n      None\n    9\n      "
                 "None\n      None\n  3\n    2\n      2\n        "
                 "None\n        None\n      None\n    None")

        # Check if the calls to the binaryTreeString() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.binaryTreeString(), test1)
        self.assertEqual(self.binaryTree2.binaryTreeString(), test2)

    def testPreOrder(self):
        """
        A function to test the functionality of the
        class BinaryTree's preOrder() function.
        """
        # The expected output of binaryTree1's
        # and binaryTree2's calls to preOrder().
        preOrder1, preOrder2 = [3, 2, 1, 4, 2], [1, 2, 5, 9, 3, 2, 2]

        # Check if the calls to the preOrder() function yield
        # the correct output for different binary trees.
        self.assertEqual(self.binaryTree1.preOrder(), preOrder1)
        self.assertEqual(self.binaryTree2.preOrder(), preOrder2)

    def testInOrder(self):
        """
        A function to test the functionality of the
        class BinaryTree's inOrder() function.
        """

        # The expected output of binaryTree1's
        # and binaryTree2's calls to inOrder().
        inOrder1, inOrder2 = [1, 2, 3, 2, 4], [5, 2, 9, 1, 2, 2, 3]

        # Check if the calls to the inOrder() function yield
        # the correct output for different binary trees.
        self.assertEqual(self.binaryTree1.inOrder(), inOrder1)
        self.assertEqual(self.binaryTree2.inOrder(), inOrder2)

    def testPostOrder(self):
        """
        A function to test the functionality of the
        class BinaryTree's postOrder() function.
        """

        # The expected output of binaryTree1's
        # and binaryTree2's calls to postOrder().
        postOrder1, postOrder2 = [1, 2, 2, 4, 3], [5, 9, 2, 2, 2, 3, 1]

        # Check if the calls to the postOrder() function yield
        # the correct output for different binary trees.
        self.assertEqual(self.binaryTree1.postOrder(), postOrder1)
        self.assertEqual(self.binaryTree2.postOrder(), postOrder2)

    def testLevelOrder(self):
        """
        A function to test the functionality of the
        class BinaryTree's levelOrder() function.
        """

        # The expected outputs of binaryTree1's
        # and binaryTree2's calls to levelOrder().
        levelOrder1, levelOrder2 = [3, 2, 4, 1, 2], [1, 2, 3, 5, 9, 2, 2]

        # Check if the calls to the levelOrder() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.levelOrder(), levelOrder1)
        self.assertEqual(self.binaryTree2.levelOrder(), levelOrder2)

    def testInverse(self):
        """
        A function to test the functionality of the
        class BinaryTree's inverse() function.
        """

        # The expected outputs of the calls to inverse() below.
        test1 = ("3\n  4\n    None\n    2\n      None\n      None"
                 "\n  2\n    None\n    1\n      None\n      None")
        test2 = ("1\n  3\n    None\n    2\n      None\n      2\n "
                 "       None\n        None\n  2\n    9\n      "
                 "None\n      None\n    5\n      None\n      None")

        # Check if the calls to the inverse() function yield
        # the correct output for different binary trees.
        self.assertEqual(self.binaryTree1.inverse().binaryTreeString(), test1)
        self.assertEqual(self.binaryTree2.inverse().binaryTreeString(), test2)

    def testEqual(self):
        """
        A function to test the functionality of the
        class BinaryTree's overridden equal() function.
        """

        # Check the equality and inequality
        # of different binary trees.
        self.assertNotEqual(self.binaryTree5, self.binaryTree6)
        self.assertEqual(self.binaryTree6, self.binaryTree7)

    def testNumberOfLeaves(self):
        """
        A function to test the functionality of the
        class BinaryTree's numberOfLeaves() function.
        """

        # Check if the calls to the numberOfLeaves() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.numberOfLeaves(), 2)
        self.assertEqual(self.binaryTree2.numberOfLeaves(), 3)
        self.assertEqual(self.binaryTree3.numberOfLeaves(), 1)
        self.assertEqual(self.binaryTree4.numberOfLeaves(), 3)

    def testNumberOfNodes(self):
        """
        A function to test the functionality of the
        class BinaryTree's numberOfNodes() function.
        """

        # Check if the calls to the numberOfNodes() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.numberOfNodes(), 5)
        self.assertEqual(self.binaryTree2.numberOfNodes(), 7)
        self.assertEqual(self.binaryTree3.numberOfNodes(), 5)
        self.assertEqual(self.binaryTree4.numberOfNodes(), 5)

    def testNumberOfInternalNodes(self):
        """
        A function to test the functionality of the
        class BinaryTree's numberOfInternalNodes() function.
        """

        # Check if the calls to the numberOfInternalNodes() function
        # yield the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.numberOfInternalNodes(), 3)
        self.assertEqual(self.binaryTree2.numberOfInternalNodes(), 4)
        self.assertEqual(self.binaryTree3.numberOfInternalNodes(), 4)
        self.assertEqual(self.binaryTree4.numberOfInternalNodes(), 2)

    def testPaths(self):
        """
        A function to test the functionality of the
        class BinaryTree's paths() function.
        """

        # Check if the calls to the paths() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.paths(), [[3, 2, 1],
                                                    [3, 4, 2]])
        self.assertEqual(self.binaryTree2.paths(), [[1, 2, 5],
                                                    [1, 2, 9],
                                                    [1, 3, 2, 2]])
        self.assertEqual(self.binaryTree3.paths(), [[1, 2, 3, 4, 5]])
        self.assertEqual(self.binaryTree8.paths(), [[17, 8, 3],
                                                    [17, 8, 14],
                                                    [17, 25, 20],
                                                    [17, 25, 30]])

    def testPathSum(self):
        """
        A function to test the functionality of the
        class BinaryTree's pathSum() function.
        """

        # Check if the calls to the pathSum() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.pathSum(6), [3, 2, 1])
        self.assertEqual(self.binaryTree2.pathSum(8), [1, 2, 5])
        self.assertEqual(self.binaryTree3.pathSum(2), [])
        self.assertEqual(self.binaryTree8.pathSum(39), [17, 8, 14])
        self.assertEqual(self.binaryTree8.pathSum(40), [])

    def testContains(self):
        """
        A function to test the functionality of the
        class BinaryTree's contains() function.
        """

        # Instantiate two subtrees, subtree1 and
        # subtree2, to test the contains() function.
        subtree1 = BinaryTree(2, BinaryTree(1, None), None)
        subtree2 = BinaryTree(3, BinaryTree(4), BinaryTree(4))

        # Check if the calls to the contains() function yield
        # the correct outputs for different binary trees and subtrees.
        self.assertEqual(self.binaryTree1.contains(subtree1), True)
        self.assertEqual(self.binaryTree2.contains(subtree1), False)
        self.assertEqual(self.binaryTree3.contains(subtree2), False)
        self.assertEqual(self.binaryTree4.contains(subtree2), True)

    def testHeight(self):
        """
        A function to test the functionality of the
        class BinaryTree's height() function.
        """

        # Check if the calls to the height() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.height(), 3)
        self.assertEqual(self.binaryTree2.height(), 4)
        self.assertEqual(self.binaryTree3.height(), 5)
        self.assertEqual(self.binaryTree4.height(), 3)

    def testWidth(self):
        """
        A function to test the functionality of the
        class BinaryTree's width() function.
        """

        # Check if the calls to the width() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.width(1), 2)
        self.assertEqual(self.binaryTree2.width(2), 3)
        self.assertEqual(self.binaryTree3.width(2), 1)
        self.assertEqual(self.binaryTree4.width(0), 1)

    def testMaxWidth(self):
        """
        A function to test the functionality of the
        class BinaryTree's maxWidth() function.
        """

        # Check if the calls to the maxWidth() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.maxWidth(), 2)
        self.assertEqual(self.binaryTree2.maxWidth(), 3)
        self.assertEqual(self.binaryTree3.maxWidth(), 1)
        self.assertEqual(self.binaryTree4.maxWidth(), 2)

    def testDiameter(self):
        """
        A function to test the functionality of the
        class BinaryTree's diameter() function.
        """

        # Check if the calls to the diameter() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.diameter(), 5)
        self.assertEqual(self.binaryTree2.diameter(), 6)
        self.assertEqual(self.binaryTree3.diameter(), 5)
        self.assertEqual(self.binaryTree4.diameter(), 4)

    def testIsBalanced(self):
        """
        A function to test the functionality of the
        class BinaryTree's isBalanced() function.
        """

        # Check if the calls to the isBalanced() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.isBalanced(), True)
        self.assertEqual(self.binaryTree2.isBalanced(), False)
        self.assertEqual(self.binaryTree3.isBalanced(), False)
        self.assertEqual(self.binaryTree4.isBalanced(), True)

    def testIsFull(self):
        """
        A function to test the functionality of the
        class BinaryTree's isFull() function.
        """

        # Check if the calls to the isFull() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.isFull(), False)
        self.assertEqual(self.binaryTree2.isFull(), False)
        self.assertEqual(self.binaryTree3.isFull(), False)
        self.assertEqual(self.binaryTree4.isFull(), True)
        self.assertEqual(self.binaryTree8.isFull(), True)
        self.assertEqual(self.binaryTree9.isFull(), False)

    def testIsComplete(self):
        """
        A function to test the functionality of the
        class BinaryTree's isComplete() function.
        """

        # Check if the calls to the isComplete() function yield
        # the correct output for different binary trees.
        self.assertEqual(self.binaryTree1.isComplete(), False)
        self.assertEqual(self.binaryTree2.isComplete(), False)
        self.assertEqual(self.binaryTree3.isComplete(), False)
        self.assertEqual(self.binaryTree4.isComplete(), False)
        self.assertEqual(self.binaryTree8.isComplete(), True)
        self.assertEqual(self.binaryTree9.isComplete(), True)

    def testIsPerfect(self):
        """
        A function to test the functionality of the
        class BinaryTree's isPerfect() function.
        """

        # Check if the calls to the isPerfect() function yield
        # the correct output for different binary trees.
        self.assertEqual(self.binaryTree1.isPerfect(), False)
        self.assertEqual(self.binaryTree2.isPerfect(), False)
        self.assertEqual(self.binaryTree3.isPerfect(), False)
        self.assertEqual(self.binaryTree4.isPerfect(), False)
        self.assertEqual(self.binaryTree8.isPerfect(), True)
        self.assertEqual(self.binaryTree9.isPerfect(), False)

    def testIsDegenerate(self):
        """
        A function to test the functionality of the
        class BinaryTree's isDegenerate() function.
        """

        # Check if the calls to the isDegenerate() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.isDegenerate(), False)
        self.assertEqual(self.binaryTree2.isDegenerate(), False)
        self.assertEqual(self.binaryTree3.isDegenerate(), True)
        self.assertEqual(self.binaryTree4.isDegenerate(), False)
        self.assertEqual(self.binaryTree8.isDegenerate(), False)
        self.assertEqual(self.binaryTree9.isDegenerate(), False)

    def testLevel(self):
        """
        A function to test the functionality of the
        class BinaryTree's level() function.
        """

        # Check if the calls to the level() function yield
        # the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.level(0), [3])
        self.assertEqual(self.binaryTree2.level(1), [2, 3])
        self.assertEqual(self.binaryTree3.level(2), [None, 3])
        self.assertEqual(self.binaryTree4.level(3), [])
        self.assertEqual(self.binaryTree8.level(2), [3, 14, 20, 30])
        self.assertEqual(self.binaryTree9.level(3), [])

    def testIsBinarySearchTree(self):
        """
        A function to test the functionality of the
        class BinaryTree's isBinarySearchTree() function.
        """

        # Check if the calls to the isBinarySearchTree() function
        # yield the correct outputs for different binary trees.
        self.assertEqual(self.binaryTree1.isBinarySearchTree(), False)
        self.assertEqual(self.binaryTree2.isBinarySearchTree(), False)
        self.assertEqual(self.binaryTree3.isBinarySearchTree(), False)
        self.assertEqual(self.binaryTree4.isBinarySearchTree(), False)
        self.assertEqual(self.binaryTree8.isBinarySearchTree(), True)
        self.assertEqual(self.binaryTree9.isBinarySearchTree(), True)

    def testInsert(self):
        """
        A function to test the functionality of the
        class BinarySearchTree's insert() function.
        """
        bst1 = BinarySearchTree(5)  # Create a binary search tree, bst1.

        # The expected output of binaryTree2's call to binaryTreeString().
        binarySearchTreeString1 = ("5\n  3\n    2\n      1\n        None\n"
                                   "        None\n      None\n    None\n  18\n"
                                   "    None\n    22\n      None\n      None")

        # Check if bst1's calls to the insert()
        # function yield the correct output.
        self.assertEqual(bst1.insert(3), True)
        self.assertEqual(bst1.insert(2), True)
        self.assertEqual(bst1.insert(1), True)
        self.assertEqual(bst1.insert(18), True)
        self.assertEqual(bst1.insert(18), False)
        self.assertEqual(bst1.insert(22), True)
        self.assertEqual(bst1.insert(2), False)

        # Check if bst1's call to the binaryTreeString()
        # function yields the correct output.
        self.assertEqual(bst1.binaryTreeString(), binarySearchTreeString1)

    def testDelete(self):
        """
        A function to test the functionality of the
        class BinarySearchTree's delete() function.
        """
        bst1 = BinarySearchTree(5)  # Create a binary search tree, bst1.

        # The expected output of binaryTree2's call to binaryTreeString().
        binarySearchTreeString1 = ("5\n  3\n    2\n      1\n        None\n"
                                   "        None\n      None\n    None\n  22\n"
                                   "    None\n    None")

        # Check if bst1's calls to the insert()
        # function yield the correct outputs.
        self.assertEqual(bst1.insert(3), True)
        self.assertEqual(bst1.insert(2), True)
        self.assertEqual(bst1.insert(1), True)
        self.assertEqual(bst1.insert(18), True)
        self.assertEqual(bst1.insert(18), False)
        self.assertEqual(bst1.insert(22), True)
        self.assertEqual(bst1.insert(2), False)

        # Check if bst1's calls to the delete()
        # function yield the correct outputs.
        self.assertEqual(bst1.delete(100), False)
        self.assertEqual(bst1.delete(18), True)

        # Check if bst1's call to the binaryTreeString()
        # function yields the correct output.
        self.assertEqual(bst1.binaryTreeString(), binarySearchTreeString1)

    def testSearch(self):
        """
        A function to test the functionality of the
        class BinarySearchTree's insert() function.
        """
        bst1 = BinarySearchTree(5)  # Create a binary search tree, bst1.

        # Check if bst1's calls to the insert()
        # function yield correct outputs.
        self.assertEqual(bst1.insert(3), True)
        self.assertEqual(bst1.insert(2), True)
        self.assertEqual(bst1.insert(1), True)
        self.assertEqual(bst1.insert(18), True)
        self.assertEqual(bst1.insert(18), False)
        self.assertEqual(bst1.insert(22), True)
        self.assertEqual(bst1.insert(2), False)

        # Check if bst1's calls to the search()
        # function yield the correct outputs.
        self.assertEqual(bst1.search(2), True)
        self.assertEqual(bst1.search(1), True)
        self.assertEqual(bst1.search(20), False)
        self.assertEqual(bst1.search(13), False)


if __name__ == "__main__":

    # Run the unit tests for the BinaryTree and BinarySearchTree classes.
    unittest.main()
