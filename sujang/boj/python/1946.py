import sys; input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]
    data = sorted(data,key=lambda x :x[0])
    
    prev = int(1e9)
    ans = 0
    for _, b in data:
        if b < prev:
            ans += 1
            prev = b
    print(ans)
    