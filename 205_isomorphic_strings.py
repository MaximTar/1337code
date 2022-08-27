class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ls = len(s)
        if ls != len(t):
            return False
        ds, dt = {k: [] for k in set(s)}, {k: [] for k in set(t)}
        for i in range(ls):
            ds[s[i]].append(i)
            dt[t[i]].append(i)
        return sorted(ds.values()) == sorted(dt.values())

    # better solution:
    # https://leetcode.com/problems/isomorphic-strings/discuss/2484918/Easy-Python-Solution-beats-99-solutions-using-hash-map
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     smap = {}
    #     tmap = {}
    #     for a, b in zip(s, t):
    #         if a in smap.keys():
    #             if smap[a] != b:
    #                 return False
    #         elif b in tmap.keys():
    #             if tmap[b] != a:
    #                 return False
    #         else:
    #             smap[a] = b
    #             tmap[b] = a
    #     return True
