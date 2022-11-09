import sys; input = sys.stdin.readline;
t = int(input())
data = list(map(int, input().split()))
print(sum(data) - max(data))