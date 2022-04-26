from collections import deque

def solution(n,s):
    s.sort()
    q = deque(s)
    temp = []

    for i in range(1,n+1):
        div = 0
        while q and q[0] <= i:
            if i == q[0]:
                div += 1
            q.popleft()

        a,b = div, len(q)+div
        if b == 0:
            a,b = 0,1
        temp.append([i, a/b])
    
    temp.sort(key=lambda x: (-x[1], x[0]))

    ans = []
    for a,b in temp:
        ans.append(a)
    return ans
