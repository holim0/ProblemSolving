n, m, k = map(int, input().split())

beer = []

s = 1
e = 0
for _ in range(k):
    v, c = map(int, input().split())
    e+=c
    beer.append((v, c))

beer = sorted(beer, key=lambda x: x[1])

answer = 1e10
while s<=e:

    mid = (s+e)//2
    prefer = 0
    curlevel = mid
    temp = []
    for v, c in beer:
        if curlevel>=c:
            temp.append(v)
        else:
            break
    
    
    if len(temp) < n:
        s = mid+1
        continue
    
    temp.sort(reverse=True)

    for i in range(n):
        prefer+=temp[i]

    if prefer >=m:
        e = mid - 1
        answer = min(mid, answer)
    else:
        s = mid + 1

if answer !=1e10:
    print(answer)
else:
    print(-1)
