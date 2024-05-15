n, m, k = map(int, input().split())

gen = list(map(int, input().split()))

check =[False for _ in range(n+1)]

for g in gen:
    check[g] = True

dist = []
for _ in range(m):
    u, v, w = map(int, input().split())
    dist.append((w, u, v))

dist = sorted(dist)

parent = [i for i in range(n+1)]

def find(x):
    if x==parent[x]:
        return x

    return find(parent[x])

def merge(x, y):
    
    x = find(x)
    y = find(y)

    if x in gen:
        parent[y] = x
    elif y in gen:
        parent[x] = y
    else:
        if x>y:
            parent[y] = x
        else:
            parent[x] = y

answer = 0
graph = []
for value in dist:
    w, a, b = value

    if find(a) != find(b):
        if not (find(a) in gen and find(b) in gen):
            answer+=w
            merge(a, b)
            graph.append((a, b))

print(answer)

    