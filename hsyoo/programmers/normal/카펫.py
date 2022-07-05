# def solution(brown, yellow):
#     answer = []
#     n = 2
#     while True:
#         m = n
#         print(m,n)
#         while True:
#             if 2 * (m + n) == brown + 2 and m*n == yellow + brown:
#                 return [m, n]
#             if 2 * (m + n) > brown + 2:
#                 break
#             m += 1
#         n += 1
        
        
#     return answer

def solution(brown, yellow):
    answer = []
    total = brown + yellow                  # a * b = total
    for b in range(1,total+1):
        if (total / b) % 1 == 0:            # total / b = a
            a = total / b
            if a >= b:                      # a >= b
                if 2*a + 2*b == brown + 4:  # 2*a + 2*b = brown + 4 
                    return [a,b]
            
    return answer

print(solution(10, 2))