import sys; input = sys.stdin.readline;
data = [1] * 100
for i in range(2, 101):
    data[i - 1] = data[i - 2] + i ** 2
while True:
    k = int(input())
    if not k:
        break
    print(data[k - 1])