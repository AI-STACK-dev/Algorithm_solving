n = int(input())
ary = list(map(int, input().split()))
s = int(input())
sorted_index = 0

while s != 0:
    if sorted_index == n:
        break
    tail = ary[sorted_index:]
    max_index = tail.index(max(tail))
    if s >= max_index:
        for j in range(sorted_index + max_index, sorted_index, -1):
            ary[j], ary[j-1] = ary[j-1], ary[j]
            s -= 1
        sorted_index += 1
    else:
        residue = ary[sorted_index:sorted_index + s+1]
        max_index = residue.index(max(residue))
        if ary[sorted_index + max_index] == ary[sorted_index]:
            sorted_index += 1
        else:
            ary[sorted_index + max_index], ary[sorted_index + max_index - 1] = ary[sorted_index + max_index-1], ary[sorted_index + max_index]
            s -= 1
    # print(ary, sorted_index, s)

for case in ary:
    print(case, end = ' ')
print()
        
