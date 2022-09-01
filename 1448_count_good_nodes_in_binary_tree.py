from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue, counter = [root], 0

        def dfs(node, max_val):
            nonlocal counter

            if node:
                if node.val >= max_val:
                    max_val = node.val
                    counter += 1
                dfs(node.left, max_val)
                dfs(node.right, max_val)

        dfs(root, -10 ** 4)
        return counter

    # From discussion comments
    # https://leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/2512547/C++-or-Python-or-C97-DFSDetailed-graph-explantion-or-Beginner-friendly-or-Easy-to-understand-_/1582311
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], _max: int) -> int:
            # If the given root node is None, there are no good nodes.
            # Otherwise, first check if the root node is a good node,
            # then check how many good nodes are there in the left subtree,
            # then check how many good nodes are there in the right subtree,
            # and finally return the total number of good nodes.
            _max = max(node.val, _max) if node else _max
            return (node.val == _max) + dfs(node.left, _max) + dfs(node.right, _max) if node else 0

        return dfs(root, -10 ** 4)  # the minimum value is -10000 according to the constraints
