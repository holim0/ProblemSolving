import sys
input = sys.stdin.readline
n, m = map(int, input().split())

cost =[]
dist = []
parent = [i for i in range(0, n+1)]

def find(x):
    if x == parent[x]:
        return x
    
    return find(parent[x])

def merge(x, y):
    x = find(x)
    y = find(y)

    if x>y:
        parent[y] = x
    else:
        parent[x] = y
    
x, k = 0, 0
for _ in range(m):
    a, b = map(int, input().split())

    if find(a-1)!= find(b-1):
        merge(a-1, b-1)

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if i!=j:
            dist.append((row[j], i, j))

dist = sorted(dist)
pos =[]
minCost =0
for d in dist:
    cost, a, b = d
    if a==0 or b ==0: continue
    if find(a) !=find(b):
        merge(a, b)
        minCost+=cost
        pos.append((a+1, b+1))

if len(pos)==0:
    print(0, 0)

else:
    print(minCost, len(pos))

    for p in pos:
        a, b = p
        print(a, b)
