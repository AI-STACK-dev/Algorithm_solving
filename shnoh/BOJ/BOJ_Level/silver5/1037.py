import sys; input = sys.stdin.readline;
input()
data = list(map(int, input().split()))
data.sort()
print(data[0] * data[-1])