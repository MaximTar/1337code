from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        queue = [root] if root else None
        result = []
        while queue:
            q, level = [], []
            for node in queue:
                level.append(node.val)
                if node.children:
                    q.extend(node.children)
            result.append(level)
            queue = q
        return result
