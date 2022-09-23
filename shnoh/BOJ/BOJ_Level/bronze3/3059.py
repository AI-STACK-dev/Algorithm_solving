import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    S = input().rstrip()
    setS = set(S)
    listS = list(setS)
    listS.sort()
    res = 2015
    for c in listS:
        res -= ord(c)
    print(res)