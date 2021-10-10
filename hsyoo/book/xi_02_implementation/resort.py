ary = list(input())
alpha = []
numer = []
for case in ary:
    if ord(case) >= 65 and ord(case) <= 91:
        alpha.append(case)
    else:
        numer.append(case)
alpha.sort()
resort = alpha[0]
for case in alpha[1:]:
    resort += case
print(resort+str(sum(map(int,numer))))