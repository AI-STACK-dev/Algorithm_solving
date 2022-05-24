# from collections import defaultdict, deque

# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return 5 * (len(cities))
#     answer = 0
#     linked_list = defaultdict(list)
#     q = deque([])
#     head, tail = None, None
#     for city in cities:
#         city = city.lower()
#         if city in q:
#             prev, next = linked_list[city]
#             answer += 1
#             if city == head:
#                 continue
#             elif city == tail:
#                 q.remove(city)
#                 q.appendleft(city)
#                 linked_list[prev][1] = None
#                 tail = prev
#                 linked_list[city] = [None, head]
#                 linked_list[head][0] = city
#                 head = city
#             else:
#                 q.remove(city)
#                 q.appendleft(city)
#                 linked_list[prev][1] = next
#                 linked_list[next][0] = prev
#                 linked_list[city] = [None, head]
#                 linked_list[head][0] = city
#                 head = city
#         else:
#             answer += 5
#             if len(q) == 0:
#                 q.appendleft(city)
#                 head, tail  = city, city
#                 linked_list[city] = [None, None]
#             elif 0 < len(q) < cacheSize:
#                 q.appendleft(city)
#                 linked_list[city] = [None, head]
#                 linked_list[head][0] = city
#                 head = city
#             else:
#                 q.pop()
#                 q.appendleft(city)
#                 if cacheSize == 1:
#                     head, tail = city, city
#                     linked_list[city] = [None, None]
#                 else:
#                     tail = linked_list[tail][0]
#                     linked_list[tail][1] = None
#                     linked_list[city] = [None, head]
#                     linked_list[head][0] = city
#                     head = city

#     cur = head
#     while cur != None:
#         print(cur)
#         cur = linked_list[cur][1]
#     return answer

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]	))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	))
print(solution(1, ['seoul', 'la', 'seoul', 'la']))