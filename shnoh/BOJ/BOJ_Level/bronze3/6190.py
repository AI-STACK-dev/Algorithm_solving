import sys; input = sys.stdin.readline;
N = int(input())
cnt = 0
while N != 1:
    if N % 2:
        N  = N * 3 + 1
    else:
        N /= 2
    cnt += 1
print(cnt)