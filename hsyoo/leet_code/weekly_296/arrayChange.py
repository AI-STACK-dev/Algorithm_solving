from collections import defaultdict

class Solution:
    def arrayChange(self, nums, operations):
        db = defaultdict(int)
        for idx, num in enumerate(nums):
            db[num] = idx
        for op in operations:
            idx = db[op[0]]
            nums[db[op[0]]] = op[1]
            db[op[1]] = idx

        return nums

print(Solution().arrayChange([1,2,4,6], [[1,3],[4,7],[6,1]]))
print(Solution().arrayChange([1,2], [[1,3],[2,1],[3,2]]))