n, m, b = map(int, input().split())

mapp =[]

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

time = 1e10
h = 0

flatMap = []

for i in range(n):
    for j in range(m):
        flatMap.append(mapp[i][j])    

flatMap.sort(reverse=True)

def calTime(curH):
    global b, flatMap
    curRest = b
    curTime = 0

    for hValue in flatMap:
        if hValue == curH: continue

        if hValue<curH:
            need = curH-hValue
            
            if curRest<need: return 1e11
            curTime+=need
            curRest-=need
        else:
            plus = hValue-curH
            curTime+= (2*plus)
            curRest+=plus
    
    return curTime


for i in range(256, -1, -1):
    
    curTime = calTime(i)
    if curTime<time:
        time = curTime
        h = i
    elif curTime==time:
        h = max(h, i)

print(time, h)