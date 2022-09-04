# 음 bit wise 연산까지는 이해가 되는 상황.
# 근데 numbers의 길이가 10 5승, 그리고 bitwise 연산의 시간복잡도를 모르겠네..
# O(n^2)이면 당연히 풀 수 있음. 어라 서브 어레이는 배열 내에서 연속적.
# 이중 포문이라도 break문을 제대로 섞는다면 가능하지 않을까? 현재 index에서 length-1까지 돌아보다가 아니면 answer 바꾸기
# 어...라? 그러면 처음이랑 마지막도 &연산 해야하지않음? 
# 리스트에 담아야겠는데? 리스트에 담고 그 리스트를 돌아야할 것 같음.
# 그러면 결국 이중포문이 되는데, 큰 포문은 0부터 n-1까지 도는 포문임. temp list에 그 숫자가 담긴다.
# 그러면 작은 포문은 뭐냐. 작은 포문은 i에 해당하는 숫자가 리스트에 담긴 애들이랑 모두 bitwise 연산을 해서 그 리스트에 담길 수 있는가?
#

class Solution:
    def longestNiceSubarray(self, nums):
        answer = 1
        n = len(nums)
        for i in range(n):
            flag = True
            tmp = [nums[i]]
            for j in range(i+1, n):

                for case in tmp:
                    if nums[j] & case == 0:
                        continue
                    else:
                        flag = False
                        break
                if flag == True:
                    tmp.append(nums[j])
                else:
                    answer = max(answer, len(tmp))
                    break
            answer = max(answer, len(tmp))
        return answer
        
print(Solution().longestNiceSubarray([1,3,8,48,10]))
print(Solution().longestNiceSubarray([3,1,5,11,13]))
print(Solution().longestNiceSubarray([135745088,609245787,16,2048,2097152]))
