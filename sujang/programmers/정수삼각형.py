def solution(t):
    n = len(t)
    for i in range(1,n):
        for j in range(i+1):
            if j == 0:
                t[i][j] += t[i-1][j]
            elif j == i:
                t[i][j] += t[i-1][j-1]
            else:
                t[i][j] += max(t[i-1][j-1], t[i-1][j])
    return max(t[-1])