import sys; input = sys.stdin.readline;
n = int(input())
cnt = 0
for _ in range(n):
    data = input().rstrip()
    k = len(data)
    for i in range(1,k):
        if data[i-1] == 'D' and data[i] == 'C':
            cnt += 1
            break
print(n - cnt)