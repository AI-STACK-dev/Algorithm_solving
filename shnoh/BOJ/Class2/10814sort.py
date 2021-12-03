import sys; input = sys.stdin.readline
n = int(input().rstrip())
data = []
for _ in range(n):
    a, b = input().rstrip().split()
    data.append([int(a),b])
data.sort(key = lambda x: x[0])
for i in range(n):
    print(*data[i])
