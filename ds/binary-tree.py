# author: ShotgunThinker

# Binary Tree
class BinaryTree:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild: BinaryTree = lchild
        self.rchild: BinaryTree = rchild

    def isLeafNode(self) -> bool:
        return self.lchild is None and self.rchild is None

    def getDepth(self):
        """
        Get depth of tree.
        :return: depth of tree.
        """
        if self.isLeafNode():
            return 1

        left_depth = 0 if self.lchild is None else self.lchild.getDepth() + 1
        right_depth = 0 if self.rchild is None else self.rchild.getDepth() + 1
        return max(left_depth, right_depth)

    def preorderTraversal(self, func):
        """
        Preorder traversal. (DLR)
        :param func: mapping function
        """
        func(self.data)
        if self.lchild is not None:
            self.lchild.preorderTraversal(func)
        if self.rchild is not None:
            self.rchild.preorderTraversal(func)

    def inorderTraversal(self, func):
        """
        Inorder traversal. (LDR)
        :param func: mapping function
        """
        if self.lchild is not None:
            self.lchild.preorderTraversal(func)
        func(self.data)
        if self.rchild is not None:
            self.rchild.preorderTraversal(func)

    def postorderTraversal(self, func):
        """
        Postorder traversal. (LRD)
        :param func: mapping function
        """
        if self.lchild is not None:
            self.lchild.preorderTraversal(func)
        if self.rchild is not None:
            self.rchild.preorderTraversal(func)
        func(self.data)
