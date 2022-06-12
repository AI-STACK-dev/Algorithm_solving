import sys; input = sys.stdin.readline;
input()
data = list(map(int, input().split()))
cnt = 0
res = 0
for num in data:
    if num:
        cnt += 1
        res += cnt
    else:
        cnt = 0
print(res)