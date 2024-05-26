r, c, k = map(int, input().split())

mapp =[]

visited = [[False for _ in range(c)] for _ in range(r)]

for _ in range(r):
    row = list(input())
    mapp.append(row)

answer = 0
def find(cx, cy, dist):
    global visited
    global answer


    if cx==0 and cy== c-1:
        if dist == k:
            answer+=1
            return 
        

    for a, b in [(0, 1),(1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b
        
        if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and mapp[nx][ny] != "T":
            visited[nx][ny] = True
            find(nx, ny, dist+1)
            visited[nx][ny] = False      

visited[r-1][0] = True 
find(r-1, 0, 1)

print(answer)