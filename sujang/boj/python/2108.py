import sys; input = sys.stdin.readline

n = int(input())

SUM = 0
MAX = -int(1e9)
MIN = int(1e9)
MED = 1000
MOD = 1000

arr = [0]*8001

# n번
for _ in range(n):
    num = int(input())
    SUM += num
    arr[num+4000] += 1
    if num > MAX:
        MAX = num
    if num < MIN:
        MIN = num

cnt = mm = 0
isOnce = False

for i in range(MIN+4000, MAX+4001):
    if arr[i] > 0:
        if cnt < ((n+1)//2):
            cnt += arr[i]
            MED = i - 4000
        
        if mm < arr[i]:
            mm = arr[i]
            MOD = i-4000
            isOnce = True
        elif mm == arr[i] and isOnce == True:
            MOD = i-4000
            isOnce = False

print(round(SUM/n))  
print(MED)
print(MOD)
print(MAX-MIN)