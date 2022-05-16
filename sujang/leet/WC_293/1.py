class Solution:
    def removeAnagrams(self, ws: List[str]) -> List[str]:
        n = len(ws)
        done = [False]*n 
        ans = []
        for i in range(n):
            tar = "".join(sorted(list(ws[i])))
            for j in range(i+1,n):
                cur = "".join(sorted(list(ws[j])))
                if cur != tar:
                    break
                done[j] = True
            if not done[i]:
                ans.append(ws[i])
        return ans
