from io import StringIO
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 1 Recursive
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            if node:
                result_str = f"{node.val}"
                left, right = dfs(node.left), dfs(node.right)
                if left:
                    result_str += f"({left})"
                if right and not left:
                    result_str += f"()({right})"
                elif right:
                    result_str += f"({right})"
                return result_str

        return dfs(root)

    # 2 Optimization with join / 51 ms
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            if node:
                # If the node exists, take its value
                result_str = f"{node.val}"
                # Next, we call the function recursively for the node's children
                left, right = dfs(node.left), dfs(node.right)
                # Now we look at the result:
                # if the left child is returned, then we append it to the result string
                if left:
                    result_str = ''.join([result_str, f"({left})"])
                # if only the right one returned, then we need to add brackets on the left
                if right and not left:
                    result_str = ''.join([result_str, f"()({right})"])
                # if both returned, then add the right one (we added the left one above)
                elif right:
                    result_str = ''.join([result_str, f"({right})"])
                return result_str

        return dfs(root)

    # 3 Shortened Recursive with join / 61 ms
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return ''.join([f"{root.val}",
                        f"({self.tree2str(root.left)})" if root.left else "()" if root.right else "",
                        f"({self.tree2str(root.right)})" if root.right else ""])
