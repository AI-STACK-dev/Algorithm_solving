import sys; input = sys.stdin.readline;
data = []
while True:
    k = float(input())
    if k == 999:
        break
    data.append(k)
n = len(data)
for i in range(n - 1):
    res = data[i + 1] - data[i]
    print(f'{res:.2f}')