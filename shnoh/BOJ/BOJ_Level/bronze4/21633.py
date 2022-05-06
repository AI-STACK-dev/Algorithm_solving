import sys; input = sys.stdin.readline;
k = int(input())
res = 25 + k * 0.01
if res < 100:
    res = 100
elif res > 2000:
    res = 2000
print(f'{res:.2f}')