class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, sum(candies) // k
        while left < right:
            mid = (left+1+right) // 2
            if k <= sum( c // mid for c in candies):
                left = mid
            else:
                right = mid - 1
        return left

