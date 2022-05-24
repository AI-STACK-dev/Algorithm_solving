from collections import Counter
def solution(nums):
    n = len(nums)
    selec = n // 2
    c = Counter(nums)
    if len(c) >= selec:
        result = selec
    else:
        result = len(c)
    print(result)
    return result