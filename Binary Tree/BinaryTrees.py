"""
Author: Ryan Adoni
Date: 8/29/2021
Description: Practice with binary trees and binary search trees 
"""

from itertools import groupby, chain
from operator import itemgetter
import unittest

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
        return list(chain.from_iterable([[pair[1] for pair in group] for _, group in groupby(sorted(helper(self, 0), key = itemgetter(0)), lambda p: p[0])]))

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
        return (self.l.height() if self.l != None else 0) + 1 + (self.r.height() if self.r != None else 0) # Return the height of the left and right subtrees plus 1 for the current node if it is not None.

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
        super().__init__(data) # Call to super, i.e., parent's constructor, to initialize the root node to data.

    def insert(self, data):
        """
        Takes as input self and an integer, data, then adds data to the binary search tree, self, maintaining the 
        binary search tree invariant; if the value data is not already inside the binary search tree, self, then it
        is added and True is returned; if the value is already inside the binary search tree, no value is added and
        False is returned.
        """
        
        # Check if the data is less than self's data.
        if data < self.data:
            
            # Check if the left subtree of self is empty.
            if self.l == None:
                self.l = BinarySearchTree(data) # add a new subtree with the value data.
                return True # return True since the value was added succesfully.

            return self.l.insert(data) # Recurse down the left branch of the tree to add data to the binary search tree, self.

        # Check if the data is greater than self's data.
        if self.data < data:
            
            # Check if the rigth subtree of self is empty.
            if self.r == None:
                self.r = BinarySearchTree(data) # add a new subtree with the value data.
                return True # return True since the value was added succesfully.
                
            return self.r.insert(data) # Recurse down the right branch of the tree to add data to the binary search tree, self.

        return False # return False since data and self's data are equal.

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

            # Check if the data of self is the data that needs to be deleted.
            if self.data == data:
                
                # Check if self has two children
                if self.l != None and self.r != None:
                    self.data = min(self.r.preOrder()) # Set self's data to the smallest value in the right subtree of self (alternatively, this could have been the largest value in the left subtree).
                    return helper(self.r, self.data, self, False) # Recurse to delete self.data in the right subtree to remove the duplicate value.

                # Check if self is a leaf.
                if self.l == None and self.r == None:
                    if left: parent.l = None # set the left child of parent to None if left is True.
                    else: parent.r = None # set the right child of parent to None if left is False.

                # Check if self has no right child and a has a left child.
                elif self.l != None and self.r == None:
                    if left: parent.l = self.l # set the left child of parent to the left child of self if left is True.
                    else: parent.r = self.l # set the right child of parent to the left child of self if left is False.
                
                # Else, self has no left child and a has a right child.
                else:
                    if left: parent.l = self.r # set the left child of parent to the right child of self if left is True.
                    else: parent.r = self.r # set the right child of parent to the right child of self if left is False.

                return True # Return True since a value has been deleted successfully.
            
            # Check if data is in the left subtree of self.
            elif self.l != None and self.l.search(data):
                return helper(self.l, data, self, True) # Recurse using the helper into the left subtree.

            # Check if data is in the right subtree of self.
            elif self.r != None and self.r.search(data):
                return helper(self.r, data, self, False) # Recurse using the helper into the right subtree.
            
            return False # Return False since data is not conatained in self.

        return helper(self, data, None, None) # Call the helper function to execute the work and return its result.

    def search(self, data):
        """
        Takes as input self and an integer, data, then returns True if data is contained within the Binary Search
        Tree, self; returns False otherwise.
        """

        # Check if self.data is equal to data, then recurse down the left and right subtrees if they are non None.
        return self.data == data or \
               (self.l.search(data) if self.l != None else False) or \
               (self.r.search(data) if self.r != None else False)

    def inverse(self):
        """
        Override the inverse function since inverse cannot be applied to a binary search tree without breaking
        the binary search tree invariant.
        """
        pass # Pass to remove functionality from the parent class, BinaryTree.

class TestBinaryTreeMethods(unittest.TestCase):
    """
    A class extending the unittest.TestCase class used to test the binary tree and binary search tree classes and 
    their component functions above.
    """

    @classmethod
    def setUpClass(self):
        """
        The setUpClass function that will instantiate a few binary trees and binary search trees to work with 
        for the testing of the functions.
        """
        self.binaryTree1 = BinaryTree(3, BinaryTree(2, BinaryTree(1)), BinaryTree(4, BinaryTree(2), None)) # define a binary tree, binaryTree1 to test the binary tree functions.
        self.binaryTree2 = BinaryTree(1, BinaryTree(2, BinaryTree(5), BinaryTree(9)), BinaryTree(3, BinaryTree(2, BinaryTree(2), None), None)) # define a binary tree, binaryTree2 to test the binary tree functions.
        self.binaryTree3 = BinaryTree(1, BinaryTree(2, None, BinaryTree(3, BinaryTree(4, BinaryTree(5), None))), None) # define a binary tree, binaryTree3, to test the functions above.
        self.binaryTree4 = BinaryTree(1, BinaryTree(2), BinaryTree(3, BinaryTree(4), BinaryTree(4))) # define a binary tree, binaryTree4, to test the functions above.
        self.binaryTree5 = BinaryTree(1, BinaryTree(2, BinaryTree(3,  BinaryTree(8), BinaryTree(9)), BinaryTree(4, BinaryTree(10), None)), BinaryTree(5, BinaryTree(6), BinaryTree(7))) # define a binary tree, binaryTree5, to test the functions above.
        self.binaryTree6 = BinaryTree(7, BinaryTree(3, BinaryTree(1), BinaryTree(5)), BinaryTree(10, BinaryTree(8))) # define a binary tree, binaryTree6, to test the functions above.
        self.binaryTree7 = BinaryTree(7, BinaryTree(3, BinaryTree(1), BinaryTree(5)), BinaryTree(10, BinaryTree(8))) # define a binary tree, binaryTree7, to test the functions above.
        self.binaryTree8 = BinaryTree(17, BinaryTree(8, BinaryTree(3), BinaryTree(14)), BinaryTree(25, BinaryTree(20), BinaryTree(30))) # define a binary tree, binaryTree8, to test the functions above.

    def testBinaryTreeString(self):
        """
        A function to test the functionality of the class BinaryTree's binaryTreeString()'s function.
        """
        binaryTreeString1 = "3\n  2\n    1\n      None\n      None\n    None\n  4\n    2\n      None\n      None\n    None" # The expected output of binaryTree1's call to binaryTreeString().
        binaryTreeString2 = "1\n  2\n    5\n      None\n      None\n    9\n      None\n      None\n  3\n    2\n      2\n        None\n        None\n      None\n    None" # The expected output of binaryTree2's call to binaryTreeString().

        self.assertEqual(self.binaryTree1.binaryTreeString(), binaryTreeString1) # Check if binaryTree1's call to the binaryTreeString() function yields the correct output.
        self.assertEqual(self.binaryTree2.binaryTreeString(), binaryTreeString2) # Check if binaryTree2's call to the binaryTreeString() function yields the correct output.

    def testPreOrder(self):
        """
        A function to test the functionality of the class BinaryTree's preOrder()'s function.
        """
        preOrder1, preOrder2 = [3, 2, 1, 4, 2], [1, 2, 5, 9, 3, 2, 2] # The expected output of binaryTree1's and binaryTree2's calls to preOrder().

        self.assertEqual(self.binaryTree1.preOrder(), preOrder1) # Check if binaryTree1's call to the preOrder() function yields the correct output.
        self.assertEqual(self.binaryTree2.preOrder(), preOrder2) # Check if binaryTree2's call to the preOrder() function yields the correct output.

    def testInOrder(self):
        """
        A function to test the functionality of the class BinaryTree's inOrder()'s function.
        """
        inOrder1, inOrder2 = [1, 2, 3, 2, 4], [5, 2, 9, 1, 2, 2, 3] # The expected output of binaryTree1's and binaryTree2's calls to inOrder().

        self.assertEqual(self.binaryTree1.inOrder(), inOrder1) # Check if binaryTree1's call to the inOrder() function yields the correct output.
        self.assertEqual(self.binaryTree2.inOrder(), inOrder2) # Check if binaryTree2's call to the inOrder() function yields the correct output.

    def testPostOrder(self):
        """
        A function to test the functionality of the class BinaryTree's postOrder()'s function.
        """
        postOrder1, postOrder2 = [1, 2, 2, 4, 3], [5, 9, 2, 2, 2, 3, 1] # The expected output of binaryTree1's and binaryTree2's calls to postOrder().

        self.assertEqual(self.binaryTree1.postOrder(), postOrder1) # Check if binaryTree1's call to the postOrder() function yields the correct output.
        self.assertEqual(self.binaryTree2.postOrder(), postOrder2) # Check if binaryTree2's call to the postOrder() function yields the correct output.

    def testLevelOrder(self):
        """
        A function to test the functionality of the class BinaryTree's levelOrder()'s function.
        """
        levelOrder1, levelOrder2 = [3, 2, 4, 1, 2], [1, 2, 3, 5, 9, 2, 2] # The expected output of binaryTree1's and binaryTree2's calls to levelOrder().

        self.assertEqual(self.binaryTree1.levelOrder(), levelOrder1) # Check if binaryTree1's call to the levelOrder() function yields the correct output.
        self.assertEqual(self.binaryTree2.levelOrder(), levelOrder2) # Check if binaryTree2's call to the levelOrder() function yields the correct output.

    def testInverse(self):
        """
        A function to test the functionality of the class BinaryTree's inverse()'s function.
        """
        inverseBinaryTreeString1 = "3\n  4\n    None\n    2\n      None\n      None\n  2\n    None\n    1\n      None\n      None" # The expected output of binaryTree1's call to inverse() and then binaryTreeString().
        inverseBinaryTreeString2 = "1\n  3\n    None\n    2\n      None\n      2\n        None\n        None\n  2\n    9\n      None\n      None\n    5\n      None\n      None" # The expected output of binaryTree2's call to inverse() and then binaryTreeString().

        self.assertEqual(self.binaryTree1.inverse().binaryTreeString(), inverseBinaryTreeString1) # Check if binaryTree1's call to the inverse() function yields the correct output.
        self.assertEqual(self.binaryTree2.inverse().binaryTreeString(), inverseBinaryTreeString2) # Check if binaryTree2's call to the inverse() function yields the correct output.

    def testEqual(self):
        """
        A function to test the functionality of the class BinaryTree's overridden equal()'s function.
        """
        self.assertNotEqual(self.binaryTree5, self.binaryTree6) # Check if binaryTree5 and binaryTree6 are not equal.
        self.assertEqual(self.binaryTree6, self.binaryTree7) # Check if binaryTree6 and binaryTree7 are equal.

    def testNumberOfLeaves(self):
        """
        A function to test the functionality of the class BinaryTree's numberOfLeaves()'s function.
        """
        self.assertEqual(self.binaryTree1.numberOfLeaves(), 2) # Check if binaryTree1's call to the numberOfLeaves() function yields the correct output.
        self.assertEqual(self.binaryTree2.numberOfLeaves(), 3) # Check if binaryTree2's call to the numberOfLeaves() function yields the correct output.
        self.assertEqual(self.binaryTree3.numberOfLeaves(), 1) # Check if binaryTree3's call to the numberOfLeaves() function yields the correct output.
        self.assertEqual(self.binaryTree4.numberOfLeaves(), 3) # Check if binaryTree4's call to the numberOfLeaves() function yields the correct output.

    def testNumberOfNodes(self):
        """
        A function to test the functionality of the class BinaryTree's numberOfNodes()'s function.
        """
        self.assertEqual(self.binaryTree1.numberOfNodes(), 5) # Check if binaryTree1's call to the numberOfNodes() function yields the correct output.
        self.assertEqual(self.binaryTree2.numberOfNodes(), 7) # Check if binaryTree2's call to the numberOfNodes() function yields the correct output.
        self.assertEqual(self.binaryTree3.numberOfNodes(), 5) # Check if binaryTree3's call to the numberOfNodes() function yields the correct output.
        self.assertEqual(self.binaryTree4.numberOfNodes(), 5) # Check if binaryTree4's call to the numberOfNodes() function yields the correct output.

    def testNumberOfInternalNodes(self):
        """
        A function to test the functionality of the class BinaryTree's numberOfInternalNodes()'s function.
        """
        self.assertEqual(self.binaryTree1.numberOfInternalNodes(), 3) # Check if binaryTree1's call to the numberOfInternalNodes() function yields the correct output.
        self.assertEqual(self.binaryTree2.numberOfInternalNodes(), 4) # Check if binaryTree2's call to the numberOfInternalNodes() function yields the correct output.
        self.assertEqual(self.binaryTree3.numberOfInternalNodes(), 4) # Check if binaryTree3's call to the numberOfInternalNodes() function yields the correct output.
        self.assertEqual(self.binaryTree4.numberOfInternalNodes(), 2) # Check if binaryTree4's call to the numberOfInternalNodes() function yields the correct output.

    def testPaths(self):
        """
        A function to test the functionality of the class BinaryTree's paths()'s function.
        """
        self.assertEqual(self.binaryTree1.paths(), [[3, 2, 1], [3, 4, 2]]) # Check if binaryTree1's call to the paths() function yields the correct output.
        self.assertEqual(self.binaryTree2.paths(), [[1, 2, 5], [1, 2, 9], [1, 3, 2, 2]]) # Check if binaryTree2's call to the paths() function yields the correct output.
        self.assertEqual(self.binaryTree3.paths(), [[1, 2, 3, 4, 5]]) # Check if binaryTree3's call to the paths() function yields the correct output.
        self.assertEqual(self.binaryTree8.paths(), [[17, 8, 3], [17, 8, 14], [17, 25, 20], [17, 25, 30]]) # Check if binaryTree8's call to the paths() function yields the correct output.

    def testPathSum(self):
        """
        A function to test the functionality of the class BinaryTree's pathSum()'s function.
        """
        self.assertEqual(self.binaryTree1.pathSum(6), [3, 2, 1]) # Check if binaryTree1's call to the pathSum(5) function yields the correct output.
        self.assertEqual(self.binaryTree2.pathSum(8), [1, 2, 5]) # Check if binaryTree2's call to the pathSum(8) function yields the correct output.
        self.assertEqual(self.binaryTree3.pathSum(2), []) # Check if binaryTree3's call to the pathSum(2) function yields the correct output.
        self.assertEqual(self.binaryTree8.pathSum(39), [17, 8, 14]) # Check if binaryTree8's call to the pathSum(39) function yields the correct output.
        self.assertEqual(self.binaryTree8.pathSum(40), []) # Check if binaryTree8's call to the pathSum(40) function yields the correct output.

    def testHeight(self):
        """
        A function to test the functionality of the class BinaryTree's height()'s function.
        """
        self.assertEqual(self.binaryTree1.height(), 3) # Check if binaryTree1's call to the height() function yields the correct output.
        self.assertEqual(self.binaryTree2.height(), 4) # Check if binaryTree2's call to the height() function yields the correct output.
        self.assertEqual(self.binaryTree3.height(), 5) # Check if binaryTree3's call to the height() function yields the correct output.
        self.assertEqual(self.binaryTree4.height(), 3) # Check if binaryTree4's call to the height() function yields the correct output.

    def testWidth(self):
        """
        A function to test the functionality of the class BinaryTree's width()'s function.
        """
        self.assertEqual(self.binaryTree1.width(1), 2) # Check if binaryTree1's call to the width() function yields the correct output.
        self.assertEqual(self.binaryTree2.width(2), 3) # Check if binaryTree2's call to the width() function yields the correct output.
        self.assertEqual(self.binaryTree3.width(2), 1) # Check if binaryTree3's call to the width() function yields the correct output.
        self.assertEqual(self.binaryTree4.width(0), 1) # Check if binaryTree4's call to the width() function yields the correct output.

    def testMaxWidth(self):
        """
        A function to test the functionality of the class BinaryTree's maxWidth()'s function.
        """
        self.assertEqual(self.binaryTree1.maxWidth(), 2) # Check if binaryTree1's call to the maxWidth() function yields the correct output.
        self.assertEqual(self.binaryTree2.maxWidth(), 3) # Check if binaryTree2's call to the maxWidth() function yields the correct output.
        self.assertEqual(self.binaryTree3.maxWidth(), 1) # Check if binaryTree3's call to the maxWidth() function yields the correct output.
        self.assertEqual(self.binaryTree4.maxWidth(), 2) # Check if binaryTree4's call to the maxWidth() function yields the correct output.

    def testDiameter(self):
        """
        A function to test the functionality of the class BinaryTree's diameter()'s function.
        """
        self.assertEqual(self.binaryTree1.diameter(), 5) # Check if binaryTree1's call to the diameter() function yields the correct output.
        self.assertEqual(self.binaryTree2.diameter(), 6) # Check if binaryTree2's call to the diameter() function yields the correct output.
        self.assertEqual(self.binaryTree3.diameter(), 5) # Check if binaryTree3's call to the diameter() function yields the correct output.
        self.assertEqual(self.binaryTree4.diameter(), 4) # Check if binaryTree4's call to the diameter() function yields the correct output.

if __name__ == "__main__":
    unittest.main() # Run the unit tests to test the BinaryTree and BinarySearchTree classes.

    binaryTree1 = BinaryTree(3, BinaryTree(2, BinaryTree(1)), BinaryTree(4, BinaryTree(2), None)) # define a binary tree, binaryTree1 to test the binary tree functions.
    binaryTree2 = BinaryTree(1, BinaryTree(2, BinaryTree(5), BinaryTree(9)), BinaryTree(3, BinaryTree(2, BinaryTree(2), None), None)) # define a binary tree, binaryTree2 to test the binary tree functions.
    binaryTree3 = BinaryTree(1, BinaryTree(2, None, BinaryTree(3, BinaryTree(4, BinaryTree(5), None))), None) # define a binary tree, binaryTree3, to test the functions above.
    binaryTree8 = BinaryTree(17, BinaryTree(8, BinaryTree(3), BinaryTree(14)), BinaryTree(25, BinaryTree(20), BinaryTree(30)))

    # vvv Sloppy Testing (To be removed) vvv
 
    # print(binaryTree1.contains(BinaryTree(2, BinaryTree(1)))) # print whether binaryTree1 contains a specific subtree
    # print(binaryTree1.isBalanced()) # print a boolean denoting if the binary tree, binaryTree1 is balanced
    # print(binaryTree1.isPerfect()) # print a boolean denoting if the binary tree, binaryTree1 is perfect

    # print(binaryTree3.isDegenerate()) # print a boolean denoting if the binary tree, binaryTree3 is degenerate
    # print(binaryTree3.isBalanced()) # print a boolean denoting if the binary tree, binaryTree3 is balanced

    # print(binaryTree4.isFull()) # print a boolean denoting if the binary tree, binaryTree4 is full

    # print(binaryTree5.level(2)) # print level 2 of the binary tree, binaryTree5
    # print(binaryTree5.isComplete()) # print a boolean denoting if the binary tree, binaryTree4, is complete

    # print(binaryTree6.isBinarySearchTree()) # print a boolean denoting if the binary tree, binaryTree6 is a binary search tree

    