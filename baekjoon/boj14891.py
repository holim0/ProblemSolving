from collections import deque

top = []

l, r = 4, 0

for i in range(4):
    row = list(map(int, input()))
    q = deque(row)
    q.append(q[0])
    q.append(q[1])
    q.popleft()
    q.popleft()
    top.append(q)

k = int(input())
order = []

for _ in range(k):
    a, b = map(int, input().split())
    order.append((a, b))


def rotate(cur, dir):
    if dir ==1:
        cur.insert(0, cur[-1])
        cur.pop()

    else:
        cur.append(cur[0])
        cur.popleft()

reverse = {
    1: -1,
    -1: 1
}

for o in order:
    isRotate = [False, False, False, False]
    topNumber, direction = o
    isRotate[topNumber-1] = True
    if topNumber == 1:
        if top[0][r] != top[1][l]:
            isRotate[1] = True

            if top[1][r] != top[2][l]:
                isRotate[2] = True

                if top[2][r] != top[3][l]:
                    isRotate[3] = True
            
        for i in range(len(isRotate)):
            if isRotate[i]:
                if i==0 or i==2:
                    rotate(top[i], direction)
                else:
                    rotate(top[i], reverse[direction])

    elif topNumber == 2:
        if top[1][l] != top[0][r]:
            isRotate[0] = True
        if top[1][r] != top[2][l]:
            isRotate[2] = True

            if top[2][r] != top[3][l]:
                isRotate[3] = True
        
        for i in range(len(isRotate)):
            if not isRotate[i]: continue
            if i==0 or i==2:
                rotate(top[i], reverse[direction])
            else:
                rotate(top[i], direction)
        
    elif topNumber == 3:
        if top[2][l] != top[1][r]:
            isRotate[1] = True
            if top[1][l] != top[0][r]:
                isRotate[0] = True
        if top[2][r] != top[3][l]:
            isRotate[3] = True


        for i in range(len(isRotate)):
            if isRotate[i]:
                if i==1 or i==3:
                    rotate(top[i], reverse[direction])
                else:
                    rotate(top[i], direction)
        
    elif topNumber == 4:
        if top[3][l] != top[2][r]:
            isRotate[2] = True

            if top[2][l] != top[1][r]:
                isRotate[1] = True

                if top[1][l] != top[0][r]:
                    isRotate[0] = True

        for i in range(len(isRotate)):
            if isRotate[i]:
                if i==0 or i==2:
                    rotate(top[i], reverse[direction])
                else:
                    rotate(top[i], direction)
        

answer = 0



for i in range(len(top)):
    cur = top[i]

    if cur[6] == 1:
        answer += pow(2, i)

print(answer)

