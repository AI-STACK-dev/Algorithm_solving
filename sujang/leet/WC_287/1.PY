class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curH, curM = map(int,current.split(":"))
        corrH, corrM = map(int,correct.split(":"))

        totalM = (corrH-curH)*60 + (corrM-curM)

        ans = 0
        for unit in [60,15,5]:
            ans += (totalM // unit)
            totalM = totalM % unit
        ans += totalM
        return ans
