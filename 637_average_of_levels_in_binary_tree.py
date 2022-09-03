from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The main idea is to introduce a separate list for the current level and the next level of the graph.
class Solution:
    # 1 Recursive
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def xfs(q):
            # if queue is not empty
            if q:
                # create the next level queue and list for this level values
                next_level, current_level = [], []
                for node in q:
                    # if there is a node
                    if node:
                        # then we add its value to the level list
                        current_level.append(node.val)
                        # and child nodes to next queue
                        next_level.append(node.left)
                        next_level.append(node.right)
                if current_level:
                    # add the average value of the level to the resulting list
                    res.append(sum(current_level) / len(current_level))
                # and after we recursively perform the same operation for each of the child nodes
                xfs(next_level)
            # create the queue with the root and the resulting list

        queue, res = [root], []
        xfs(queue)
        return res

    # 2 Iterative
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[List[int]]:
        # create the queue and the resulting list
        queue, res = [root], []
        # now until the queue is empty
        while queue:
            # create the next level queue and list for this level values
            next_level, current_level = [], []
            for node in queue:
                # node may be empty if it's leaf node
                # the further course of the solution coincides with the recursive method
                if node:
                    current_level.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            if current_level:
                res.append(sum(current_level) / len(current_level))
            queue = next_level
        return res
