class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        N = len(nums)
        numZero = [0]*(N+1)
        numOne = [0]*(N+1)
        for i in range(1,N+1):
            numZero[i] += numZero[i-1] + ( 1 if nums[i-1] == 0 else 0)
        for i in range(N-1,-1,-1):
            numOne[i] += numOne[i+1] + ( 1 if nums[i] == 1 else 0)


        ans = []
        Max = 0
        for i in range(N+1):
            temp = numOne[i] + numZero[i]
            if temp > Max:
                ans = []
                ans.append(i)
                Max = temp
            elif temp == Max:
                ans.append(i)
        return ans



