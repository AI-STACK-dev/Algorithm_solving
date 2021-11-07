import sys
n , m = map(int, sys.stdin.readline().split())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))
# 일단 경우의 수는 64 * 64 * 64