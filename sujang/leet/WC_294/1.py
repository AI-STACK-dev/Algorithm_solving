class Solution:
    def percentageLetter(self, s: str, l: str) -> int:
        N = len(s)
        n = 0
        for i in s:
            if i == l:
                n += 1
        return math.floor((n/N)*100)