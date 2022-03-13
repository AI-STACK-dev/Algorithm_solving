class Solution(object):
    def minSteps(self, s, t):
        tableS = [0]*26
        tableT = [0]*26
        for i in s:
            tableS[ord(i)-ord("a")] += 1
        for i in t:
            tableT[ord(i)-ord("a")] += 1
        
        ans = 0
        for i in range(26):
            ans += abs(tableS[i]-tableT[i])
        
        return ans