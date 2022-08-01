import sys; input = sys.stdin.readline;
n = int(input())
data = [list(input().rstrip()) for _ in range(n)]
for i in range(n):
    if ord(data[i][0]) > 96:
        data[i][0] = chr(ord(data[i][0]) - 32)
    print("".join(data[i]))