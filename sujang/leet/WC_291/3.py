from collections import defaultdict

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        check = [False]*n
        for i in range(n):
            if nums[i] % p == 0:
                check[i] = True

        ans = defaultdict(int)
        for i in range(n):
            temp = 0
            prev = ""
            for j in range(i,n):
                if check[j] == True:
                    temp += 1
                if temp > k:
                    break
                prev += " "+str(nums[j])
                ans[prev] += 1
        return len(ans)
