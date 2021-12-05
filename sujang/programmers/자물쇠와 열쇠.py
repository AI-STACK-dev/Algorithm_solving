def rotate(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def check(new_lock):
    # check
    n = len(new_lock)//3
    for a in range(n,n*2):
        for b in range(n,n*2):
            if new_lock[a][b] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for _ in range(4):
        key = rotate(key)
        param = n-m+1
        for x in range(param,param+n+m-1):
            for y in range(param,param+n+m-1):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
                        
    return False

                