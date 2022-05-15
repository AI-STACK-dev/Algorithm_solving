import sys; input = sys.stdin.readline;
N = int(input())
data = list(map(int, input().split()))
Y = M = 0
for i in range(N):
    Y += 10 * (data[i] // 30 + 1)
    M += 15 * (data[i] // 60 + 1)
if Y > M:
    print('M', M)
elif Y == M:
    print('Y M', M)
else:
    print('Y', Y)