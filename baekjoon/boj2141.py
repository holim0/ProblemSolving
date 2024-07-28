n = int(input())

info = []

for _ in range(n):
    pos, cnt = map(int, input().split())
    info.append((pos, cnt))

info.sort()
mindist = float("inf")
minPos = float("inf")
s, e = 0, n-1

acc = [info[0][1]]

for i in range(1, n):
    acc.append(acc[-1] + info[i][1])



while s<=e:

    mid = (s+e)//2
    
    
    left, right = acc[mid], acc[n-1] - acc[mid]
    

    if left>=right:
        e = mid-1
        minPos = min(minPos, mid)
    else: 
        s = mid+1

print(info[minPos][0])