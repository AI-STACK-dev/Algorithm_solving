import sys; input = sys.stdin.readline;
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))
res = 0
for i in range(3):
    res += max(data2[i] - data1[i], 0)
print(res)