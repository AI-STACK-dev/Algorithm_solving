"""from copy import deepcopy
from bisect import bisect_left, bisect_right

def solution(n, k, cmds):
    delete_ = []

    for cmd in cmds:
        temp = cmd.split()
        if len(temp) == 2:
            tmp_cmd, step = temp[0], temp[1]
        else:
            tmp_cmd = temp[0]
        if tmp_cmd == 'D' or tmp_cmd == 'U':
            sorted_delete = deepcopy(sorted(delete_))
            if tmp_cmd == 'D':
                # k += int(step)
                #k부터 k + step까지 delete안 에 갯수
                right_ = bisect_right(sorted_delete, k+int(step))
                left_ = bisect_left(sorted_delete, k)
                add_step = right_ - left_
                k = k + int(step) + add_step
            else:
                # k -= int(step)
                right_ = bisect_right(sorted_delete, k)
                left_ = bisect_left(sorted_delete, k-int(step))
                add_step = right_ - left_
                k = k - int(step) - add_step
        elif tmp_cmd == 'C':
            if k != (n-1):
                delete_.append(k)
                k+=1
            else:
                delete_.append(k)
                k-=1
        elif tmp_cmd == 'Z':
            num = delete_.pop()
            if num < k:
                k+=1
            else:
                continue
    set_ = set(delete_)
    answer = ''
    for i in range(n):
        if i in set_:
            answer += 'X'
        else:
            answer += 'O'
    return answer"""
from collections import defaultdict

def solution(n, k, cmds):
    linked_list = defaultdict(list)
    for i in range(n):
        linked_list[i] = [i-1, i+1]
    answer = ['O' for i in range(n)]
    stack = []

    for cmd in cmds:
        temp = cmd.split()
        if len(temp) == 2:
            tmp_cmd, step = temp[0], int(temp[1])
        else:
            tmp_cmd = temp[0]
        
        if tmp_cmd == 'U' or tmp_cmd == 'D':
            if tmp_cmd == 'U':
                for _ in range(step):
                    k = linked_list[k][0]
            else:
                for _ in range(step):
                    k = linked_list[k][1]
        elif tmp_cmd == 'C':
            # k, prev, next 순
            prev = linked_list[k][0]
            next = linked_list[k][1]
            answer[k] = 'X'
            stack.append((k, prev, next))

            if next == n:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]
            
            if prev == -1:
                linked_list[next][0] = prev
            elif next == n:
                linked_list[prev][1] = next
            else:
                linked_list[next][0] = prev
                linked_list[prev][1] = next

            
        elif tmp_cmd == 'Z':
            now, prev, next = stack.pop()
            answer[now] = 'O'
            if prev == -1:
                linked_list[next][0] = now
            elif next == n:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(answer)
    

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))