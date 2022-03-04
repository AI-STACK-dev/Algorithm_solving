import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(5)]
a = min(data[0], data[1], data[2])
b = min(data[3], data[4])
print(a + b - 50)