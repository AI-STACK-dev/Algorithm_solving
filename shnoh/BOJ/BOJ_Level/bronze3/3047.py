import sys; input = sys.stdin.readline;
data = list(map(int, input().split()))
data.sort()
order = input().rstrip()
for c in order:
    print(data[ord(c) - 65], end=' ')