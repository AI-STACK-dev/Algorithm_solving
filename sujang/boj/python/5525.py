import sys; input = sys.stdin.readline
n = int(input())
m  = int(input())
data = input().rstrip()

isSeq = False
count = []
curr = 0
for i in range(1,len(data)-1):
    if data[i-1] == "I" and data[i] == "O" and data[i+1]=="I":
        isSeq = True
        curr +=1
    elif data[i-1] == "O" and data[i] == "I" and data[i+1]=="O":
        continue

    elif isSeq and curr != 0:
        count.append(curr)
        isSeq = False
        curr = 0
if curr != 0:
    count.append(curr)

ans = 0
for c in count:
    if c >= n :
        ans += c-n+1
print(ans)
