n, m = map(int, input().split())


INF = 1e10
dist = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1




for i in range(1, n+1):
    dist[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

pos =[]
minDist = 1e10

def getDist(c1, c2):
    curdist = 0
    for i in range(1, n+1):
        minTargetDist = min(dist[i][c1], dist[i][c2])
        curdist+= 2* (minTargetDist)

    return curdist

for i in range(1, n+1):
    for j in range(i+1, n+1):
        c1, c2 = i, j
        curDist = getDist(c1, c2)

        if minDist > curDist:
            minDist = curDist
            pos = []
            pos.append((c1, c2))
        elif minDist == curDist:
            pos.append((c1, c2))

pos.sort()

print(pos[0][0], pos[0][1], minDist)
