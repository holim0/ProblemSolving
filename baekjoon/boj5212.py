r, c = map(int, input().split())

mapp =[]
napp = [[0 for _ in range(c)] for _ in range(r)]
for _ in range(r):
    l = list(input())
    mapp.append(l)


for i in range(r):
    for j in range(c):
        if mapp[i][j] == ".":
            napp[i][j] = "."
        else:
            sea = 0

            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = i+x, j+y
                if 0<=nx<r and 0<=ny<c:
                    if mapp[nx][ny] ==".":
                        sea+=1
                else:
                    sea+=1
            
            if sea>=3:
                napp[i][j] = "."
            else:
                napp[i][j] = "X"
si, sj, ei, ej = 0, 0, 0, 0

for i in range(r):
    isDone = False
    for j in range(c):
        if napp[i][j] == "X":
            si = i
            isDone = True
            break
    if isDone:
        break

for j in range(c):
    isDone = False
    for i in range(r):
        if napp[i][j] =="X":
            sj = j
            isDone = True
            break
    if isDone: break

for i in range(r-1, -1, -1):
    isDone = False
    for j in range(c-1, -1, -1):
        if napp[i][j] =="X":
            ei = i
            isDone = True
            break
    if isDone: break

for j in range(c-1, -1, -1):
    isDone = False
    for i in range(r-1, -1, -1):
        if napp[i][j] =="X":
            ej = j
            isDone = True
            break
    if isDone: break

for i in range(si, ei+1):
    l = napp[i]
    l = l[sj:ej+1]
    print("".join(l))


