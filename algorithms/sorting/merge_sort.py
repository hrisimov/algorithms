from typing import List


# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'({self.key}, {self.value})'


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs

        def merge_sort(pairs, s, e):
            if s == e:
                return

            # m = s + (e - s) // 2
            m = (s + e) // 2
            merge_sort(pairs, s, m)
            merge_sort(pairs, m + 1, e)
            self.__merge(pairs, s, m, e)

        merge_sort(pairs, 0, len(pairs) - 1)
        return pairs

    @staticmethod
    def __merge(pairs, s, m, e):
        left_half = pairs[s: m + 1]
        right_half = pairs[m + 1: e + 1]

        i = 0
        j = 0
        k = s

        while i < len(left_half) and j < len(right_half):
            if left_half[i].key <= right_half[j].key:
                pairs[k] = left_half[i]
                i += 1
            else:
                pairs[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            pairs[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            pairs[k] = right_half[j]
            j += 1
            k += 1
