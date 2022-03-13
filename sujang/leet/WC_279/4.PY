class Solution(object):
    def minimumTime(self, s):
        left, res, n = 0, len(s), len(s)
        for i,c in enumerate(s):
            left = min(left + (c == '1') * 2, i + 1)
            res = min(res, left + n - 1 - i)
        return res
        