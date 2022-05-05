from collections import defaultdict
def solution(gems):
    gemRepo = defaultdict(int)
    N,n = len(gems), len(set(gems))
    start,end = 0,0
    ansStart,ansEnd = 0,N-1
    # init
    gemRepo[gems[0]] += 1
    temp = 1
    # loop
    while True:
        if temp < n and end+1 < N:
            end += 1
            gemRepo[gems[end]] += 1
        elif temp == n:
            if end-start < ansEnd - ansStart:
                ansStart,ansEnd = start,end
            gemRepo[gems[start]] -= 1
            if gemRepo[gems[start]] == 0:
                del gemRepo[gems[start]]
            start += 1
        else:
            break
        temp = len(gemRepo.keys())
    
    return [ansStart+1,ansEnd+1]
