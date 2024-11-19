r, c = map(int, input().split())

mapp =[]

for _ in range(r):
    row = list(input())
    mapp.append(row)


visit = {}
# check = [[False] * c for _ in range(r)]
answer = 0
def checkRange(x, y):

    if 0<=x<r and 0<=y<c: return True

    return False


def go(x, y, visitCnt):
    global answer  

    if answer<visitCnt:
        answer = visitCnt

    for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x+a, y+b
        
        if checkRange(nx, ny) and not visit.get(mapp[nx][ny], False):
            visit[mapp[nx][ny]] = True
            go(nx, ny, visitCnt+1)
            visit[mapp[nx][ny]] = False
        
visit[mapp[0][0]] = True

go(0, 0, 1)
print(answer)