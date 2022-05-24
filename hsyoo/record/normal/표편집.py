from collections import defaultdict
def solution(n, k, cmds):
    linked_list = {}
    for i in range(n):
        linked_list[i] = [i-1, i+1]
    answer = ['O' for i in range(n)]
    stack = []
    for cmd in cmds:

        temp = cmd.split()
        if len(temp) == 2:
            temp_cmd, step = temp[0], int(temp[1])
        else:
            temp_cmd = temp[0]
        if temp_cmd == 'U' or temp_cmd == 'D':
            if temp_cmd == 'U':
                for _ in range(step):
                    k = linked_list[k][0]
            else:
                for _ in range(step):
                    k = linked_list[k][1]
        elif temp_cmd == 'C':
            prev, next = linked_list[k]
            stack.append((k, prev, next))
            answer[k] = 'X'

            if next == n:
                k = prev
            else:
                k = next
                
            if prev == -1:
                linked_list[next][0] = prev
            elif next == n:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
        else:
            now, prev, next = stack.pop()
            answer[now] = 'O'

            if prev == -1:
                linked_list[next][0] = now
            elif next == n:
                linked_list[prev][1] = now
            else:
                linked_list[next][0] = now
                linked_list[prev][1] = now
        print(k, answer)
    return "".join(answer)

# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# print(solution(8, 2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))