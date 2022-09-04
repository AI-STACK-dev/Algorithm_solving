ary = [5 ,7, 9,0,3,1,6,2,4,8]

def quick_sort(ary):
    if len(ary) <= 1:
        return ary

    pivot = ary[0]
    tail = ary[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(ary))