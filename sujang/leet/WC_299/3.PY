class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        s1 = sum(nums1)
        s2 = sum(nums2)
        origMax = max(s1,s2)

        s1_s2 = [0]*n
        for i in range(n):
            s1_s2[i] = nums1[i] - nums2[i]
        amt1 = self.calSeqSumMax(s1_s2)
        origMax = max(origMax, max(s1-amt1,s2+amt1))

        s2_s1 = [0]*n
        for i in range(n):
            s2_s1[i] = nums2[i] - nums1[i]
        amt2 = self.calSeqSumMax(s2_s1)
        origMax = max(origMax, max(s1+amt2,s2-amt2))

        return origMax

    def calSeqSumMax(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        cache[0] = nums[0]

        for i in range(1, len(nums)):
            cache[i] = max(0, cache[i-1]) + nums[i]

        return max(cache)

