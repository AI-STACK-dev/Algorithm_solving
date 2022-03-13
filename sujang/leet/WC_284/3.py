from collections import deque
from curses.ascii import NL
class Solution(object):
    def maximumTop(self, nums, k):
        n = len(nums)
        if n == 1 and k%2 == 1:
            return -1
        if k == 0:
            return nums[0]
        if k == 1:
            return nums[1]
        if k > n:
            return max(nums)
        if k == n:
            return max(nums[:n-1])
        if k < n:
            return max(max(nums[:k-1]), nums[k])
        