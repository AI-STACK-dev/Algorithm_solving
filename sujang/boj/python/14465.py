import sys; input = sys.stdin.readline

n,k,b = map(int,input().split())
broken = [0] * (n+1)

for _ in range(b):
    i = int(input())
    broken[i] = 1

for i in range(1,n+1):
    broken[i] += broken[i-1]

ans = b
for i in range(k,n+1):
    ans = min(ans, broken[i]-broken[i-k])
print(ans)