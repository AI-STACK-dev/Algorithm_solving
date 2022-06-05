class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        numsRepo = defaultdict(int)

        for i in range(len(nums)):
            numsRepo[nums[i]] = i

        for a,b in operations:
            idx = numsRepo[a]
            nums[idx] = b
            numsRepo[b] = idx
        
        return nums
