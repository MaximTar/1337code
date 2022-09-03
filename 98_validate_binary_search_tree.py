from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Many options: https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_bst(node, mn, mx):
            if node is None:
                return True

            if node.val <= mn or node.val >= mx:
                return False

            return (is_bst(node.left, mn, node.val) and
                    is_bst(node.right, node.val, mx))

        max_val = 2147483648
        min_val = -2147483649

        return is_bst(root, min_val, max_val)
