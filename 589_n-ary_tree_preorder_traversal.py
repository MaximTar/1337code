from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # 1 Head-on
    def preorder(self, root: Node) -> List[int]:

        def xfs(q):
            if q:
                node = q.pop(0)
                if node:
                    q = node.children + q
                    res.append(node.val)
                xfs(q)

        queue, res = [root], []
        xfs(queue)
        return res

    # 2 More elegant
    def preorder(self, root: Node) -> List[int]:

        def xfs(node):
            # if there is a node
            if node:
                # then we add its value to the resulting list
                res.append(node.val)
                # and after we recursively perform the same operation for each of the child nodes
                for child_node in node.children:
                    xfs(child_node)

        # create the resulting list
        res = []
        # and pass the root to the function
        xfs(root)
        return res

    # 3 Follow up: Recursive solution is trivial, could you do it iteratively?
    # Runtime: 52 ms, faster than 94.37% of Python3 online submissions for N-ary Tree Preorder Traversal.
    # Memory Usage: 15.9 MB, less than 97.56% of Python3 online submissions for N-ary Tree Preorder Traversal.
    def preorder(self, root: Node) -> List[int]:
        # create the queue and the resulting list
        queue, res = [root], []
        # now until the queue is empty
        while queue:
            # take the first element from the queue
            node = queue.pop(0)
            # if it's not empty
            # (may be empty if we came here from a leaf of a tree)
            if node:
                # then we put the child nodes in the queue
                # must be summed in this order to get the correct result
                # (if we change the order, then in the first example from the task
                # from node "3" we will go to node "2", but we need to go to node "5")
                queue = node.children + queue
                # now just store the result in a list
                res.append(node.val)
        # and return it
        return res
