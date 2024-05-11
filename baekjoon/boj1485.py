t = int(input())

for _ in range(t):
    pos = []
    for _ in range(4):
        x, y = map(int, input().split())
        pos.append((x, y))
    
    pos = sorted(pos)

    l1, l2, l3 =0, 0, 0
    x0, y0 = pos[0]
    for i in range(1, 4):
        cx, cy = pos[i]
        if i==1:
            l1 = abs(x0-cx)**2 + abs(y0-cy)**2
        if i==2:
            l2 = abs(x0-cx)**2 + abs(y0-cy)**2
        if i==3:
            l3 = abs(x0-cx)**2 + abs(y0-cy)**2


    if l1 == l2:
        x1, y1 = pos[1]
        x2, y2 = pos[2]

        if l3 == abs(x1-x2)**2 + abs(y1-y2)**2:
            print(1)
        else:
            print(0)
    elif l1 == l3:
        x1, y1 = pos[1]
        x3, y3 = pos[3]

        if l3 == abs(x1-x3)**2 + abs(y1-y3)**2:
            print(1)
        else:
            print(0)
    elif l2 == l3:
        x2, y2 = pos[2]
        x3, y3 = pos[3]

        if l3 == abs(x3-x2)**2 + abs(y3-y2)**2:
            print(1)
        else:
            print(0)
    else:
        print(0)