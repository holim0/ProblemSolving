n, m = map(int, input().split())

namu = list(map(int, input().split()))

s, e = 1, max(namu)

while s<=e:


    mid = (s+e)//2

    cnt = 0

    for na in namu:
        if na>=mid:
            cnt += na-mid

    if cnt<m:
        e = mid-1
    elif cnt >=m:
        s = mid +1

print(e)
