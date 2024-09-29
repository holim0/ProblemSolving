def solution(routes):
    answer = 0
    mapp = []
    routes.sort(key=lambda x: (x[1], x[0]))
    
    curEnd = -1e10
    
    for r in routes:
        s, e = r
        
        if s>curEnd:
            answer+=1
            curEnd = e
        
    
    return answer