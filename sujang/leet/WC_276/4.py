class Solution:
    def maxRunTime(self, n: int, A: List[int]) -> int:
        A.sort()
        su = sum(A)
        while A[-1] > su / n:
            n -= 1
            su -= A.pop()
        return su / n
