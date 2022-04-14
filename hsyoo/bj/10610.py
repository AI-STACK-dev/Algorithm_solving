"""from collections import Counter
n = str(input())
length = len(n)
c1 = Counter(n)
start = (int(10**length) // 30) * 30
end = (int(10 ** (length - 1)) // 30) * 30

flag = 1
for i in range(start, end, -30):
    if Counter(str(i)) == c1:
        print(i)
        flag = 0
        break
if flag == 1:
    print(-1)


"""
n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))