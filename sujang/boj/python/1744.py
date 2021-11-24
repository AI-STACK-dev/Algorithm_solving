import sys; input = sys.stdin.readline

n = int(input().rstrip())

pos = []
neg = []
for _ in range(n):
    num = int(input().rstrip())
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)
pos.sort(reverse=True)
neg.sort()

ans = 0
i = 0
while i < len(pos):
    if i == len(pos)-1:
        ans += pos[i]
    else:
        if pos[i] == pos[i]*pos[i+1]:
            ans += pos[i]
        else:
            ans += pos[i]*pos[i+1]
            i+=1
    i +=1

i = 0
while i < len(neg):
    if i == len(neg)-1:
        ans += neg[i]
    else:
        ans += max(neg[i],neg[i]*neg[i+1])
        i+=1
    i +=1
print(ans)
