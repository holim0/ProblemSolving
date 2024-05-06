def solution(friends, gifts):
    answer = 0
    
    giveCnt = {}
    takeCnt = {}
    giftJisu = {}
    connect = {}
    nextGiftCnt = {}
    connectCnt ={}
    
    for f in friends:
        if f not in giveCnt:
            giveCnt[f] = 0
        
        if f not in takeCnt:
            takeCnt[f] = 0
    
    for g in gifts:
        fromm, to = g.split(" ")
        
        if g not in connectCnt:
            connectCnt[g] = 1
        else:
            connectCnt[g] +=1
        
        if fromm not in connect:
            connect[fromm] = [to]
        else:
            connect[fromm].append(to)
    
        if fromm not in giveCnt:
            giveCnt[fromm] = 1
        else:
            giveCnt[fromm] +=1
            
        if to not in takeCnt:
            takeCnt[to] =1
        else:
            takeCnt[to]+=1
    
    def checkConnect(a, b):
        if a in connect and b in connect:
            if a in connect[b] or b in connect[a]:
                return True
            
        return False
    
    def checkGiftScore(a, b):
        aGiftScore = giveCnt[a] - takeCnt[a]
        bGiftScore = giveCnt[b] - takeCnt[b]
        if aGiftScore<bGiftScore:
            if b not in nextGiftCnt:
                nextGiftCnt[b] = 1
            else:
                nextGiftCnt[b]+=1
        elif aGiftScore>bGiftScore:
            if a not in nextGiftCnt:
                nextGiftCnt[a] = 1
            else:
                nextGiftCnt[a]+=1
    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            a, b = friends[i], friends[j]
            ab = a + " " + b
            ba = b + " " + a
            if checkConnect(a, b):
                aTob =0
                bToa =0
                if ab in connectCnt:
                    aTob = connectCnt[ab]

                if ba in connectCnt:
                    bToa = connectCnt[ba]

                if aTob > bToa:
                    if a not in nextGiftCnt:
                        nextGiftCnt[a] = 1
                    else:
                        nextGiftCnt[a]+=1
                elif aTob < bToa:
                    if b not in nextGiftCnt:
                        nextGiftCnt[b] = 1
                    else:
                        nextGiftCnt[b]+=1
                else:
                    checkGiftScore(a, b)  
            else:
                checkGiftScore(a, b)
                    
    for key in nextGiftCnt:
        answer =max(answer, nextGiftCnt[key])
    return answer