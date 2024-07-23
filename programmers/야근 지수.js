import heapq as hp

def solution(n, works):
    answer = 0
    w = []
    
    for ww in works:
        hp.heappush(w, -ww)
    
    while n:
        curw = hp.heappop(w)
        curw = (-1) * curw
        if curw ==0:
            return 0
            
        curw-=1
        hp.heappush(w, -curw)
        n-=1
    
    
    print(w)
    for ww in w:
        answer+= pow(ww, 2)
    return answer