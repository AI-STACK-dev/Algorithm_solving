import sys; input = sys.stdin.readline;
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
for t in data:
    k = str(bin(t[0]))
    cnt = 0
    for x in k:
        if x == '1':
            cnt += 1
    if cnt % 2 == t[1]:
        print("Valid")
    else:
        print("Corrupt")