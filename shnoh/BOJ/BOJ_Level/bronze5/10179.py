import sys; input = sys.stdin.readline;
n = int(input())
data = [float(input()) for _ in range(n)]
for i in range(n):
    print(f'${data[i] * 0.8:.2f}')