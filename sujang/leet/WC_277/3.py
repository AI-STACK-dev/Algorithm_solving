class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        isThere = [0]*1000003
        ans = []
        for i in nums:
            isThere[i+1] += 1
        for i in nums:
            if isThere[i]==0 and isThere[i+2]==0 and isThere[i+1]==1:
                ans.append(i)
        return ans