from collections import deque

def solution(edges):
    MAX = 1000001
    start = 0
    answer = [0, 0, 0, 0]
    
    degree = [0 for _ in range(MAX)]
    out = [0 for _ in range(MAX)]
    number = set()
    
    for e in edges:
        f, to = e[0], e[1]
        number.add(f)
        number.add(to)
        degree[to] +=1
        out[f]+=1
    
    

    number = sorted(number)
    for n in number:
        if degree[n] ==0:
            if out[n]>=2:
                start = n
                break
    for e in edges:
        f, to = e[0], e[1]
        if f == start:
            degree[to] -=1
    
    totalGraph = out[start]
    eight = 0
    makdae = 0
    for cur in number:
        if out[cur]>=2 and cur != start:
            eight+=1
        
        elif cur != start and out[cur] ==0:
            makdae+=1
    
    answer = [start, totalGraph-eight-makdae, makdae, eight]
        
                

    return answer