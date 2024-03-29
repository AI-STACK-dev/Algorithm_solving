class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            temp = []

            n = len(nums)
            for i in range(0,n//2):
                if i % 2 == 0:
                    temp.append(min(nums[i*2], nums[i*2+1]))
                else:
                    temp.append(max(nums[i*2], nums[i*2+1]))
            
            nums = temp
        return nums[0]