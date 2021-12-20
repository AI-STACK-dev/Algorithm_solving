import sys
input = sys.stdin.readline
n = int(input().rstrip())
cnt = 2
while True:
    if n == 1:
        break
    elif n % cnt == 0:
        print(cnt)
        n /= cnt
        cnt = 2
    else:
        cnt += 1
