class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        n = len(capacity)
        diff = [capacity[i] - rocks[i] for i in range(n)]
        diff.sort()
        sum_ = 0
        cnt = 0
        print(diff)
        for i in range(n):
            print(f"cnt : {cnt}, sum : {sum_}")
            sum_ += diff[i]
            cnt += 1 
            if sum_ > additionalRocks:
                cnt -= 1
                break
        
        return cnt
        

print(Solution().maximumBags([10,2,2], [2,2,0], 100)) # 3
print(Solution().maximumBags([2,3,4,5], [1,2,4,4], 2)) # 3
print(Solution().maximumBags([2,2,2,2,2,2], [2,2,2,2,2,2], 5)) # 6
print(Solution().maximumBags([91,54,63,99,24,45,78], [35,32,45,98,6,1,25],17)) # 6