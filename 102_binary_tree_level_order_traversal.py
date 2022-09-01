from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 1 Recursive
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def xfs(q):
            if q:
                next_q, line = [], []
                for node in q:
                    if node:
                        line.append(node.val)
                        next_q.append(node.left)
                        next_q.append(node.right)
                if line:
                    res.append(line)
                xfs(next_q)

        queue, res = [root], []
        xfs(queue)
        return res

    # 2 Iterative (46 ms / 14.2 MB)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, res = [root], []

        while queue:
            next_queue, line = [], []
            for node in queue:
                if node:
                    line.append(node.val)
                    next_queue.append(node.left)
                    next_queue.append(node.right)
            if line:
                res.append(line)
            queue = next_queue
        return res

    # 3 Deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            res.append([])
            for _ in range(len(q)):
                node = q.popleft()
                res[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
