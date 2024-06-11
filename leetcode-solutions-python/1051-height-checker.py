from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        unmatched_number = 0
        expects = sorted(heights)
        assert len(expects) == len(heights)
        for i in range(len(heights)):
            if heights[i] != expects[i]:
                unmatched_number +=1

        return unmatched_number

