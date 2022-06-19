class Solution:
    def partitionArray(self, nums, k):
        n = len(nums)
        answer = 1
        start, end = 0, 0
        nums.sort()
        while end != n:
            if nums[end] - nums[start] > k:
                answer += 1
                start = end
            end +=1 
        return answer

print(Solution().partitionArray([3,6,1,2,5], 2))
print(Solution().partitionArray([1,2,3], 1))
print(Solution().partitionArray([2,2,4,5], 0))