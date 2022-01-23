'''
문제 3.
35분 49초
'''
def solution(fees, records):
    unitTime, unitPrice, paraTime, paraPrice = fees
    
    carInfo = {}
    carList = []
    for r in records:
        time,carNum,IO = r.split()
        temp = list(map(int,time.split(":")))
        time = temp[0]*(60) + temp[1]
        if carNum in carInfo.keys():
            # 다시 입차인 경우
            if carInfo[carNum][1]:
                carInfo[carNum][1] = False
                carInfo[carNum][0] = time
            # 출차인 경우
            else:
                carInfo[carNum][1] = True
                carInfo[carNum][2] += time-carInfo[carNum][0]
        else:
            carInfo[carNum] = [time,False,0]
            carList.append((int(carNum),carNum))
    
    # 출차 기록 안된 차 정리
    for car in carInfo.keys():
        if not carInfo[car][1]:
            carInfo[car][2] += 1439 - carInfo[car][0]
            
    # 반환할 리스트 정리
    ans = []
    carList = sorted(carList,key=lambda x: x[0])
    for _,car in carList:
        time = carInfo[car][2]
        howMuch = unitPrice
        if time > unitTime:
            quo = (time - unitTime) // paraTime
            if (time - unitTime) % paraTime != 0:
                quo += 1
            howMuch += quo * paraPrice
        ans.append(howMuch)
            
    print(ans)
    return ans
