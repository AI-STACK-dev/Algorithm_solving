class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = int(1e9)
        n = len(cards)
        temp = [-1]*1000001
        for i in range(n):
            element = cards[i]
            if temp[element] != -1:
                ans = min(i - temp[element]+1, ans)    
            temp[element] = i
        return ans if ans != int(1e9) else -1
        