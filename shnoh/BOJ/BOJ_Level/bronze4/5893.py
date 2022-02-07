import sys; input = sys.stdin.readline;
data = input().rstrip()
decimal = 0
n = len(data)
two = 1
for i in range(n - 1, -1, -1):
    decimal += int(data[i]) * two
    two *= 2
decimal *= 17
data2 = []
while decimal > 0:
    data2.append(decimal % 2)
    decimal = decimal // 2
data2.reverse()
print(*data2, sep = "")
