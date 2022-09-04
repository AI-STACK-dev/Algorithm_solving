# U: 현재 선택된 행에서 X칸 위 (앞)
# D: 아래 칸 선택.
# C: 지금꺼 삭제하고 바로 아래꺼 행 선택. 만약 맨 마지막이면(linked list next가 none이면 prev를 선택)
# Z: 최근꺼를 다시 되돌린다. -> temp의 next와 prev를 이용하여 껴놓고 next와 prev 노드를 껴넣은애랑 연결한다.
# python은 링크드리스트를 해시로 구현할 수 있음. 마지막 리턴은 for문(n) 돌면서 key가 none인지, 아닌지를 구분하면서 answer return

from collections import defaultdict

def solution(n, k, cmds):
    answer= ['O' for i in range(n)]
    stack = []
    linked = defaultdict(list)
    for i in range(n):
        linked[i] = [i-1, i+1]
    cur = k
    for command in cmds:
        if len(command) > 1:
            cmd, x = command.split()
            x = int(x)
        elif len(command) == 1:
            cmd = command
        
        if cmd == 'U':
            for i in range(x):
                cur = linked[cur][0]
        elif cmd == 'D':
            for i in range(x):
                cur = linked[cur][1]
        elif cmd == 'C':
            prev = linked[cur][0]
            next = linked[cur][1]
            answer[cur] = 'X'
            stack.append((cur, prev, next))

            if next == n:
                cur = linked[cur][0]
            else:
                cur = linked[cur][1]
            
            if prev == -1:
                linked[next][0] = prev
            elif next == n:
                linked[prev][1] = next
            else:
                linked[next][0] = prev
                linked[prev][1] = next

        elif cmd == 'Z':
            now, prev, next = stack.pop()
            answer[now] = 'O'
            if prev == -1:
                linked[next][0] = now
            elif next == n:
                linked[prev][1] = now
            else:
                linked[next][0] = now
                linked[prev][1] = now
    return ''.join(answer)
    
    # result = []
    # cur = head
    # while cur != None:
    #     result.append(cur)
    #     cur = linked[cur][1]

    # set_ = set(result)
    # for i in range(n):
    #     if i in set_:
    #         answer += 'O'
    #     else:
    #         answer += 'X'
    # return answer
 
print(solution(8,2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	))
print(solution(8,2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	))