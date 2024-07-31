n, l, m = map(int, input().split())
pos =[]

answer = 0
for _ in range(m):
    a, b = map(int, input().split())
    pos.append((a, b))


def checkCnt(a1, b1, a2, b2):
    global answer


    for r in range(1, int(l//2)+1):
        c = (l- (2 *r))//2
        if c<=0: continue
        curCnt = 0
        for i in range(m):
            cx, cy = pos[i]
            if a1<=cx<=a1+r and b2<=cy<=b2+c:
                curCnt+=1

        answer = max(answer, curCnt)


for i in range(m):
    a1, b1 = pos[i]
    for j in range(m):
        a2, b2 = pos[j]
        checkCnt(a1, b1, a2, b2)

print(answer)

