import sys

N, M = map(int, sys.stdin.readline().split())
data = [int(x) for x in sys.stdin.readline().split()]
DP = [0]*100001
for i in range(1, N+ 1):
    DP[i] = DP[i - 1] + data[i - 1]
for _ in range(M):
    I, J = map(int, sys.stdin.readline().split())
    print(DP[J] - DP[I-1])