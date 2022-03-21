from copy import deepcopy
class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        maxScore = 0
        ans = []
        def dfs(arrCount, bobArrows, bobScore, arrIndex):
            nonlocal maxScore, ans
            if arrCount > numArrows:
                return
            if arrIndex > 11 or arrCount == numArrows:
                if  bobScore > maxScore:
                    maxScore = bobScore
                    ans = bobArrows
                    if numArrows > arrCount:
                        ans[0] += numArrows - arrCount
                return

            # skip this Bob's arrow
            temp1 = deepcopy(bobArrows)
            dfs(arrCount, temp1, bobScore, arrIndex+1)

            # Bob earn point
            temp2 = deepcopy(bobArrows)
            temp2[arrIndex] = aliceArrows[arrIndex] + 1
            bobScore += arrIndex
            dfs(arrCount+temp2[arrIndex], temp2, bobScore, arrIndex+1)

        dfs(0,[0]*12,0,0)
        return ans

numArrows = 3
aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]
s = Solution()
print(s.maximumBobPoints(numArrows, aliceArrows))
