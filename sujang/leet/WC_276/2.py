class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        incrementOP = 0
        doubleOP = 0
        while target != 1:
            if maxDoubles != 0:
                if target % 2 != 0:
                    target -= 1
                    incrementOP += 1
                target //= 2
                doubleOP += 1
                maxDoubles -= 1
            
            else:
                incrementOP += (target - 1) 
                target = 1
                
        return incrementOP + doubleOP
        