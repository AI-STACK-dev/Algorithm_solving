# def binary_search(ary, start, end):
#     print(ary, start, end)
#     mid = end
#     while start <= end and mid >= start:
#         mid = (start + end) // 2
#         print(mid)
#         if ary[mid] == True:
#             start = mid + 1
#         elif ary[mid] == False:
#             end = mid - 1
#     ary[mid] = True
#     return ary, mid

# def solution(k, room_numbers):
#     answer = []
#     check_space = [False] * (k+1)
#     for room_number in room_numbers:
#         if check_space[room_number] == False:
#             check_space[room_number] = True
#             answer.append(room_number)
#         else:
#             start, end = room_number + 1, k
#             check_space, mid = binary_search(check_space, start, end)
#             answer.append(mid)
#             break
#     return answer

import sys

sys.setrecursionlimit(10000000)
def find_empty_room(number, rooms):
    if number not in rooms:
        rooms[number] = number + 1
        return number
    else:
        empty = find_empty_room(rooms[number], rooms)
        rooms[number] = empty + 1
        return empty

def solution(k, room_number):
    answer = []
    rooms = dict()

    for number in room_number:
        print(rooms)
        empty_room = find_empty_room(number, rooms)
        answer.append(empty_room)
    return answer

print(solution(10, [1,3,4,1,3,1]))