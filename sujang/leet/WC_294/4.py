from itertools import accumulate

class Solution:
    def totalStrength(self, A):
        mod = 10 ** 9 + 7
        n = len(A)

        right = [n] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                right[stack.pop()] = i
            stack.append(i)

        left = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                left[stack.pop()] = i
            stack.append(i)

        res = 0
        acc = list(accumulate(accumulate(A), initial = 0))
        for i in range(n):
            l, r = left[i], right[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res += A[i] * (racc * ln - lacc * rn) % mod
        return res % mod


a = [1,3,1,2]
print(Solution().totalStrength(a))

