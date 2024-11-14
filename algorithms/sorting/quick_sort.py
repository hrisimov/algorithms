from typing import List


# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'({self.key}, {self.value})'


"""
                   |    Time Complexity    |     Space Complexity
--------------------------------------------------------------------
    Best Case      |     O(n * log(n))     |        O(log(n))
                   |                       |
   Average Case    |     O(n * log(n))     |        O(log(n))
                   |                       |
    Worst Case     |       O(n ^ 2)        |          O(n)
--------------------------------------------------------------------
n - Number of pairs
"""


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quick_sort(pairs, s, e):
            if s >= e:
                return

            p = self.__partition(pairs, s, e)
            quick_sort(pairs, s, p - 1)
            quick_sort(pairs, p + 1, e)

        quick_sort(pairs, 0, len(pairs) - 1)
        return pairs

    @staticmethod
    def __partition(pairs, s, e):
        pivot = pairs[e]
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1

        pairs[left], pairs[e] = pairs[e], pairs[left]
        return left
