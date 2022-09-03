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
            # if queue is not empty
            if q:
                # create the next level queue and list for this level values
                next_q, line = [], []
                for node in q:
                    # if there is a node
                    if node:
                        # then we add its value to the line list
                        line.append(node.val)
                        # and child nodes to next queue
                        next_q.append(node.left)
                        next_q.append(node.right)
                if line:
                    # add the line list to the resulting list
                    res.append(line)
                # and after we recursively perform the same operation for each of the child nodes
                xfs(next_q)
            # create the queue with the root and the resulting list

        queue, res = [root], []
        xfs(queue)
        return res

    # 2 Iterative (46 ms / 14.2 MB)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # create the queue and the resulting list
        queue, res = [root], []
        # now until the queue is empty
        while queue:
            # create the next level queue and list for this level values
            next_queue, line = [], []
            for node in queue:
                # node may be empty if it's leaf node
                # the further course of the solution coincides with the recursive method
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
