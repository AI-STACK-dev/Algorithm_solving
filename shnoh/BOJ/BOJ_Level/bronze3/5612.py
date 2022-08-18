import sys; input = sys.stdin.readline;
n = int(input())
m = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
Max = m
for a,b in data:
    m = m + a - b
    Max = max(Max, m)
    if m < 0:
        Max = 0
        break
print(Max)