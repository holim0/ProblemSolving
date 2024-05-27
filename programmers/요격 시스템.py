def solution(targets):
    answer = 1
    
    targets.sort(key=lambda x: x[1])

    end = targets[0][1]
    
    for i in range(1, len(targets)):
        s, e = targets[i][0], targets[i][1]
        
        if s>=end:
            answer+=1
            end = e
                
    return answer