## lambda expression

def add(a,b):
    return a + b

print(add(3,7))

print((lambda a,b : a+b)(3,7))

arr = [('harry', 50), ('lebeca', 32), ('hwanseung2', 74)]
def my_key(x):
    return x[1]

print(sorted(arr, key = my_key))
print(sorted(arr, key = lambda x : x[1], reverse = True))

## library

result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse = True)
print(f"result : {result}")
print(f"reverse result : {reverse_result}")

result = sorted(arr, key = lambda x : x[1], reverse = True)
print(f"result : {result}")

from itertools import permutations, combinations

data = ['a', 'b', 'c']
result = list(permutations(data, 3))
print(result)

result = list(combinations(data, 2))
print(result)

from itertools import product
result = list(product(data, repeat = 2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

import math

a = 21
b = 14
def lcm(a,b):
    return a*b//math.gcd(a,b)
print(math.gcd(21,14))
print(lcm(21,14))