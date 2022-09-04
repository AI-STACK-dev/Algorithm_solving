import sys; input = sys.stdin.readline;
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
cntA = 0
cntB = 0
for a,b in data:
    if a>b:
        cntA += 1
    elif b>a:
        cntB += 1
print(cntA, cntB)