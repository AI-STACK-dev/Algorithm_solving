class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        ans = []
        for i in range(len(pos)):
            ans.extend((pos[i],neg[i]))
        return ans