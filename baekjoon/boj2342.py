import sys
sys.setrecursionlimit(10**5)
order = list(map(int, input().split()))

order = order[:-1]

dist = [[[-1]*(len(order)+1) for _ in range(5)] for _ in range(5)]

def getDist(fromm, to):
    if fromm==0:
        return 2
    
    if abs(fromm-to)==2:
        return 4
    
    if fromm==to:
        return 1
    
    return 3

def solve(x, y, idx):
    global order
    if idx==len(order): return 0
    if dist[x][y][idx] !=-1:
        return dist[x][y][idx]
   

    leftMoveCnt = solve(order[idx], y, idx+1) + getDist(x, order[idx])
    rightMoveCnt = solve(x, order[idx], idx+1) + getDist(y, order[idx])

    dist[x][y][idx] = min(leftMoveCnt, rightMoveCnt)

    return dist[x][y][idx]

answer = solve(0, 0, 0)
print(answer)