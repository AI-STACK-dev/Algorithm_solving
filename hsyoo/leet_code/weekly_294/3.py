# class Solution:
#     def minimumLines(self, stockPrices):
#         stockPrices.sort()
#         print(stockPrices)
#         n = len(stockPrices)
#         if n == 1:
#             return 0
#         x1, y1 = stockPrices[0]
#         x2, y2 = stockPrices[1]
#         pre_grad = (y2 - y1) / (x2 - x1)
#         answer = 1
#         for i in range(2, n):
#             x1,y1 = stockPrices[i-1]
#             x2,y2 = stockPrices[i]
#             grad = (y2 - y1) / (x2 - x1)
#             print(pre_grad, grad)
#             if pre_grad != grad:
#                 answer += 1
#             pre_grad = grad
#         return answer 

class Solution:
    def minimumLines(self, stockPrices) -> int:
        # key point: never use devision to judge whether 3 points are on a same line or not, use the multiplication instead !!
        
        n = len(stockPrices)
        stockPrices.sort(key = lambda x: (x[0], x[1]))
        
        if n == 1:
            return 0
        
        pre_delta_y = stockPrices[0][1] - stockPrices[1][1]
        pre_delta_x = stockPrices[0][0] - stockPrices[1][0]
        num = 1
        
        for i in range(1, n-1):
            cur_delta_y = stockPrices[i][1] - stockPrices[i+1][1]
            cur_delta_x = stockPrices[i][0] - stockPrices[i+1][0]
            
            if pre_delta_y * cur_delta_x != pre_delta_x * cur_delta_y:
                num += 1
                pre_delta_x = cur_delta_x
                pre_delta_y = cur_delta_y
        
        return num

# print(Solution().minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1],[9,-5]]))
print(Solution().minimumLines([[3,4],[1,2],[7,8],[2,3]]))
# print(Solution().minimumLines([[1,1],[3,3],[2,2]]))
# print(Solution().minimumLines([[1,1],[2,3],[3,1],[4,3], [5,1], [6,3]]))