import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    V, E = map(int, input().split())
    print(2 - V + E)