n = int(input())
list_ = []
for _ in range(n):
    name, kor, eng, mat = input().split()
    kor, eng, mat = int(kor), int(eng), int(mat)
    list_.append((name, kor, eng, mat))

list_.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for item in list_:
    print(item[0])