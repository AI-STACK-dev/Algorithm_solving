import sys; input = sys.stdin.readline;
t = int(input())
cnt = 0
data = [list(map(float, input().split())) for _ in range(t)]
for bag in data:
    if ((bag[0] <= 56 and bag[1] <= 45 and bag[2] <= 25) or bag[0] + bag[1] + bag[2] <= 125 ) and bag[3] <= 7:
        cnt += 1
        print(1)
    else:
        print(0)
print(cnt)