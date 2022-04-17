class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            splitS = [ s[i:i+k] for i in range(0,len(s),k)]
            temp = []
            for frag in splitS:
                Sum = 0
                for c in frag:
                    Sum += int(c)
                temp.append(Sum)
            s = "".join(map(str, temp))
        return s
        