import sys; input = sys.stdin.readline

k = int(input().rstrip())
n = int(input().rstrip())

first = [ chr(ord('A')+i) for i in range(k)]
target = list(input().rstrip())
data = [ input().rstrip() for _ in range(n)]

# first data update
for i in range(n):
    d = data[i]
    if d[0] == '?':
        break
    j = 0
    while j < k-1:
        if d[j] == '-':
            first[j], first[j+1] = first[j+1],first[j]
            j += 1
        j+=1
idx = i

# target update
for j in range(n-1,idx,-1):
    d = data[j]
    l = 0
    while l < k-1:
        if d[l] == '-':
            target[l], target[l+1] = target[l+1],target[l]
            l += 1
        l+=1
# first, target done!

ans = ''
i = 0
while i < k-1:
    if first[i] != target[i]: 
        if first[i+1] != target[i+1]:
            ans += '-*'
            i += 1
        else:
            print('x'*(k-1))
            exit()
    else:
        ans += '*'
    i += 1
print(ans[:k-1])