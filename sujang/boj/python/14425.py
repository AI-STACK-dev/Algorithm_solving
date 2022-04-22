import sys;input=sys.stdin.readline
n,m = map(int,input().split())
data = {}
for _ in range(n):
    s = input().rstrip()
    data[s] = 1

cnt = 0
for _ in range(m):
    s = input().rstrip()
    if s in data:
        cnt += 1
print(cnt)
