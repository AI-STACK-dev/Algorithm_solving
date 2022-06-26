class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [0]*int(1e4+1)
        dp[1] = 2
        dp[2] = 3
        if n <= 2:
            return dp[n]**2

        for i in range(3,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return int(dp[n]**2 % int(1e9+7))