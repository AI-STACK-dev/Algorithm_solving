import sys; input = sys.stdin.readline

s = list(input().rstrip())

count0 = count1 = 0

if s[0] == '0':
    count1 += 1
else:
    count0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count1,count0))