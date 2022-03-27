class Solution:
    def kthPalindrome(self, queries: List[int], n: int) -> List[int]:
        maxNum = 9
        startNum = 1
        halfN = n//2 

        if n == 1:
            maxNum += 1
        elif n %2 == 0:
            startNum = 10**(halfN -1)
            maxNum *= startNum
        else:
            startNum = 10**(halfN)
            maxNum *= startNum
        
        dataRepo = []
        for i in range(startNum, startNum + maxNum):
            s = str(i)
            rev = "".join(reversed(s[:halfN]))
            dataRepo.append(int("".join([s,rev])))
            
        ans = []
        for i in queries:
            if i > maxNum:
                ans.append(-1)
            else:
                ans.append(dataRepo[i-1])

        return ans

