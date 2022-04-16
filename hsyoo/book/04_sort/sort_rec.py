### 선택정렬, 삽입정렬, 퀵정렬, 계수정렬

ary = [7,5,9,0,3,1,6,2,4,8]
length = len(ary)
def selection_sort(ary, length):
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if ary[j] < ary[min_index]:
                min_index = j
        ary[min_index], ary[i] = ary[i], ary[min_index]
    return ary

def insertion_sort(ary, length):
    for i in range(1, length):
        for j in range(i, 0, -1):
            if ary[j] < ary[i]:
                ary[j], ary[i] = ary[i], ary[j]
            else:
                break
    return ary

def quick_sort(ary):
    if len(ary) == 1:
        return ary
    pivot = ary[0]
    tail = ary[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x> pivot]
    return left_side + [pivot] + right_side

def count_sort(ary):
    max_ = max(ary)
    count = [0] * (max_+1)
    for num in ary:
        count[num] += 1
    
    sorted_ary = []
    for i in range(max_+1):
        for j in range(count[i]):
            sorted_ary.append(i)
    return sorted_ary

print(selection_sort(ary, length))
print(insertion_sort(ary, length))
print(quick_sort(ary))
print(count_sort(ary))