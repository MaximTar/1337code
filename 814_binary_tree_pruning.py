from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # First, we recursively traverse the nodes of the binary tree and descend to its leaves.
    # Then we begin to rise from the leaves to the root.
    # We check if the node has no leaves (not root.left and not root.right) and its value is zero (root.val == 0), then we return None.
    # Thus, its parent node will lose one child.
    # If the same parent node also loses the second child
    # (that is, it will not have children and its value will be equal to zero),
    # then further we will check it (this very parent) for equality to zero.
    # We will repeat until we come across a leaf whose value will be equal to one and return it.
    # With further traversal to the root, this branch will no longer meet the condition of having no children.

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if not root.left and not root.right and root.val == 0:
                return None
        return root

    # https://leetcode.com/problems/binary-tree-pruning/discuss/2540001/Python-or-3-Liner
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        return root if (root.left or root.right or root.val == 1) else None
