class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        numberList = list(number)

        for i in range(n):
            if numberList[i] == digit:
                prev = i
                if i+1 < n and  numberList[i] < numberList[i+1]:
                    return "".join(numberList[:i] + numberList[i+1:])
        
        return "".join(numberList[:prev] + numberList[prev+1:])
