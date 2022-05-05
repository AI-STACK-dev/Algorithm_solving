from itertools import permutations
def solution(n, weak, dist):
    N = len(weak)
    for i in range(N):
        weak.append(weak[i]+n)
    
    ans = len(dist) + 1
    
    for i in range(N):
        for lis in permutations(dist,len(dist)):
            cnt = 1
            pos = weak[i] + lis[cnt-1]
            for j in range(i, i+N):
                if pos < weak[j]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[j] + lis[cnt-1]
            ans = min(ans, cnt)
    
    if ans == len(dist) + 1:
        return -1
    return ans