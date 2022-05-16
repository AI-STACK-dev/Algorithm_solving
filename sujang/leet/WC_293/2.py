from collections import deque
class Solution:
    def maxConsecutive(self, bot: int, top: int, special: List[int]) -> int:
        ans = 0
        special.sort()
        s = deque(special)
        s.appendleft(bot);s.append(top)
        n = len(s)
        for i in range(n-1):
            amt = 1
            if i == 0 or i==n-2:
                amt = 0
            ans = max(ans,s[i+1]-s[i] - amt)
        return ans
