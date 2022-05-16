from bisect import bisect_left, bisect_right
from operator import itemgetter

class CountIntervals:
    def __init__(self):
        self.interval = []
        self.cur_count = 0
    
    def add(self, left, right):
        interval = self.interval
        if not interval:
            interval.append((left, right))
            self.cur_count += right - left + 1
        else:
            # l = bisect_left(interval, left-1, key = lambda x : x[1])
            l = bisect_left(interval, left-1, key = itemgetter(1))
            lval = left
            if l < len(interval):
                lval = min(interval[l][0], lval)
            # r = bisect_right(interval, right + 1, key = lambda x : x[0])
            r = bisect_right(interval, right + 1, key = itemgetter(0))
            rval = right
            if r > 0:
                rval = max(interval[r - 1][1], rval)
            to_delete = 0
            for i in range(l, r):
                to_delete += interval[i][1] - interval[i][0] + 1
            self.cur_count += rval - lval + 1 - to_delete
            interval[l:r] = [(lval, rval)]

    def count(self):
        return self.cur_count

obj = CountIntervals()
obj.add(2,3)
obj.add(7,10)
print(obj.count())
obj.add(5, 8)
print(obj.count())