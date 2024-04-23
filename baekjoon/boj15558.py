from collections import deque
import sys

n, k = map(int, input().split())

mapp = []

for _ in range(2):
    m = list(input())
    mapp.append(m)

visited = [[False for _ in range(n)] for _ in range(2)]

visited[0][0] = True
q = deque([])

q.append((0, 0, 0))

swap = {
    0: 1,
    1: 0
}

while q:
    i, j, curTime = q.popleft()


    if j+1 >= n or j+k >=n:
        print(1)
        sys.exit()
    
    if j+1<=n-1 and not visited[i][j+1] and mapp[i][j+1]== "1":
        visited[i][j+1] = True
        q.append((i, j+1, curTime+1))

    if j-1>=0 and not visited[i][j-1] and j-1 > curTime and mapp[i][j-1]== "1":
        visited[i][j-1] = True
        q.append((i, j-1, curTime+1))


    if j+k<=n-1 and not visited[swap[i]][j+k] and mapp[swap[i]][j+k]== "1":
        visited[swap[i]][j+k] = True
        q.append((swap[i], j+k, curTime+1))

    

print(0)

