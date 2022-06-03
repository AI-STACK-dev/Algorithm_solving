#이진 트리에서 조건에 따라 순회 가능한 모든 경우의 수를 탐색하면서 최대 양의 개수를 구하면 정답.
from collections import defaultdict, deque
from copy import deepcopy

is_wolf = []
num2edges = defaultdict(list)
max_sheep = 0

def find_max_recursive(current_loc, used, nsheep, nwolf, can_go):
    global max_sheep

    if used[current_loc]:
        return
    used[current_loc] = True
    if is_wolf[current_loc]:
        nwolf += 1
    else:
        nsheep += 1
        max_sheep = max(max_sheep, nsheep)
    
    if nsheep <= nwolf:
        return
    
    can_go.extend(num2edges[current_loc]) # 현재 노드와 연결된 노드를 추가함
    for next_loc in can_go:
        find_max_recursive(next_loc, deepcopy(used), nsheep, nwolf, 
        can_go = [loc for loc in can_go if loc != next_loc and not used[loc]])

def solution(info, edges):
    global is_wolf, num2edges, max_sheep
    is_wolf = info #양과 늑대를 기록한 리스트
    used = [False] * len(is_wolf) # 방문한 노드 확인

    for edge in edges:
        parent, child = edge
        num2edges[parent].append(child)
    
    find_max_recursive(0, used, 0, 0, [])
    return max_sheep