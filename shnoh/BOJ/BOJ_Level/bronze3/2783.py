import sys; input = sys.stdin.readline;
data = [list(map(int, input().split()))]
n = int(input())
for _ in range(n):
    data.append(list(map(int, input().split())))
Min = 100
for x, y in data:
    Min = min(Min, x / y)
print(f'{Min * 1000:.2f}')