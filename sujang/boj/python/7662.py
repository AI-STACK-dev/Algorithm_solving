import sys; input = sys.stdin.readline
import heapq as hp

n = int(input())
for _ in range(n):
    m = int(input())
    visited = [False]*1000001
    maxh = []
    minh = []
    for i in range(m):
        cmd = input().rstrip().split()
        if cmd[0] == "I":
            num = int(cmd[1])
            hp.heappush(maxh,(-num,i))
            hp.heappush(minh,(num,i))
            visited[i] = True
        elif cmd[1] =='1':
            while maxh and not visited[maxh[0][1]]:
                hp.heappop(maxh)
            if maxh:
                visited[maxh[0][1]] = False
                hp.heappop(maxh)
        else:
            while minh and not visited[minh[0][1]]:
                hp.heappop(minh)
            if minh:
                visited[minh[0][1]] = False
                hp.heappop(minh)
    while maxh and not visited[maxh[0][1]]:
        hp.heappop(maxh)
    while minh and not visited[minh[0][1]]:
        hp.heappop(minh)
    if maxh and minh:
        print(-maxh[0][0],minh[0][0])
    else:
        print("EMPTY")
