import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

link = []

for _ in range(m):
    a, b, c = map(int, input().split())
    link.append((c, a, b))

link = sorted(link)

p = [i for i in range(n+1)]

def find(x):
    global p
    if x == p[x]:
        return x
    
    p[x] = find(p[x])
    return p[x]

def merge(a, b):
    global p 

    a = find(a)
    b = find(b)

    if a >b:
        p[b] = a
    else:
        p[a] = b

answer = 0
for l in link:
    cost, a, b = l
    
    if find(a) != find(b):
        answer +=cost
        merge(a, b)
    
print(answer)