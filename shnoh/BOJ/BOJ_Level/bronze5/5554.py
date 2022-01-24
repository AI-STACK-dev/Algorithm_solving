import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(4)]
sec = sum(data)
print(sec // 60)
print(sec % 60)