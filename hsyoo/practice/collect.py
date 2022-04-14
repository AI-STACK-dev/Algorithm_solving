from collections import Counter, defaultdict, deque

list_ = [1,2,3,1,2,2,3,2,3,4,1,23,5,6,4,3,23,6]
counter = Counter(list_)

print(counter[1])
print(counter.most_common(10))

name_dict = defaultdict()
name_dict['con'] = 1
print(name_dict)