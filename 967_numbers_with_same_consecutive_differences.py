from typing import Set, List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> Set[str]:

        res = set()

        def bfs(q):
            if q:
                snn_1 = snn_2 = q.pop()
                nn = int(snn_1[-1])
                pnn = nn + k
                mnn = nn - k
                if pnn < 10:
                    snn_1 += str(pnn)
                    if len(snn_1) == n:
                        res.add(snn_1)
                    elif len(snn_1) < n:
                        q.add(snn_1)
                if mnn >= 0:
                    snn_2 += str(mnn)
                    if len(snn_2) == n:
                        res.add(snn_2)
                    elif len(snn_2) < n:
                        q.add(snn_2)
                bfs(q)

        queue = set(list(map(str, (range(1, 10)))))
        bfs(queue)

        return res

    # Better
    # From discussions:
    # https://leetcode.com/problems/numbers-with-same-consecutive-differences/discuss/2524567/PythonBFS-Easiest-approachDetailed-explained-or-Beginner-friendly-or-Easy-to-understand
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        # BFS solution
        res = []
        q = set((1, d) for d in range(1, 10))

        while q:
            pos, num = q.pop()  # get one element
            if pos == n:  # check if we meet the length we want
                res.append(num)  # we no longer need to append number if we meet the length
            else:
                for j in range(10):  # loop through 0~9
                    if abs(num % 10 - j) == k:  # check if the difference between two digits is k
                        q.add((pos + 1, num * 10 + j))

        return res
