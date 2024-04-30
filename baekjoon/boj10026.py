from collections import deque

answer1, answer2 = 0, 0

n = int(input())

mapp = []

for _ in range(n):
    m = input()
    m = list(m)
    mapp.append(m)

visited = [[False for _ in range(n)] for _ in range(n)]
q = deque([])

for i in range(n):
    for j in range(n):
        if visited[i][j]: continue

        cur = mapp[i][j]
        visited[i][j] = True
        answer1+=1
        q.append((i, j))

        while q:
            cx, cy = q.popleft()

            for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = cx+a, cy+b

                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and mapp[nx][ny] == cur:
                    visited[nx][ny] = True
                    q.append((nx, ny))


visited = [[False for _ in range(n)] for _ in range(n)]

q = deque([])

color =  {
    "R": "R",
    "G": "R",
    "B": "B"
}

for i in range(n):
    for j in range(n):
        if visited[i][j]: continue

        cur = color[mapp[i][j]]
        visited[i][j] = True
        answer2+=1
        q.append((i, j))

        while q:
            cx, cy = q.popleft()

            for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = cx+a, cy+b

                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and color[mapp[nx][ny]] == cur:
                    visited[nx][ny] = True
                    q.append((nx, ny))



print(answer1, answer2)