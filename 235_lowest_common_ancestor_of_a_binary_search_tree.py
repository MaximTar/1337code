# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # For clarity, we choose the smallest and largest of the given nodes.
    # Let's use the tree structure: we know that key of each internal node is greater
    # than all the keys in the respective node's left subtree and less than the ones in its right subtree.
    # Thus, if a node is located between the minimum and maximum - this node is the lowest common ancestor.
    # Otherwise, if the node's current value is greater than the maximum, we move to the left.
    # Similarly, if less than the minimum - to the right.
    # Repeat until we get an answer.

    # 1 Recursive
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def lca(node):
            value = node.val
            if left <= value <= right:
                return node
            elif right < value:
                lca(node.left)
            elif left > value:
                lca(node.right)

        left = min(p.val, q.val)
        right = max(p.val, q.val)
        return lca(root)

    # 2 Iterative
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        left = min(p.val, q.val)
        right = max(p.val, q.val)

        while root:
            value = root.val
            if left <= value <= right:
                return root
            elif right < value:
                root = root.left
            elif left > value:
                root = root.right
