import sys; input = sys.stdin.readline;
ori = [1,1,2,2,2,8]
data = list(map(int, input().split()))
for i in range(6):
    data[i] = ori[i] - data[i]
print(*data)