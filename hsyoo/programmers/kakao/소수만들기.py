from itertools import combinations
import math

def solution(nums):
    answer = 0
    sum_ = sum(nums)
    ary = [True] * (sum_ + 1)
    for i in range(2, int(math.sqrt(sum_))+1):
        j = 2
        while i * j < sum_+1:
            ary[i*j] = False
            j += 1
    comb = list(combinations(nums, 3))
    for case in comb:
        s = sum(case)
        if ary[s] == True:
            answer +=1
        
    return answer