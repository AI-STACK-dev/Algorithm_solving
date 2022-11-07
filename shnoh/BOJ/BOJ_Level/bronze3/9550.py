import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    res = 0
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    for c in data:
        res += c // k
    print(res)