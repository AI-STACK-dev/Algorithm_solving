import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
data = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

def dfs(s):
    for i in data[s]:
        if parents[i] == 0:
            parents[i] = s
            dfs(i)

dfs(1)

print(*parents[2:], sep ='\n')
