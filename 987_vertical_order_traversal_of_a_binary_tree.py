from typing import Optional, List, ValuesView
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 1 Head-on / Recursive
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def xfs(node, idx):
            if idx in dct:
                dct[idx].append(node.val)
            else:
                dct[idx] = [node.val]
            c, r = idx
            if node.left:
                xfs(node.left, (c - 1, r + 1))
            if node.right:
                xfs(node.right, (c + 1, r + 1))

        dct = {}
        xfs(root, (0, 0))

        sorted_keys = sorted(dct.keys())
        res = []
        for key_idx in range(len(sorted_keys)):
            key = sorted_keys[key_idx]
            if key_idx > 0 and key[0] == sorted_keys[key_idx - 1][0]:
                res[-1].extend(sorted(dct[key]))
            else:
                res.append(sorted(dct[key]))

        return res

    # 2 Iterative
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        dct = {}
        q = {(root, (0, 0))}

        while q:
            node, idx = q.pop()
            if idx in dct:
                dct[idx].append(node.val)
            else:
                dct[idx] = [node.val]
            c, r = idx
            if node.left:
                q.add((node.left, (c - 1, r + 1)))
            if node.right:
                q.add((node.right, (c + 1, r + 1)))

        sorted_keys = sorted(dct.keys())
        res = []
        for key_idx in range(len(sorted_keys)):
            key = sorted_keys[key_idx]
            if key_idx > 0 and key[0] == sorted_keys[key_idx - 1][0]:
                res[-1].extend(sorted(dct[key]))
            else:
                res.append(sorted(dct[key]))

        return res

    # 3 Iterative with DefaultDict (35 ms / 14.2 MB)
    # Runtime: 35 ms, faster than 95.00% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:  # ValuesView[list]:

        # create a dictionary of nodes (position: value)
        # position consists of a column and a row (not row + column)
        # order is important for further sorting
        # defaultdict is required to be able to call the list methods on a "non-existent" list
        nodes = defaultdict(list)
        # create a queue with the root
        queue = {(root, (0, 0))}

        # until the queue is empty
        while queue:
            # pop a node and a position from it
            node, pose = queue.pop()
            # if the node is None, then move on
            if not node:
                continue
            # add the value of the node to the dictionary
            nodes[pose].append(node.val)
            # unpack the position to update the queue
            column, row = pose
            queue.update(((node.left, (column - 1, row + 1)),
                          (node.right, (column + 1, row + 1))))

        # sort the keys of the node dictionary
        # they will be in the order we need - first by column, then by row
        # that is, for example, [(2, 2), (2, 4), (1, 3), (1, 1)] will become [(1, 1), (1, 3), (2, 2), (2, 4)]
        sorted_keys = sorted(nodes.keys())

        # now, having passed through the sorted keys,
        # it remains only to add the corresponding values from the dictionary into the list
        res = []
        for key_idx in range(len(sorted_keys)):
            key = sorted_keys[key_idx]
            # if there multiple nodes in the same row and same column, these nodes should be sorted by their values
            nodes[key].sort()
            # but if the column matches the previous one, then the previous sheet needs to be extended, not appended
            if key_idx > 0 and key[0] == sorted_keys[key_idx - 1][0]:
                res[-1].extend(nodes[key])
            else:
                res.append(nodes[key])
        return res

        # another approach to implement the last step
        # res = defaultdict(list)
        # for column, row in sorted_keys:
        #     print(res)
        #     nodes[(column, row)].sort()
        #     res[column].extend(nodes[(column, row)])
        # return res.values()
