from collections import deque

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    ary = list(map(int, input().split()))
    q = deque()
    for idx, case in enumerate(ary):
        if idx == m:
            q.append((case, True))
        else:
            q.append((case, False))
    cnt = 1
    while q:
        num, bin = q.popleft()

        if len(q) != 0:
            max_num = max(q, key = lambda x : x[0])[0]
        else:
            print(cnt)
            break

        if num < max_num:
            q.append((num, bin))
        else:
            if bin == True:
                print(cnt)
                break
            else:
                cnt +=1
    
        