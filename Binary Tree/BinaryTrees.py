
class BinaryTree:
    """
    A class to represent a binary tree and functions that can be applied on them
    """

    def __init__(self, data, l = None, r = None):
        """
        The constructor for the BinaryTree class that represents a binary tree.  By default the left and right
        subtree are None values, i.e., leaves
        """
        self.data, self.l, self.r = data, l, r # initialize the variables for the data, the left subtree, and the right subtree

    def preorder(self):
        """
        Takes self as input, then returns a list representing the preorder traversal of the nodes in the binary tree
        """

        # Return the data of self plus the recursion on the left and right subtrees if they are not None, i.e., they are not leaves.
        return [self.data] + (self.l.preorder() if self.l != None else []) + (self.r.preorder() if self.r != None else []) 

    def inorder(self):
        """
        Takes self as input, then returns a list representing the inorder traversal of the nodes in the binary tree
        """

        # Return the recursion on the left subtree plus the data of self plus the recursion on the right 
        # subtree.  Recurse only if the left and right subtrees are not None, i.e., they are not leaves.
        return (self.l.inorder() if self.l != None else []) + [self.data] + (self.r.inorder() if self.r != None else []) 

    def postorder(self):
        """
        Takes self as input, then returns a list representing the postorder traversal of nodes in the binary tree
        """

        # Return the recursion on the left subtree plus the recursion on the right subtree plus the data of self.
        # Recurse only if the left and right subtrees are not None, i.e., they are not leaves.
        return (self.l.postorder() if self.l != None else []) + (self.r.postorder() if self.r != None else []) + [self.data]     

    def binaryTreeString(self, level = 0):
        """
        A function that takes as input a default value, level, that is used to space the string representation
        of the binary tree stored in self.  the variable level should not be used by the used by the caller and
        should be  left at its default value.
        """

        # Print the data stored in self, then initialize a variable, spacing, to hold the whitespace needed 
        # to format the string, then recurse to print the left and right binary subtrees.
        return str(self.data) + (spacing := "\n" + (level + 1) * "  ") + (self.l.binaryTreeString(level + 1) if self.l != None else "None") + spacing + (self.r.binaryTreeString(level + 1) if self.r != None else "None")

if __name__ == "__main__":

    binaryTree = BinaryTree(3, BinaryTree(2, BinaryTree(1)), BinaryTree(4)) # define a binary tree, binaryTree to test the functions above

    print(binaryTree.binaryTreeString()) # print the binary tree, binaryTree
    # print(binaryTree.preorder()) # print the preorder traversal of the binary tree, binaryTree
    # print(binaryTree.inorder()) # print the inorder traversal of the binary tree, binaryTree
    # print(binaryTree.postorder()) # print the postorder traversal of the binary tree, binaryTree
    