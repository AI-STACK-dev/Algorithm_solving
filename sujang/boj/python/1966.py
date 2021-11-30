from collections import deque
import sys; input = sys.stdin.readline

tc = int(input().rstrip())
for _ in range(tc):
    n,m = map(int,input().rstrip().split())
    d = deque(list(map(int,input().rstrip().split())))
    dd = deque(list(range(n)))
    cnt = 1
    while d:
        MAX = max(d)
        tmp = d.popleft()
        idx = dd.popleft()
        if tmp == MAX:
            if idx == m:
                print(cnt)
                break
            cnt += 1
        else:
            d.append(tmp)
            dd.append(idx)
            

