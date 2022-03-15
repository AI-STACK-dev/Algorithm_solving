import sys; input = sys.stdin.readline;
data0 = [int(input()) for _ in range(4)]
data1 = [int(input()) for _ in range(2)]
x = sum(data0) - min(data0)
y = sum(data1) - min(data1)
print(x + y)