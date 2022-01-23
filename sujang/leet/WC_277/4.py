class Solution:
    def valid(self, guess, statements):
        n = len(statements)
        for i in range(n):
            typ = guess[i]
            if typ == 1:
                for j in range(n):
                    if statements[i][j]!=2 and statements[i][j] != guess[j]:
                        return False
        return True

    def maximumGood(self,statements:List[List[int]]) -> int:
        n = len(statements)
        ans = 0
        for i in range(1 << n):
            guess = [int(x) for x in bin(i)[2:].zfill(n)]
            if self.valid(guess, statements):
                ans = max(ans,sum(guess))
        return ans






