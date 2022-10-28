import sys; input = sys.stdin.readline;
k = int(input())
n = int(input())
cur = 0
for _ in range(n):
    t2, z = input().rstrip().split()
    t = int(t2)
    cur += t
    if cur > 210:
        break
    if z == 'T':
        k = (k + 1) % 8
    if not k:
        k = 8
print(k)