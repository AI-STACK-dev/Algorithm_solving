"""s = str(input())
num = ''
minus = False
result = 0
temp = 0
for case in s:
    # print(temp)
    if case.isdigit():
        num = num + case
    else:
        num = int(num)
        if case == '-' and minus == False:
            print(1)
            temp += num
            minus = True
        elif case == '-' and minus == True:
            print(2)
            result -= temp
            temp = 0
            minus = True
        elif case == '+' and minus == False:
            print(3)
            result += num
        else:
            print(4)
            temp += num
        num=''
print(result)
            
"""
ary = input().split('-')
result = 0
for i in ary[0].split('+'):
    result += int(i)
for i in ary[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)