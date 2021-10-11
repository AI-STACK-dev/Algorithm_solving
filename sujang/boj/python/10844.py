from sys import stdin

n = int(stdin.readline())
ans = [0]+[1]*9
for _ in range(1,n):
    temp = [0]*10
    for i in range(10):
        if i == 0:
            temp[i] = ans[1]
        elif i == 9:
            temp[i] = ans[8]
        else:
            temp[i] = ans[i-1]+ans[i+1]
    ans = temp
print(sum(ans)%1000000000)
