class Solution:
    def minMaxGame(self, nums):
        new_nums = []
        while len(nums) != 1:
            n = len(nums)
            new_nums = [0] * (n//2)
            for i in range(n//2):
                if i % 2 == 0:
                    new_nums[i] = min(nums[2*i], nums[2*i+1])
                else:
                    new_nums[i] = max(nums[2*i], nums[2*i+1])
            nums = new_nums
        return nums[0]

print(Solution().minMaxGame([1,3,5,2,4,8,2,2]))
print(Solution().minMaxGame([3]))