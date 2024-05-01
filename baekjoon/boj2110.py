import sys
n, c = map(int, input().split())

pos = []

for _ in range(n):
    p = int(input())
    pos.append(p)

pos = sorted(pos)

s, e = 1, pos[-1]-pos[0]

while s<=e:

    mid = (s+e)//2
    
    cur = pos[0]
    cnt = 1
    for i in range(1, len(pos)):

        if pos[i]-cur>=mid:
            cnt+=1
            cur = pos[i]

    if cnt>=c:
        s = mid+1
    else:
        e = mid-1

print(e)