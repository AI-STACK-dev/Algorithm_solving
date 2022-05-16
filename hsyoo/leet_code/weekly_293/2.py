class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        answer = 0
        max_ = -1
        n = len(special)
        special.sort()
        if special[0] - bottom > 1:
            max_ = max(max_, special[0] - bottom)
        for idx in range(1,n):
            diff = special[idx] - special[idx-1]
            if diff > 1:
                max_ = max(max_, diff-1)
        if top - special[-1] > 1:
            max_ = max(max_, top - special[-1])
        return max_ if max_ > 0 else -1

print(Solution.maxConsecutive(2, 9, [4,6]))