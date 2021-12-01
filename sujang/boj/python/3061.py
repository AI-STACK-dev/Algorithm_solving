import sys; input = sys.stdin.readline

tc = int(input().rstrip())
for _ in range(tc):
    n = int(input().rstrip())
    ans = 0
    temp = [0]*n
    for d in list(map(int,input().rstrip().split())):
        ans += sum(temp[d-1:])
        temp[d-1] = 1
    print(ans)