import sys; input = sys.stdin.readline;
data1 = list(map(int, input().split(":")))
data2 = list(map(int, input().split(":")))
data3 = []
k1 = k2 = 0
data3 = []
k1 = (data1[0] * 60 + data1[1]) * 60 + data1[2]
k2 = (data2[0] * 60 + data2[1]) * 60 + data2[2]
res = k2 - k1
if res <= 0:
    res += 24 * 60 * 60
data3.append(res % 60)
res = res // 60
data3.append(res % 60)
data3.append(res // 60)
for i in range(3):
    if data3[i] < 10:
        data3[i] = str(data3[i]).zfill(2)
print(f'{data3[2]}:{data3[1]}:{data3[0]}')