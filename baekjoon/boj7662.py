import heapq as hp

t = int(input())


for _ in range(t):
    maxQ = []
    minQ = []
    isDelete = {}
    k = int(input())

    for _ in range(k):
        order, number= input().split()
        number = int(number)

        if order == "I":
            hp.heappush(maxQ, number * (-1))
            hp.heappush(minQ, number)
            isDelete[number] = isDelete.get(number, 0) + 1
        else:
            if len(maxQ)==0 or len(minQ)==0: continue
            if number == 1:
                while maxQ:
                    maxValue = hp.heappop(maxQ) * (-1)

                    if isDelete[maxValue]==0:
                        continue
                    else:
                        isDelete[maxValue] -=1
                        break
            
            else:
                while minQ:
                    minValue = hp.heappop(minQ)

                    if isDelete[minValue]==0:
                        continue
                    else:
                        isDelete[minValue]-=1
                        break

    isPrint= False
    while maxQ:
        cur = hp.heappop(maxQ) * -1

        if isDelete[cur] >0:
            print(cur, end=" ")
            isPrint = True
            break
    
    while minQ:
        cur = hp.heappop(minQ)

        if isDelete[cur] >0:
            isPrint = True
            print(cur)
            break
    
    if not isPrint:
        print("EMPTY")
