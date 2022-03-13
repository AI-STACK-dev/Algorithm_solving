from math import inf
class Solution:
    def minimalKSum(self, nums, k):
        ans = k*(k+1)//2
        prev = -1
        for x in sorted(nums): 
            if prev < x: 
                if x <= k: 
                    k += 1
                    ans += k - x
                else: break
                prev = x
        return ans 
