from collections import defaultdict

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cntDict = defaultdict(int)
        for t in tasks:
            cntDict[t] += 1

        ans = 0
        for k in cntDict.keys():
            val = cntDict[k]
            if val == 1:
                return -1
            elif val == 2:
                ans += 1
            else:
                div = val // 3
                quo = val % 3
                if quo == 0:
                    ans += div
                else:
                    ans += div + 1
        return ans
