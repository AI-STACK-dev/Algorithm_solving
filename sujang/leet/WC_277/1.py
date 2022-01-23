class Solution:
    def countElements(self, nums: List[int]) -> int:
        MAX = max(nums)
        MIN = min(nums)
        cnt = 0
        for i in nums:
            if i != MAX and i!= MIN:
                cnt += 1
        return cnt
