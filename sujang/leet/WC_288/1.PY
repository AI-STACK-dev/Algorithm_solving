class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(map(int,list(str(num))))
        N = len(num)
        pos = [0]*N

        odds, evens = [], []
        for i,n in enumerate(num):
            if n % 2 == 0:
                evens.append(n)
            else:
                pos[i] = 1
                odds.append(n)
        odds.sort();evens.sort()

        ans = []
        for i in range(N):
            if pos[i] == 0:
                ans.append(str(evens.pop()))
            else:
                ans.append(str(odds.pop()))

        return "".join(ans)
