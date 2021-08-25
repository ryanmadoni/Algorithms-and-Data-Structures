"""
Author: Ryan Adoni
Date: 8/20/2021
Description: Practice with binary trees and binary search trees 
"""

from itertools import groupby, chain
from operator import itemgetter

class BinaryTree:
    """
    A class to represent a binary tree and functions that can be applied to them.
    """

    def __init__(self, data, l = None, r = None):
        """
        The constructor for the BinaryTree class that represents a binary tree.  By default the left and right
        subtree are None values, i.e., leaves.
        """
        self.data, self.l, self.r = data, l, r # initialize the variables for the data, the left subtree, and the right subtree

    def preOrder(self):
        """
        Takes self as input, then returns a list representing the preorder traversal of the nodes in the binary tree.
        """

        # Return the data of self plus the recursion on the left and right subtrees if they are not None, i.e., they are not leaves.
        return [self.data] + (self.l.preOrder() if self.l != None else []) + (self.r.preOrder() if self.r != None else []) 

    def inOrder(self):
        """
        Takes self as input, then returns a list representing the inorder traversal of the nodes in the binary tree.
        """

        # Return the recursion on the left subtree plus the data of self plus the recursion on the right 
        # subtree.  Recurse only if the left and right subtrees are not None, i.e., they are not leaves.
        return (self.l.inOrder() if self.l != None else []) + [self.data] + (self.r.inOrder() if self.r != None else []) 

    def postOrder(self):
        """
        Takes self as input, then returns a list representing the postorder traversal of nodes in the binary tree.
        """

        # Return the recursion on the left subtree plus the recursion on the right subtree plus the data of self.
        # Recurse only if the left and right subtrees are not None, i.e., they are not leaves.
        return (self.l.postOrder() if self.l != None else []) + (self.r.postOrder() if self.r != None else []) + [self.data]     

    def levelOrder(self):
        """
        Takes self as input, then returns a list representing the level order traversal of nodes in the binary tree.
        """
        def helper(binaryTree, level):
            """
            A helper function to help get the level order of self.  This function gets the preorder traversal of self,
            but each node's value is put into a two-tuple pair with its current level.
            """
            return [(level, binaryTree.data)] + (helper(binaryTree.l, level + 1) if binaryTree.l != None else []) + (helper(binaryTree.r, level + 1) if binaryTree.r != None else []) 

        # Use itertools.groupby to group the preorder traversal obtained from the helper to group each level,
        # then trim the level metadata and chain the final list of lists.  This is an extremely Pythonic way of
        # coding this function.  A preorder traversal is arbitrarily used here to simply traverse the binary tree,
        # but it could be any traversal: preorder, inorder, or postorder
        return list(chain.from_iterable([[pair[1] for pair in group] for _, group in groupby(sorted(helper(self, 0)), lambda p: p[0])]))

    def inverse(self):
        """
        Takes as input self, then returns the inverse or mirror of the binary tree, self
        """

        # Invert/Mirror each subtree recursively if the left and right subtrees are not None, i.e., they are not leaves.
        return BinaryTree(self.data, self.r.inverse() if self.r != None else None, self.l.inverse() if self.l != None else None)

    def numberOfNodes(self):
        """
        Takes as input self, then returns the number of nodes in the binary tree, self
        """

        # Check if the current node is a leaf, i.e., both its left and right branches are None
        if self.l == None and self.r == None:
            return 1 # Return 1 since a leaf has been found
        
        # Return the number of nodes on the left and right branches of self if they are not None 
        # and add 1 to count the current node
        return (self.l.numberOfNodes() if self.l != None else 0) + (self.r.numberOfNodes() if self.r != None else 0) + 1

    def numberOfLeaves(self):
        """
        Takes as input self, then returns the number of leaves in the binary tree, self
        """

        # Check if the current node is a leaf, i.e., both its left and right branches are None
        if self.l == None and self.r == None:
            return 1 # Return 1 since a leaf has been found

        # Return the number of leaves on the left and right branches of self if they are not None
        return (self.l.numberOfLeaves() if self.l != None else 0) + (self.r.numberOfLeaves() if self.r != None else 0)
    
    def numberOfInternalNodes(self):
        """
        Takes as input self, then returns the number of internal nodes in the binary tree, self.
        """

        # Returns the number of internal nodes, i.e., the number of total nodes minus the number of leaves.
        # This can also be done without these helper functions by mimicking the format of the two functions
        # numberOfNodes() and numberOfLeaves(), but returning 0 when the base case is reached, i.e., a leaf is 
        # reached.
        return self.numberOfNodes() - self.numberOfLeaves() 

    def paths(self):
        """
        Takes as input self, then returns a list of lists representing all possible simple paths from the root
        to every leaf in self.
        """

        def helper(binaryTree, path):
            """
            A helper to help find all the paths from the root to every leaf in binaryTree.
            """
        
            # Check if the current node is a leaf, i.e., both its left and right branches are None
            if binaryTree.l == None and binaryTree.r == None:
                return [path + [binaryTree.data]] # return the path since a leaf has been reached

            # Recurse to return the paths on the left and right subtrees of binaryTree
            return (helper(binaryTree.l, path + [binaryTree.data]) if binaryTree.l != None else []) + \
                   (helper(binaryTree.r, path + [binaryTree.data]) if binaryTree.r != None else [])
        
        return helper(self, []) # call the helper to execute the work and get all possible simple paths from the root to every leaf in self.

    def pathSum(self, n):
        """
        Takes as input self and an integer n, then returns a list representing the first simple path-if one exists 
        in self such that the path's sum is equal to n.  returns an empty list, [], if the sum cannot be made.
        """

        # try to execute the following line of code, which can raise a ValueError if n is not in the 
        # call to paths(), paths
        try: 

            # return paths indexed at the index of n if n is in the list where paths 
            # is mapped to the sum function.
            return (paths := self.paths())[list(map(sum, paths)).index(n)] 

        # catch the ValueError
        except ValueError:
            return [] # return [] since the call to index() returned a ValueError

    def contains(self, subtree):
        """
        Takes as input self and a BinaryTree, subtree, then returns a boolean value denoting if the subtree, 
        subtree, is contained in the binary tree, self.  Returns True if subtree is contained and False otherwise.
        """

        # Return whether the tree rooted as self is equal to subtree, then or that result with the recursion
        # of the left and right branches of self if they are not None.
        return self == subtree or \
               (self.l.contains(subtree) if self.l != None else False) or \
               (self.r.contains(subtree) if self.r != None else False)

    def height(self):
        """
        Takes as input self and returns the height, or maximum depth, of the binary tree, self.  Height can be
        defined as either the number of nodes or number of connections between nodes.  This function will measure
        height in nodes.
        """

        # Check if the current node is a leaf, i.e., both its left and right branches are None
        if self.l == None and self.r == None:
            return 1 # Return 1 since a leaf has been found

        # Return the max of the number of leaves on the left and right branches of self if they are not None, i.e.,
        # the height of the binary tree, self, then add one for the current node.
        return max(self.l.height() if self.l != None else 0, self.r.height() if self.r != None else 0) + 1

    def width(self, level):
        """
        Takes as input self and a non-negative integer, level, then returns the width of the level, level, in the
        binary tree, self.  The width of a level in a binary tree is the number of nodes in a certain level.
        """

        def helper(binaryTree, level):
            """
            A helper function to help get the width of a specific level of self.  This function gets the preorder
            traversal of self, but each node's value is put into a two-tuple pair with its current level.
            """
            return [(level, binaryTree.data)] + (helper(binaryTree.l, level + 1) if binaryTree.l != None else []) + (helper(binaryTree.r, level + 1) if binaryTree.r != None else []) 

        # Use itertools.groupby to group the preorder traversal obtained from the helper to group each level,
        # then get the length of the specific level if it exists.  This is an extremely Pythonic way of
        # coding this function.  A preorder traversal is arbitrarily used here to simply traverse the binary tree,
        # but it could be any traversal: preorder, inorder, or postorder
        return len(L[level]) if level < len((L := [list(group) for _, group in groupby(sorted(helper(self, 0)), lambda p: p[0])])) else 0

    def maxWidth(self):
        """
        Takes as input self, then returns the maximum width of the tree, self.
        """
        def helper(binaryTree, level):
            """
            A helper function to help get the max width of self.  This function gets the preorder
            traversal of self, but each node's value is put into a two-tuple pair with its current level.
            """
            return [(level, binaryTree.data)] + (helper(binaryTree.l, level + 1) if binaryTree.l != None else []) + (helper(binaryTree.r, level + 1) if binaryTree.r != None else []) 

        # Use itertools.groupby to group the preorder traversal obtained from the helper to group each level,
        # then get the max width of the binary tree, self.  This is an extremely Pythonic way of
        # coding this function.  A preorder traversal is arbitrarily used here to simply traverse the binary tree,
        # but it could be any traversal: preorder, inorder, or postorder
        return max([len(list(group)) for _, group in groupby(sorted(helper(self, 0)), lambda p: p[0])])

    def diameter(self):
        """
        Takes as input self, then returns the diameter of the binary tree, self.  The diameter of a binary tree is
        defined as the number of nodes on the longest path between any two leaves in the binary tree.
        """
        return self.l.height() + 1 + self.r.height() # Return the height of the left and right subtrees plus 1 for the current node.

    def isLeftSkewed(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is left skewed.  
        Returns True if the binary tree, self, is left skewed and False otherwise.  A binary tree is left skewed
        if every node has exactly one child and every node does not have right children.
        """
        
        # Check if the current node is a leaf, i.e., both its left and right branches are None.
        if self.l == None and self.r == None:
            return True # Return True since a leaf has been reached. 

        return False if self.r != None else self.l.isLeftSkewed() # Return whether a left subtree of self is left skewed and self has no right children. 

    def isRightSkewed(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is right skewed.  
        Returns True if the binary tree, self, is right skewed and False otherwise.  A binary tree is right skewed
        if every node has exactly one child and every node does not have left children.
        """
        
        # Check if the current node is a leaf, i.e., both its left and right branches are None.
        if self.l == None and self.r == None:
            return True # Return True since a leaf has been reached. 

        return False if self.l != None else self.r.isRightSkewed() # Return whether a right subtree of self is right skewed and self has no left children. 

    def isDegenerate(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is degenerate.  
        Returns True if the binary tree, self, is degenerate (a.k.a. pathological) and False otherwise.  
        A binary tree is degenerate or pathological if every node has exactly one child, i.e., the binary tree
        degenerates to a linked list.
        """
        
        # Check if the current node is a leaf, i.e., both its left and right branches are None.
        if self.l == None and self.r == None:
            return True # Return True since a leaf has been reached.

        # Check if the binary tree, self, only has one child, a left child.
        if self.l != None and self.r == None:
            return self.l.isDegenerate() # Recurse down the left branch of the binary tree, self.

        # Check if the binary tree, self, only has one child, a right child.
        if self.l == None and self.r != None:
            return self.r.isDegenerate() # Recurse down the right branch of the binary tree, self.

        return False # Return False because the binarr tree, self, has two children.

    def isBalanced(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is balanced.
        Returns True if the binary tree, self, is balanced and False otherwise.  A balanced binary tree is
        a binary tree in which the heights of every left and right subtree can differ by at most 1.
        """

        # Return whether the absolute difference of the binary tree's left and right subtrees' heights is less 
        # than one and whether the left and right subtrees of the binary tree, self, are balanced if they exist.
        return abs((self.l.height() if self.l != None else 0) - (self.r.height() if self.r != None else 0)) <= 1 and \
               (self.l.isBalanced() if self.l != None else True) and \
               (self.r.isBalanced() if self.r != None else True)

    def isFull(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is full.
        Returns True if the binary tree, self, is full and False otherwise.  A full binary tree is a 
        binary tree if every node has 0 or 2 children.
        """

        # Check if the current node is a leaf, i.e., both its left and right branches are None.
        if self.l == None and self.r == None:
            return True # Return True since a leaf has been reached.
        
        # Check if the current node has two children, i.e., both its left and right branches are not None.
        if self.l != None and self.r != None:
            return self.l.isFull() and self.r.isFull() # Return the recursion of the left and right subtrees.

        return False # return False since the binary tree, self, has one child.

    def level(self, level):
        """
        Takes as input self and a non-negative integer, then returns a list representing the corresponding level
        in self.
        """
        def helper(binaryTree, level):
            """
            A helper function to help get the level of self.  This function gets the preorder
            traversal of self, but each node's value is put into a two-tuple pair with its current level.
            """
            return [(level, binaryTree.data)] + (helper(binaryTree.l, level + 1) if binaryTree.l != None else [(level + 1, None)]) + (helper(binaryTree.r, level + 1) if binaryTree.r != None else [(level + 1, None)]) 

        # Use itertools.groupby to group the preorder traversal obtained from the helper to group each level,
        # then get the level desired if that level exists.  This is an extremely Pythonic way of
        # coding this function.  A preorder traversal is arbitrarily used here to simply traverse the binary tree,
        # but it could be any traversal: preorder, inorder, or postorder
        return [[pair[1] for pair in list(group)] for _, group in groupby(sorted(helper(self, 0), key = itemgetter(0)), lambda p: p[0])][level] if level < self.height() else []

    def isComplete(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is complete.
        Returns True if the binary tree, self, is complete and False otherwise.  A complete binary tree is
        a binary tree in which all levels are completely filled except possibly the last level and the last 
        level has all keys as left as possible.
        """
        level, complete = 0, True # Instantiate two variables: one to keep track of the current level and a boolean keeping track if the binary tree is complete.

        # Loop until the call to level yields an empty list, [].
        while (values := self.level(level)) != []:

            # Check if None is in values.
            if None in values:
                found = False # Instantiate a boolean to see if a None has been found in the list, values.

                # Loop for each value in values.
                for value in values:

                    # Check if a None has been found.
                    if value == None:
                        found = True # set the boolean, found, to True.

                    # Check to see if a None has been found and a non None value is after it, i.e., the binary tree is incomplete.
                    if found and value != None:
                        complete = False # Set complete to False.
        
            level += 1 # increment the level.

        return complete # Return a boolean denoting whether the binary tree, self is complete.

    def isPerfect(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is perfect.
        Returns True if the binary tree, self, is perfect and False otherwise.  A perfect binary tree is 
        a binary tree in which all internal nodes have two children and all leaves are at same level.
        """
        return self.numberOfNodes() == 2 ** self.height() - 1 # Check if the number of nodes equals 2 ^ (height) - 1, i.e., the binary tree, self, is perfect.

    def isBinarySearchTree(self):
        """
        Takes as input self, then returns a boolean value denoting if the binary tree, self, is a binary 
        search tree.  Returns True if the binary tree, self, is a binary search tree and False otherwise.
        A binary search tree is a binary tree that fulfills the following invariant: every left nodes' value
        and its childrens' values are less than its parent's value and every right nodes' value and its 
        childrens' values are greater than its parent's value.
        """

        # Check if the binary search tree invariant is upheld and recurse to see if the children of self are 
        # also binary search trees.
        return (all([node < self.data for node in self.l.preOrder()]) if self.l != None else True) and \
               (all([self.data < node for node in self.r.preOrder()]) if self.r != None else True) and \
               (self.l.isBinarySearchTree() if self.l != None else True) and \
               (self.r.isBinarySearchTree() if self.r != None else True)

    def binaryTreeString(self, level = 0):
        """
        A function that takes as input a default value, level, that is used to space the string representation
        of the binary tree stored in self.  the variable level should not be used by the used by the caller and
        should be  left at its default value.
        """

        # Print the data stored in self, then initialize a variable, spacing, to hold the whitespace needed 
        # to format the string, then recurse to print the left and right binary subtrees.
        return str(self.data) + (spacing := "\n" + (level + 1) * "  ") + (self.l.binaryTreeString(level + 1) if self.l != None else "None") + spacing + (self.r.binaryTreeString(level + 1) if self.r != None else "None")

    def __eq__(self, obj):
        """
        An overriden version of the object's equal method.  This function returns True if self and obj represent
        the same binary tree and return False otherwise.
        """

        # Check if obj is a BinaryTree and if they have the same preorder traversal, i.e., 
        # they represent the same binary tree.   A preorder traversal is arbitrarily used
        # here, but it could be any traversal: preorder, inorder, or postorder
        return isinstance(obj, BinaryTree) and self.preOrder() == obj.preOrder() 

if __name__ == "__main__":

    binaryTree1 = BinaryTree(3, BinaryTree(2, BinaryTree(1)), BinaryTree(4, BinaryTree(2), None)) # define a binary tree, binaryTree1 to test the functions above
    binaryTree2 = BinaryTree(3, BinaryTree(2, BinaryTree(1)), BinaryTree(4, BinaryTree(2), None)) # define a binary tree, binaryTree2, to test the functions above
    binaryTree3 = BinaryTree(1, BinaryTree(2, None, BinaryTree(3, BinaryTree(4, BinaryTree(5), None))), None) # define a binary tree, binaryTree3, to test the functions above
    binaryTree4 = BinaryTree(1, BinaryTree(2), BinaryTree(3, BinaryTree(4), BinaryTree(4))) # define a binary tree, binaryTree4, to test the functions above
    binaryTree5 = BinaryTree(1, BinaryTree(2, BinaryTree(3,  BinaryTree(8), BinaryTree(9)), BinaryTree(4, BinaryTree(10), None)), BinaryTree(5, BinaryTree(6), BinaryTree(7))) # define a binary tree, binaryTree5, to test the functions above
    binaryTree6 = BinaryTree(7, BinaryTree(3, BinaryTree(1), BinaryTree(5)), BinaryTree(10, BinaryTree(8))) # define a binary tree, binaryTree6, to test the functions above

    # print(binaryTree1.binaryTreeString()) # print the binary tree, binaryTree1
    # print(binaryTree1.preOrder()) # print the preorder traversal of the binary tree, binaryTree1
    # print(binaryTree1.inOrder()) # print the inorder traversal of the binary tree, binaryTree1
    # print(binaryTree1.postOrder()) # print the postorder traversal of the binary tree, binaryTree1
    # print(binaryTree1.levelOrder()) # print the level order traversal of the binary tree, binaryTree1
    # print(binaryTree1.inverse().binaryTreeString()) # print the inverse/mirror of the binary tree, binaryTree1
    # print(binaryTree1 == binaryTree2) # print if binaryTree1 and binaryTree2 are equal
    # print(binaryTree1.numberOfLeaves()) # print the number of leaves in binaryTree1
    # print(binaryTree1.numberOfNodes()) # print the number of nodes in binaryTree1
    # print(binaryTree1.numberOfInternalNodes()) # print the number of internal nodes in binaryTree1
    # print(binaryTree1.paths()) # print the paths of the binary tree, binaryTree1
    # print(binaryTree1.pathSum(6)) # print the first path that has the sum 6 in the binary tree, binaryTree1 
    # print(binaryTree1.height()) # print the height of the binary tree, binaryTree1
    # print(binaryTree1.contains(BinaryTree(2, BinaryTree(1)))) # print whether binaryTree1 contains a specific subtree
    # print(binaryTree1.width(1)) # get the width of binaryTree1's 1st level
    # print(binaryTree1.maxWidth()) # print the max width of the binary tree, binaryTree1
    # print(binaryTree1.diameter()) # print the diameter of the binary tree, binaryTree1
    # print(binaryTree1.isBalanced()) # print a boolean denoting if the binary tree, binaryTree1 is balanced
    # print(binaryTree1.isPerfect()) # print a boolean denoting if the binary tree, binaryTree1 is perfect

    # print(binaryTree3.binaryTreeString()) # print the binary tree, binaryTree3
    # print(binaryTree3.isDegenerate()) # print a boolean denoting if the binary tree, binaryTree3 is degenerate
    # print(binaryTree3.isBalanced()) # print a boolean denoting if the binary tree, binaryTree3 is balanced

    # print(binaryTree4.binaryTreeString()) # print the binary tree, binaryTree4
    # print(binaryTree4.isFull()) # print a boolean denoting if the binary tree, binaryTree4 is full

    # print(binaryTree5.binaryTreeString()) # print the binary tree, binaryTree5
    # print(binaryTree5.level(2)) # print level 2 of the binary tree, binaryTree5
    # print(binaryTree5.isComplete()) # print a boolean denoting if the binary tree, binaryTree4, is complete

    # print(binaryTree6.isBinarySearchTree()) # print a boolean denoting if the binary tree, binaryTree6 is a binary search tree