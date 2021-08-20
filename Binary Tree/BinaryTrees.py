from itertools import groupby, chain

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
        return list(chain.from_iterable([[pair[1] for pair in group] for _, group in groupby(sorted(helper(self, 0)))]))

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
        Takes as input self, then returns the number of internal nodes in the binary tree, self
        """

        # Returns the number of internal nodes, i.e., the number of total nodes minus the number of leaves.
        # This can also be done without these helper functions by mimicking the format of the two functions
        # numberOfNodes() and numberOfLeaves(), but returning 0 when the base case is reached, i.e., a leaf is 
        # reached.
        return self.numberOfNodes() - self.numberOfLeaves() 

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

    binaryTree1 = BinaryTree(3, BinaryTree(2, BinaryTree(1)), BinaryTree(4)) # define a binary tree, binaryTree1 to test the functions above
    binaryTree2 = BinaryTree(3, BinaryTree(2, BinaryTree(1)), BinaryTree(4, BinaryTree(2), None)) # define a binary tree, binaryTree2, to test the functions above

    print(binaryTree1.binaryTreeString()) # print the binary tree, binaryTree1
    # print(binaryTree1.preOrder()) # print the preorder traversal of the binary tree, binaryTree1
    # print(binaryTree1.inOrder()) # print the inorder traversal of the binary tree, binaryTree1
    # print(binaryTree1.postOrder()) # print the postorder traversal of the binary tree, binaryTree1
    # print(binaryTree1.levelOrder()) # print the level order traversal of the binary tree, binaryTree1
    # print(binaryTree1.inverse().binaryTreeString()) # print the inverse/mirror of the binary tree, binaryTree1
    # print(binaryTree1 == binaryTree2) # print if binaryTree1 and binaryTree2 are equal
    # print(binaryTree1.numberOfLeaves()) # print the number of leaves in binaryTree1
    # print(binaryTree1.numberOfNodes()) # print the number of nodes in binaryTree1
    # print(binaryTree1.numberOfInternalNodes()) # print the number of internal nodes in binaryTree1

    