n = input()
temp = [0] * 10
for i in n:
    i = int(i)
    if i == 6 or i == 9:
        if temp[6] > temp[9]:
            temp[9] += 1
        else:
            temp[6] += 1
    else:
        temp[i] += 1
print(max(temp))
