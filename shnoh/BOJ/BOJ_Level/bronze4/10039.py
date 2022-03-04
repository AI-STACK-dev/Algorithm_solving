import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(5)]
for i in range(5):
    if data[i] < 40:
        data[i] = 40
print(sum(data) // 5)
