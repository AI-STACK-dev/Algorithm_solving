from collections import Counter
string = input().upper()
a = dict(Counter(string))
max_ = max(a.values())
b = []
for k,v in a.items():
    if v == max_:
        b.append(k)
if len(b) > 1:
    print('?')
else:
    print(b[0])
