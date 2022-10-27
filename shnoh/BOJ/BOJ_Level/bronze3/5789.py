import sys; input = sys.stdin.readline;
n = int(input())
for _ in range(n):
    s = input().rstrip()
    k = len(s) // 2
    if s[k - 1] == s[k]:
        print("Do-it")
    else:
        print("Do-it-Not")