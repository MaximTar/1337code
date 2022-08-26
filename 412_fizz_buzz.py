from typing import List
# import math


class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    #     res = []
    #     for i in range(1, n + 1):
    #         if i % 3 == 0:
    #             if i % 5 == 0:
    #                 res.append('FizzBuzz')
    #             else:
    #                 res.append('Fizz')
    #         elif i % 5 == 0:
    #             res.append('Buzz')
    #         else:
    #             res.append(str(i))
    #     return res

    # faster but needs more memory (strings)
    # def fizzBuzz(self, n: int) -> List[str]:
    #     res = []
    #     for i in range(1, n + 1):
    #         s = ''
    #         if i % 3 == 0:
    #             s += 'Fizz'
    #         if i % 5 == 0:
    #             s += 'Buzz'
    #         res.append(s if s else str(i))
    #     return res

    # def fizzBuzz(self, n: int) -> List[str]:
    #     m = n + 1
    #     res = list(map(str, range(m)))
    #     res[::3] = ['Fizz'] * int(math.ceil(m / 3))
    #     res[::5] = ['Buzz'] * int(math.ceil(m / 5))
    #     res[::15] = ['FizzBuzz'] * int(math.ceil(m / 15))
    #     return res[1:]

    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            s = None
            if i % 15 == 0:
                s = 'FizzBuzz'
            elif i % 3 == 0:
                s = 'Fizz'
            elif i % 5 == 0:
                s = 'Buzz'
            res.append(s if s else str(i))
        return res
