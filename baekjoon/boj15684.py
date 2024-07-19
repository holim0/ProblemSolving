import sys

n, m, h = map(int, input().split())

garo = []

check = [[False for _ in range(n)] for _ in range(h+1)]

link ={}

for _ in range(m):
    a, b = map(int, input().split())
    check[a][b] = True
    if b not in link:
        link[b]= [(a, b+1)]
    else:
        link[b].append((a, b+1))

    if b+1 not in link:
        link[b+1] = [(a, b)]
    else:
        link[b+1].append((a, b))

notCheck =[]

for i in range(1, h+1):
    for j in range(1, n):
        if not check[i][j]:
            notCheck.append((i, j))

def go(cur, curH):
    
    sortedLink = sorted(link[cur])
    print(sortedLink)
    isNxt = False
    n, nh = -1, -1
    for nxtH, nxt in sortedLink:
        if curH < nxtH:
            isNxt = True
            print("ggg", nxtH, nxt)
            nh, n = nxtH, nxt
            break
    
    if isNxt:
        go(n, nh)
    else:
        print("cur!!", cur)
        return cur


def checkValid(curJohab):
    
    for a, b in curJohab:
        print(a, b)
        if b not in link:
            link[b]= [(a, b+1)]
        else:
            link[b].append((a, b+1))

        if b+1 not in link:
            link[b+1] = [(a, b)]
        else:
            link[b+1].append((a, b))
    
    for start in range(1, n+1):
        end = go(start, 0)
        if end != start: 
            for a, b in curJohab:
                link[b].pop()
                link[b+1].pop()
            return False

    return True


def getJohab(curIdx, targetCnt, curJohab):
    global johabList
    if targetCnt==len(curJohab):
        if(checkValid(curJohab)):
            print(curJohab)
            print(len(curJohab))
            sys.exit()
        return 
        

    for i in range(curIdx, len(notCheck)):
        a, b = notCheck[i]
        curJohab.append((a, b))
        getJohab(i+1, targetCnt, curJohab)
        curJohab.pop()





def getSol():
    global johabList
    for cnt in range(1, 4):
        # for start in range(0, len(notCheck)-cnt+1):
        getJohab(0, cnt, [])
        
        
getSol()

print(-1)