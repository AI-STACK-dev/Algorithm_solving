tc = int(input())
for _ in range(tc):
    a,b = input().split()
    ans = ''
    for s in b:
        ans += s*int(a)
    print(ans)