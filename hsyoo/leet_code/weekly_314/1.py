class Solution:
    def hardestWorker(self, n, logs):
        logs.sort(key = lambda x : x[1])
        prev = 0
        answer = []
        for item in logs:
            worker_id, finish = item
            time = finish - prev
            prev = finish
            answer.append((time, worker_id))
        
        answer.sort(key = lambda x: (x[0], -x[1]), reverse = True)
        # print(answer)
        return answer[0][1]

print(Solution().hardestWorker(10, [[0,3],[2,5],[0,9],[1,15]]))
print(Solution().hardestWorker(26, [[1,1],[3,7],[2,12],[7,17]]))
print(Solution().hardestWorker(2, [[0,10],[1,20]]))
            
        