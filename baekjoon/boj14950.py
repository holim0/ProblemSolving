n, m, t = map(int, input().split())
g = []

for _ in range(m):
    a, b, c = map(int, input().split())
    g.append((c, a, b))

p = [i for i in range(n+1)]

g.sort()

answer = 0

plus = 0

def find(a):
    if a == p[a]: return a

    return find(p[a])

def merge(a, b):
    a = find(a)
    b = find(b)

    if a>b:
        p[a] = b
    else:
        p[b] = a

for c, a, b in g:
    
    if find(a) != find(b):
        merge(a, b)
        answer+= (c+plus)
        plus+=t

print(answer)

