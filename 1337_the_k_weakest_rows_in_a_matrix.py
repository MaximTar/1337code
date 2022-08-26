from collections import Counter
# from heapq import heappush
# import numpy as np
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dct = {}
        for idx, row in enumerate(mat):
            dct[idx] = Counter(row)[1]
        return list(dict(sorted(dct.items(), key=lambda item: item[1])).keys())[:k]

    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     dct = {}
    #     for idx, row in enumerate(mat):
    #         counter = 0
    #         for el in row:
    #             if el == 0:
    #                 break
    #             counter += 1
    #         dct[idx] = counter
    #     return list(dict(sorted(dct.items(), key=lambda item: item[1])).keys())[:k]

    # not good with memory usage (numpy)
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     dct = {}
    #     for idx, row in enumerate(mat):
    #         dct[idx] = Counter(row)[1]
    #     ar = np.array(list(dct.items()))
    #     return ar[np.lexsort((ar[:, 1], ar[:, 0]))][:k]

    # one-liner but slow and use much memory
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     return np.argsort(np.sum(mat, axis=1), kind='mergesort')[:k]

    # interesting approach
    # https://dev.to/seanpgallivan/solution-the-k-weakest-rows-in-a-matrix-2679
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     y, x = len(mat), len(mat[0])
    #     vis, ans = [0] * y, []
    #     for j in range(x + 1):
    #         for i in range(y):
    #             if not vis[i] and (j == x or not mat[i][j]):
    #                 ans.append(i)
    #                 vis[i] = 1
    #             if len(ans) == k:
    #                 return ans

    # wrong
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     heap = []
    #     for idx, row in enumerate(mat):
    #         counter = 0
    #         for el in row:
    #             if el == 0:
    #                 break
    #             counter += 1
    #         heappush(heap, (counter, idx))
    #     _, res = zip(*heap[:k])
    #     return res
