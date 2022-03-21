class Solution(object):
    def countHillValley(self, nums):
        new_nums = []

        # remove continuous duplicate
        prev = nums[0]
        new_nums.append(prev)
        for n in nums[1:]:
            if n != prev:
                new_nums.append(n)
            prev = n
        
        # decision
        ans = 0
        for i in range(1,len(new_nums)-1):
            if new_nums[i-1] < new_nums[i] and new_nums[i+1] < new_nums[i]:
                ans += 1 
            if new_nums[i-1] > new_nums[i] and new_nums[i+1] > new_nums[i]:
                ans += 1 
        
        return ans



