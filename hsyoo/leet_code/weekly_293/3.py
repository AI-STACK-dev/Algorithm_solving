from itertools import combinations

class Solution:
    def largestCombination(self, candidates) -> int:
        max_ = -1
        answer = 0
        n = len(candidates)
        for r in range(n, 1, -1):
            combs = list(combinations(candidates, r))
            for comb in combs:
                case = comb[0]
                for v in range(1, r):
                    case = case & comb[v]
                if case > 0:
                    return r
        # return answer
print(Solution().largestCombination([16,17,71,62,12,24,14]))