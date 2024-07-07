n, m, k = map(int, input().split())

cost = list(map(int, input().split()))

cost.insert(0, 0)

g = {}

p = [0, ]

for i in range(1, n+1):
    p.append(i)

def find(x):
    if x == p[x]:
        return p[x]

    return find(p[x])


def merge(a, b):

    a = find(a)
    b = find(b)
    if a>b:
        p[a] = b
    
    else:
        p[b] = a
        


for _ in range(m):
    v, w = map(int, input().split())
    if find(v) != find(w):
        merge(v, w)

minCost = 0

pWithCost =[(-1, -1)]

for i in range(1, n+1):
    pWithCost.append((find(p[i]), cost[i]))

pWithCost.sort()

check = [False] * (n+1)
for i in range(1, n+1):
    parent, cost = pWithCost[i]

    if not check[parent]:
        check[parent] = True
        minCost+=cost

if minCost<=k:
    print(minCost)
else:
    print("Oh no")





