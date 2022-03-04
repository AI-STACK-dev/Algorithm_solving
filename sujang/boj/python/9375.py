import sys; input = sys.stdin.readline

tc = int(input().rstrip())
for _ in range(tc):
    dic = {}
    n = int(input().rstrip())
    # dictionary에 저장
    for _ in range(n):
        a,b  = input().rstrip().split()
        if b in dic.keys():
            dic[b] += 1
        else:
            dic[b] = 2

    ans = 1    
    for v in dic.values():
        ans *= v
    print(ans-1)
