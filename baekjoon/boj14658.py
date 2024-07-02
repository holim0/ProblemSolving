n, m, l, k = map(int, input().split())

drop = []

for _ in range(k):
    x, y  =map(int, input().split())
    drop.append((x, y))

drop.sort()


maxCatch = -1




for i in range(k):
    x1, y1 = drop[i]
    for j in range(k):
        x2, y2 = drop[j]
        cnt = 0
        for kk in range(k):
            cx, cy = drop[kk]
            if x1<=cx<=x1+l and y2<=cy<=y2+l:
                cnt+=1
        maxCatch = max(maxCatch, cnt)

print(k-maxCatch)