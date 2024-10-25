from typing import List


# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'({self.key}, {self.value})'


class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        pairs_states = []

        for i in range(len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1

            pairs_states.append(pairs.copy())

        return pairs_states
