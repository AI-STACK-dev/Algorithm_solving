import sys; input = sys.stdin.readline;
ans = int(input())
data = list(map(int, input().split()))
cnt = 0
for num in data:
    if ans == num:
        cnt += 1
print(cnt)