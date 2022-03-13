class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        front,end = s.split(":")
        fA,fNum = front[0],front[1]
        eA,eNum = end[0],end[1]

        ans = []
        for alp in range(ord(fA), ord(eA)+1):
            for num in range(int(fNum),int(eNum) + 1):
                ans.append(chr(alp) + str(num))

        return ans