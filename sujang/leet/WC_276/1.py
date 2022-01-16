class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        quo = n // k
        remain = n % k
        ans = []
        for i in range(0,quo+1):
            if i == quo:
                if remain == 0:
                    break
                add = fill*(k-remain)
                ans.append(s[i*k:]+add)
            else:
                ans.append(s[i*k:(i+1)*k])
        return ans
