import sys; input = sys.stdin.readline
n,m = map(int, input().split())
data = list(map(int,input().split()))
data.sort()
ans = []

def recur(i):
    if i == m:
        print(*ans)
        return
    
    for j in range(n):
        if i == 0 or ans[i-1] <= data[j]:
            ans.append(data[j])
            recur(i+1)
            ans.pop()

recur(0)