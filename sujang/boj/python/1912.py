import sys;input = sys.stdin.readline

n = int(input().rstrip())
data = list(map(int,input().rstrip().split()))

ans = [-int(1e9)]*(n+1)
for i in range(1,n+1):
    ans[i] = max(data[i-1], ans[i-1]+data[i-1])

print(max(ans))