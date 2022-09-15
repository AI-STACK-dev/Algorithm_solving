import sys; input = sys.stdin.readline;
n = int(input())
bx, by = map(int, input().split())
for _ in range(n):
    lx, ly, hx, hy = map(int, input().split())
    if lx <= bx and bx <= hx and ly <= by and by <= hy:
        print("Yes")
        quit()
print("No")