from collections import defaultdict

class Solution:
    def largestCombination(self, cs) -> int:
        repo = [0]*(25)
        for c in cs:
            curr = bin(c)[2:][::-1]
            for i in range(len(curr)):
                if curr[i] == "1":
                    repo[i] += 1
        return max(repo)


a = [16,17,71,62,12,24,14]
print(Solution().largestCombination(a))
