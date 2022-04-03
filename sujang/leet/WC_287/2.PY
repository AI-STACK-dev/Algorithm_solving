from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ws = []
        ls = []
        ls1 = []
        for w,l in matches:
            ws.append(w)
            ls.append(l)
        for k,v in Counter(ls).items():
            if v == 1:
                ls1.append(k)
        ans = []
        ans.append(sorted(list(set(ws) - set(ls))))
        ans.append(sorted(ls1))

        return ans
