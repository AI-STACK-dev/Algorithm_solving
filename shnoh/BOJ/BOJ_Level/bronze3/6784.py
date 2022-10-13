import sys; input = sys.stdin.readline;
n = int(input())
stu = [input().rstrip() for _ in range(n)]
ans = [input().rstrip() for _ in range(n)]
cnt = 0
for i in range(n):
    if stu[i] == ans[i]:
        cnt += 1
print(cnt)