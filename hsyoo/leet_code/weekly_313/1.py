class Solution:
    def commonFactors(self, a, b):
        min_ = min(a, b)
        answer = 0
        for i in range(1, min_+1):
            if a % i == 0 and b % i == 0:
                answer +=1
        return answer
print(Solution().commonFactors(12, 6))
        