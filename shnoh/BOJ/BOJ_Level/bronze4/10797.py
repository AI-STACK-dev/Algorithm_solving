import sys; input = sys.stdin.readline;
day = int(input())
data = list(map(int, input().split()))
cnt = 0
for num in data:
    if day == num:
        cnt += 1
print(cnt)