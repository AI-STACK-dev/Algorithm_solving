ary = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(ary)):
    min_idx = i
    for j in range(i+1, len(ary)):
        if ary[min_idx] > ary[j]:
            min_idx = j
    ary[i], ary[min_idx] = ary[min_idx], ary[i]

print(ary)