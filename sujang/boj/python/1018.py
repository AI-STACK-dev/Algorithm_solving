from sys import stdin

n,m = map(int,stdin.readline().rstrip().split())
data = [list(stdin.readline().rstrip()) for _ in range(n)]

ans = []
for i in range(n-7):
    for j in range(m-7):
        w_0 = 0
        b_0 = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2 ==0:
                    if data[k][l] =='B':
                        w_0 += 1
                    else:
                        b_0 += 1
                else:
                    if data[k][l] =='B':
                        b_0 += 1
                    else:
                        w_0 += 1
                        
        ans.extend([w_0,b_0])
print(min(ans))
