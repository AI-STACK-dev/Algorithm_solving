ary = input()
ary_ = []
for idx in range(len(ary)-1, -1, -1):
    ary_.append(int(ary[idx]))

pre = ary_[0]
for case in ary_[1:]:
    if str(case) in ['0', '1']:
        pre += case
    else:
        pre *= case
print(pre)