n, m = map(int, input().split())

knowTrue = list(map(int, input().split()))

knowCheck = {}

for i in range(1, len(knowTrue)):
    knowCheck[knowTrue[i]] = True


answer = m

p = [i for i in range(n+1)]


def find(x):
    if x==p[x]:
        return p[x]

    return find(p[x])


def merge(x, y):

    x = find(x)
    y = find(y)


    if x>y:
        p[x] = y
    else:
        p[y] = x

party = []

for _ in range(m):
    info = list(map(int, input().split()))
    
    for i in range(1, len(info)-1):
        cur, nxt = info[i], info[i+1]
        if find(cur) != find(nxt):
            merge(cur, nxt) 


    party.append(info)

for i in range(1, n+1):
    p[i] = find(i)
    if i in knowCheck:
        knowCheck[p[i]] = True
    

for curParty in party:
    if p[curParty[1]] in knowCheck:
        answer-=1

print(answer)
        
        

