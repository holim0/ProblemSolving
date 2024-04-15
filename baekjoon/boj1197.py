import sys
input = sys.stdin.readline

v, e = map(int, input().split())

g = []

for _ in range(e):
    a, b, c = list(map(int, input().split()))

    g.append((c, a, b))

g.sort()

p = [0 for _ in range(v+1)]

for i in range(1, v+1):
    p[i] = i

def find(a):
    global p
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]

def merge(a, b):
    global p

    a = find(a)
    b = find(b)

    if a>b:
        p[a] = b
    else:
        p[b] = a
answer = 0
for value in g:
    cost, a, b = value

    if find(a) != find(b):
        answer +=cost
        merge(a, b)
    
print(answer)