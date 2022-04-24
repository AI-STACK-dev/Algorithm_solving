import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(3)]
res = data[0] + data[1] * 2 + data[2] * 3
if res >= 10:
    print("happy")
else:
    print("sad")