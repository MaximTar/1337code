from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        # create the queue and the resulting list
        queue = [root] if root else None
        result = []
        # now until the queue is empty
        while queue:
            # create the next level queue and list for this level values
            q, level = [], []
            # for every node in queue
            for node in queue:
                # append its value to the line list
                level.append(node.val)
                # and if the node have children
                if node.children:
                    # add them to the next queue
                    q.extend(node.children)
            # add the line list to the resulting list
            result.append(level)
            # and after we recursively perform the same operation for the next level queue
            queue = q
        return result
