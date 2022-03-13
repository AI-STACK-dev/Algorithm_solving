class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odds = []
        evens = []
        for i in range(len(nums)):
            if i%2==0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        odds.sort(reverse=True)
        evens.sort()

        ans = []
        for i in range(len(nums)//2):
            ans.append(evens.pop(0))
            ans.append(odds.pop(0))
        if evens:
            ans.append(evens.pop())
        return ans
