import sys; input = sys.stdin.readline

n,k = map(int,input().split())

ice = [0]*(1000001)
mx,mn = 0,int(1e9)
for _ in range(n):
    a,b = map(int,input().split())
    ice[b] = a
    mx = max(b,mx)
    mn = min(b,mn)


end = mn
curr = 0
ans = 0
for start in range(mn,mx+1):
    while end < mx+1 and end-start <= (2*k):
        if ice[end] != 0:
            curr += ice[end]
        end += 1
    ans = max(curr,ans)
    curr -= ice[start]

print(ans)
