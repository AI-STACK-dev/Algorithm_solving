class Solution(object):
    def prefixCount(self, words, pref):
        cnt = len(pref)
        ans = 0
        for w in words:
            if len(w) >= cnt and w[:cnt] == pref:
                ans += 1
        return ans

