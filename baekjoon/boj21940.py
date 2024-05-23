n, m = map(int, input().split())

INF = 1e10
dist = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    dist[a][b] = t

for i in range(1, n+1):
    dist[i][i] = 0

answer = []
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

totalNum = int(input())
live = list(map(int, input().split()))
minFromMax = 1e10

for i in range(1, n+1):
    curMax = 0

    for l in live:
        curMax = max(curMax, dist[l][i] + dist[i][l])
    
    if minFromMax > curMax:
        minFromMax = curMax
        answer = [i]

    elif minFromMax == curMax:
        answer.append(i)

answer.sort()

print(" ".join(str(a) for a in answer))