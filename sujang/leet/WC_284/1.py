class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        keyIndexs = []
        for i in range(len(nums)):
            if key == nums[i]:
                keyIndexs.append(i)
        
        ans = []
        for i in range(len(nums)):
            for j in keyIndexs:
                if abs(j-i) <= k:
                    ans.append(i)
                    break
        
        ans.sort()
        return ans