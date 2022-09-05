import sys; input = sys.stdin.readline;
data = input().rstrip()
n = len(data)
start = n % 3
for i in range(n):
    print(data[i], end = '')
    if (i + 1) % 3 == start and i != (n - 1):
        print(',', end = '')