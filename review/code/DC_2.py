from typing import Optional


class BinaryTree():
    def __init__(self, val, left_child=None, right_child=None):
        self.val = val
        self.left_child: Optional[BinaryTree] = left_child
        self.right_child: Optional[BinaryTree] = right_child

    def __str__(self):
        return str(self.val)


def solve(tree: BinaryTree):
    if tree.left_child is None and tree.right_child is None:
        return tree

    if tree.left_child.val < tree.val:
        return solve(tree.right_child)

    if tree.right_child is not None and tree.right_child.val < tree.val:
        return solve(tree.right_child)

    # values of all children are greater than current node, return current node
    return tree


tree = BinaryTree(8)
print(solve(tree))
