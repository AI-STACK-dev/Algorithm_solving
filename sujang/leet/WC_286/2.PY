class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        cnt = 0
        while i < n:
            if nums[i-1] == nums[i]:
                i -= 1
                cnt += 1
            i += 2
        if n == i:
            cnt += 1
        return cnt
        
        