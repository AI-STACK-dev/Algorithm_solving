# 3x3 행렬 모든 원소 뒤집는 함수
def rev(X):
    Y = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if X[i][j] == 0:
                Y[i][j] = 1
    return Y

def solve(A,B,r,c):
    if A == B:
        return 0
    if r < 3 or c < 3:
        return -1
    count = 0
    for i in range(r-2):
        for j in range(c-2):
            if A[i][j] != B[i][j]:
                A_= [x[j:j+3] for x in a[i:i+3]]
                A_ = rev(A_)
                for x in range(3):
                    for y in range(3):
                        A[x+i][y+j]=A_[x][y]
                count += 1
    
    if A == B:
        return count
    else:
        return -1


r,c = map(int,input().split())
a = [[int(x) for x in input()] for _ in range(r)]
b = [[int(x) for x in input()] for _ in range(r)]
print(solve(a,b,r,c))