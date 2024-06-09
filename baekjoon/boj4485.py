import sys
import heapq

input = sys.stdin.readline
num = 1
while True:

    n = int(input())
    if n==0: break

    mapp =[]

    for _ in range(n):
        row = list(map(int, input().split()))
        mapp.append(row)

    INF = 1e10
    lossCnt = [[INF] * n for _ in range(n)]

    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    lossCnt[0][0] = mapp[0][0]

    q = []

    heapq.heappush(q, (lossCnt[0][0], 0, 0))

    while q:
        curLossCnt, cx, cy = heapq.heappop(q)

        if lossCnt[cx][cy] < curLossCnt: continue

        for a, b in dir:
            nx, ny = cx+a, cy+b

            if 0<=nx<n and 0<=ny<n:
                if lossCnt[nx][ny] > curLossCnt + mapp[nx][ny]:
                    lossCnt[nx][ny] = curLossCnt + mapp[nx][ny]
                    heapq.heappush(q, (lossCnt[nx][ny], nx, ny))

    print("Problem " + str(num)+":", lossCnt[n-1][n-1])
    num+=1