import sys; input = sys.stdin.readline;
data = list(map(int, input().split()))
data.sort()
print(data[0] * data[2])