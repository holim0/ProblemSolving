import sys
input = sys.stdin.readline
n, p = map(int, input().split())

stackMap = {}

answer = 0

info =[]

for _ in range(n):
    a, b = map(int, input().split())
    info.append((a, b))

for a, b in info:
    if a not in stackMap:
        stackMap[a] = [b]
        answer+=1
    
    else:
        if len(stackMap[a]) ==0:
            stackMap[a] = [b]
            answer+=1
            continue 
        
        while stackMap[a] and stackMap[a][-1]>b:
            topValue= stackMap[a].pop()
            answer+=1
        
        if stackMap[a] and stackMap[a][-1] == b: continue
        stackMap[a].append(b)
        answer+=1

print(answer)