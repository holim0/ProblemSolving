n, d, k, c = map(int, input().split())


belt = []

for _ in range(n):
    name = int(input())
    belt.append(name)

answer = 0

cnt = {}

curKind = 0


s, e = 0, k-1



while s<n:
    if s==0 and e==k-1:
        for i in range(s, e+1):
            cur = belt[i]
            if cur not in cnt:
                cnt[cur]=1
                curKind+=1
            else:
                cnt[cur]+=1
    else:
        beforeValue = belt[s-1]
        cnt[beforeValue]-=1

        if cnt[beforeValue]==0: curKind-=1

        addValue= belt[e%n]
        if addValue not in cnt or cnt[addValue]==0:
            cnt[addValue] = 1
            curKind+=1
        else:
            cnt[addValue]+=1


    
    if c not in cnt or cnt[c]==0:
        answer = max(answer, curKind+1)
    else:
        answer = max(answer, curKind)

    s+=1
    e+=1

print(answer)
