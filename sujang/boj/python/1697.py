from sys import stdin
from collections import deque

n,k = map(int,stdin.readline().rstrip().split())

visited = [0]*100001
def bfs():
    global n,k
    ans = 0
    d = deque([[n,ans]])
    while d:
        n,ans = d.popleft()
        if n == k:
            return ans
        if not visited[n]:
            visited[n] = 1
            if n+1 <= 100000:
                d.append([n+1,ans+1])
            if n-1 >= 0:
                d.append([n-1,ans+1])
            if n*2 <= 100000:
                d.append([n*2,ans+1])
    return ans

print(bfs())