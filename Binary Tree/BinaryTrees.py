
class BinaryTree:
    """
    """

    def __init__(self, data, l = None, r = None):
        """
        """
        self.data, self.l, self.r = data, l, r

    def preorder():
        """
        """

    def BinaryTreeString(self, level = 0):
        """
        """
        return str(self.data) + (spacing := "\n" + (level + 1) * "  ") + (self.l.BinaryTreeString(level + 1) if self.l != None else "None") + spacing + (self.r.BinaryTreeString(level + 1) if self.r != None else "None")

if __name__ == "__main__":

    binaryTree = BinaryTree(1, BinaryTree(2, BinaryTree(4)), BinaryTree(3))

    print(binaryTree.BinaryTreeString())
    