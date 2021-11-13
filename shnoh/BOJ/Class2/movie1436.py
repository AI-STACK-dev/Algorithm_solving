import sys
n = int(sys.stdin.readline())
cnt = 0
k = 666
while True:
    if '666' in str(k):
        cnt += 1
        if cnt == n:
            break
    k += 1
print(k)