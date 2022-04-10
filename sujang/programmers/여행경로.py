from collections import deque

def solution(ts):
    # collections
    front, end = [], []
    routes = ["ICN"]
    # sort
    ts = sorted(ts, key = lambda x: (x[0], x[1]))
    # divide
    for a,b in ts:
        front.append(a)
        end.append(b)
    # deque
    fq, eq = deque(front), deque(end)
    # search
    while fq:
        a,b = fq.popleft(), eq.popleft()
        if a == routes[-1]:
            routes.append(b)
        else:
            fq.append(a)
            eq.append(b)
            
        if fq and routes[-1] not in fq:
            fq.append(routes[-2])
            eq.append(routes.pop())
            
    return routes


t = [["ICN","BOO"], ["ICN", "COO"], ["COO", "ICN"]]
print(solution(t))