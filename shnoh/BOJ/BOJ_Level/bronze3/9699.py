import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    data = list(map(int, input().split()))
    print(f"Case #{i + 1}: {max(data)}")