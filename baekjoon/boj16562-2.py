n, m, k = map(int, input().split())

cost =list(map(int, input().split()))
cost.insert(0, 0)

p = [i for i in range(n+1)]

def find(x):
    if x==p[x]:
        return x

    return find(p[x])


def merge(x, y):
    x = find(x)
    y = find(y)

    if x>y:
        p[x] = y
    else:
        p[y] = x

for _ in range(m):
    a, b  = map(int, input().split())

    if find(a) != find(b):
        merge(a, b)

minCost = 0

for i in range(1, n+1):
    parent = find(i)
    curMinCost = min(cost[i], cost[parent])
    cost[i] = curMinCost
    cost[parent] = curMinCost
    p[i] = parent

check = {}
for i in range(1, n+1):
    parent = p[i]
    if parent not in check:
        check[parent] = True
        minCost+=cost[parent]

if minCost<=k:
    print(minCost)
else:
    print("Oh no")
