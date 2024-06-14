n = int(input())

location = list(map(int, input().split()))

location.sort()


minDist = 1e10

answer = n//2

def getDist(cur):
    global answer
    global minDist
    dist = 0


    for i in range(n):
        value = location[i]
        dist+= abs(value-location[cur])
    
    if minDist>dist:
        minDist = dist
        answer = cur
    elif minDist==dist:
        if answer> cur:
            answer = cur


getDist(n//2)
if n//2-1>=0:
    getDist(n//2-1)

if n//2+1<n:
    getDist(n//2+1) 


print(location[answer])