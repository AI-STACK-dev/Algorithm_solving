import sys; input = sys.stdin.readline;
a,b,c,d = map(int, input().split())
data = list(map(int, input().split()))
for i in range(3):
    cnt = 0
    dog1 = data[i] % (a + b)
    if dog1 <= a and dog1 != 0:
        cnt += 1
    dog2 = data[i] % (c + d)
    if dog2 <= c and dog2 != 0:
        cnt += 1
    print(cnt)