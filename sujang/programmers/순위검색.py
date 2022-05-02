from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    repo = defaultdict(list)
    # make repo
    for i in info:
        data = i.split()
        resume = data[:-1]
        score = data[-1]
        for j in range(5):
            listToMask = combinations([0,1,2,3],j)
            for k in listToMask:
                temp = resume.copy()
                for l in k:
                    temp[l] = "-"
                key = " ".join(temp)
                repo[key].append(int(score))
    
    for vs in  repo.values():
        vs.sort()
    
    # find answer
    ans = []
    for q in query:
        q = q.replace("and ", "").split()
        score = q[-1]
        qq = " ".join(q[:-1])
        answer = 0
        if qq in repo:
            temp = repo[qq]
            answer = len(temp) - bisect_left(temp, int(score))
        ans.append(answer)
    return ans
