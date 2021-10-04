input_ = input()
temp_col = input_[0]
row = int(input_[1]) - 1
col_dict = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
col = int(col_dict[temp_col])
case_list = []
cnt = 0
for a in [-2, 2]:
    for b in [-1, 1]:
        case_list.append((row-a, col - b))
        case_list.append((row - b, col - a))
for case in case_list:
    if case[0] < 0 or case[0] > 7:
        cnt +=1
    elif case[1] < 0 or case[1] > 7:
        cnt +=1

            
print(8 - cnt)