import sys
input = sys.stdin.readline
n, m = map(int, input().split())

g = []

for _ in range(m+1):
    a, b, c =map(int, input().split())
    g.append((c, a, b))

min_g = sorted(g)
max_g = sorted(g, reverse=True)



parent = [0 for _ in range(n+1)]

for i in range(0, n+1):
    parent[i] = i

def find(x):
    if x== parent[x]:
        return x
    
    x = find(parent[x])
    return x

def merge(x, y):
    x = find(x)
    y = find(y)

    if x>y:
        parent[x] = y
    else:
        parent[y] = x

piro_cnt1 = 0
for c, a, b in min_g:
    if find(a) != find(b):
        merge(a, b)
        
        if c == 0:
            
            piro_cnt1+=1


piro_cnt2 = 0


parent = [0 for _ in range(n+1)]
for i in range(0, n+1):
    parent[i] = i

for c, a, b in max_g:
    if find(a) != find(b):
        merge(a, b)
        if c == 0:
            piro_cnt2+=1


print(int(pow(piro_cnt1, 2) - pow(piro_cnt2, 2)))
