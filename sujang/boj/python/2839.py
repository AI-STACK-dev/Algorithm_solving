import sys; input = sys.stdin.readline

n = int(input().rstrip())

d = [int(1e9)]*(n+1)

for i in range(n+1):
    if i-3 == 0 or i-5 == 0:
        d[i] = 1
    if i > 5:
        d[i] = min(d[i], d[i-3] + 1,d[i-5]+1) 

if d[n] >= int(1e9):
    print(-1)
else:
    print(d[n])