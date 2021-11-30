import sys
input = sys.stdin.readline
n = int(input().rstrip())
data = [int(input().rstrip()) for _ in range(n)]
data.sort()
print(*data, sep = '\n')
