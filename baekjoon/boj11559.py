from collections import deque
mapp =[]

answer = 0

for _ in range(12):
    l = list(input())
    mapp.append(l)

def checkDone():
    global mapp
    visited = [[False for _ in range(6)] for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if mapp[i][j] != ".":
                cnt = 0
                curValue = mapp[i][j]
                q = deque([])
                q.append((i, j))
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    cnt+=1

                    for a, b in [(1, 0), (0,1), (-1, 0), (0, -1)]:
                        nx, ny = x+a, y+b
                        if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and mapp[nx][ny] == curValue:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                
                if cnt>=4: 
                    return False

    return True            

def move():
    global mapp
    for j in range(6):
        temp = []
        for i in range(11, -1, -1):
            if mapp[i][j] !=".":
                temp.append(mapp[i][j])
        
        while len(temp) != 12:
            temp.append(".")
        
        for i in range(11, -1, -1):
            mapp[i][j] = temp[11-i]

        



while checkDone() == False:
    visited = [[False for _ in range(6)] for _ in range(12)]
    isBomb = False
    for i in range(12):
        for j in range(6):
            if mapp[i][j] != ".":
                curValue = mapp[i][j]
                q = deque([])
                q.append((i, j))
                saveList = [(i, j)]
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for a, b in [(1, 0), (0,1), (-1, 0), (0, -1)]:
                        nx, ny = x+a, y+b
                        if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and mapp[nx][ny] == curValue:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            saveList.append((nx, ny))
                
                if len(saveList)>=4:
                    isBomb = True
                    for x, y in saveList:
                        mapp[x][y] = "."

    if isBomb: 
        answer+=1
        # for i in range(12):
        #     print("".join(mapp[i]))
        move()
        # print("afterMove")
        # for i in range(12):
        #     print("".join(mapp[i]))
        
    
            



print(answer)
