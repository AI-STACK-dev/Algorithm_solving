import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(5)]
a = int(data[0] - data[1] / data[3])
b = int(data[0] - data[2] / data[4])
print(min(a,b))