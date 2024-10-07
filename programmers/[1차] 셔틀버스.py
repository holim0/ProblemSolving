def numberToTime(number):
    
    hour = number//60
    minute = number%60
    
    hour = str(hour)
    minute = str(minute)
    
    if len(hour)==1:
        hour = "0" +hour
    
    if len(minute)==1:
        minute = "0" + minute
    
    return hour+":"+minute

def solution(n, t, m, timetable):
    answer = 0
    numberTime = []
    busTimeTable = []
    busTimeCnt = {}
    for time in timetable:
        hour, minute = time.split(":")
        curNumberTime = int(hour) * 60 + int(minute)
        numberTime.append(curNumberTime)
    
    for i in range(n):
        busTimeTable.append(540 + t * i)
        busTimeCnt[540 + t * i] = [0, 0]
    
    numberTime.sort()
    boardCheck = [False for _ in range(len(numberTime))]
    
    timeIdx = 0
    for curBusTime in busTimeTable:
        cnt = 0
        
        while timeIdx<len(numberTime) and numberTime[timeIdx]<=curBusTime and cnt<m: 
            busTimeCnt[curBusTime][0]+=1
            busTimeCnt[curBusTime][1] = max(numberTime[timeIdx], busTimeCnt[curBusTime][1])
            timeIdx+=1
            cnt+=1
    
    busTimeCntList = []
    for key in busTimeCnt:
        busTimeCntList.append((key, busTimeCnt[key]))
    
    busTimeCntList.sort(reverse=True)
    
    anwer = 0
    
    for value in busTimeCntList:
        curBusTime, info = value
        curCnt, lastTime = info
        
        if curCnt<m:
            answer = max(curBusTime, lastTime)
            break
        else:
            answer = lastTime-1
            break
    
            
    
    return numberToTime(answer)