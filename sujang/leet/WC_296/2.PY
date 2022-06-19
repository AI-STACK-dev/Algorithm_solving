class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = 1
        prev = nums[0]
        for n in nums:
            if (n - prev) > k:
                ans += 1
                prev = n
        
        return ans
