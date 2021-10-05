from collections import Counter
sum= 1
for i in range(3):
    sum *= int(input())
cnt = Counter(str(sum))
for i in range(10):
    try:
        print(cnt[str(i)])
    except:
        print('0')