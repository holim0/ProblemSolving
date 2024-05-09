n = int(input())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

check = [[False for _ in range(n)] for _ in range(n)]

INF = 1e10
answer = 1e10
def find(cnt, cost, x, y):
    global answer
    if cnt == 3:
        answer = min(cost, answer)
        return 
    
    golist = []
    for a, b in [(0,1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x + a, y+b
        if 0<=nx<n and 0<=ny<n and not check[nx][ny]:
            golist.append((nx, ny))
    
    cur_cost = cost + mapp[x][y]
    if len(golist) == 4:
        for a, b in golist:
            cur_cost+=mapp[a][b]
            check[a][b] = True

        for i in range(n):
            for j in range(n):
                if not check[i][j]:
                    find(cnt+1, cur_cost, i, j)
        
        for a, b in golist:
            check[a][b] = False

             


for i in range(n):
    for j in range(n):
        check = [[False for _ in range(n)] for _ in range(n)]
        find(0, 0, i, j)

print(answer)