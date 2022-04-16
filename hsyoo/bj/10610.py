ary = list(input())
sum_ = 0
ary.sort(reverse = True)
for case in ary:
    sum_ += int(case)
if '0' not in ary or sum_ % 3 != 0:
    print(-1)
else:
    print(''.join(ary))