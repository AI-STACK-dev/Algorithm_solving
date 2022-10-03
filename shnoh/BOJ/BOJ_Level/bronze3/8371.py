import sys; input = sys.stdin.readline;
n = int(input())
ori = input().rstrip()
rew = input().rstrip()
cnt = 0
for i in range(n):
    if ori[i] != rew[i]:
        cnt += 1
print(cnt)