import sys; input = sys.stdin.readline;
data = list(map(int, input().split()))
# x = data[0] / data[1]
# y = data[2] / data[3]

# res = x * y / 2
res = data[0] / data[1] * data[2] / data[3] / 2
if res == int(res):
    print(1)
else:
    print(0)