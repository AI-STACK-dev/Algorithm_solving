import sys; input = sys.stdin.readline;
data = list(map(int, input().split()))
data.sort()
x = data[0] + data[1]
if x <= data[2]:
    print(2 * x - 1)
else:
    print(sum(data))