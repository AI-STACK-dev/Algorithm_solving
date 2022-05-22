class Solution:
    def maximumBags(self, cs: List[int], rs: List[int], a: int) -> int:
        n = len(cs)
        sub = [0]*n
        for i in range(n):
            sub[i] = cs[i] - rs[i]
        sub.sort()        

        prev = 0
        result = 0
        for s in sub:
            prev += s
            if prev <= a:
                result += 1
            else:
                break
        return result        
