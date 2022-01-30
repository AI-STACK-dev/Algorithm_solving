class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        hashDict = {}
        start = ord('a')
        for alp in range(26):
            hashDict[chr(start+alp)] = alp+1
        
        for i in range(0,len(s)-k+1):
            string = s[i:i+k]
            val = 0
            for j in range(k):
                val += (hashDict[string[j]]) * (power**j)
            if hashValue ==  (val % modulo):
                return string