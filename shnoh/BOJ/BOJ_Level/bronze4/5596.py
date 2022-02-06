import sys; input = sys.stdin.readline;
data = list(map(int, input().split()))
data2 = list(map(int, input().split()))
print(max(sum(data), sum(data2)))