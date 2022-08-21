import sys; input = sys.stdin.readline;
t = int(input())
base = [350.34, 230.90, 190.55, 125.30, 180.90]
data = [list(map(int, input().split())) for _ in range(t)]
for t in data:
    res = 0
    for i in range(5):
        res += t[i] * base[i]
    print(f'${res:.2f}')