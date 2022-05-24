n = int(input())

row = [0] * n
ans = 0

def is_promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[i] - row[x]) == abs(x - i):
            return False
    return True
def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    for i in range(n):
        row[x] = i
        if is_promising(x):
            n_queens(x+1)

n_queens(0)
print(ans)