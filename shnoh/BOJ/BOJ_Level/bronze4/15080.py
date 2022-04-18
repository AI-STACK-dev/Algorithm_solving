import sys; input = sys.stdin.readline;
data1 = list(map(int, input().rstrip().split(' : ')))
data2 = list(map(int, input().rstrip().split(' : ')))
start = end = 0
for i in range(3):
    start += data1[i] * 60 ** (2 - i)
    end += data2[i] * 60 ** (2 - i)
res = end - start
if res < 0:
    res += 24 * 3600
print(res)