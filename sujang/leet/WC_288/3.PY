class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, di = 0 ,1
        
        if len(nums) == 1:
            return (nums[0] + k) % (10**9+7)

        while k > 0:
            nums[i] += 1            

            nexti = i + di
            k -= 1
            # change directions
            if nexti < 0 or nexti >= len(nums) or nums[i] < nums[nexti]:
                di *= -1
            elif nums[i] == nums[nexti]:
                i = 0
            else:
                i = nexti
        
        ans = 1
        for i in nums:
            ans =(ans*i )% (10**9+7)
        return ans
        
            