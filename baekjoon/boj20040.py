import sys
input = sys.stdin.readline

n, m = map(int, input().split())

p = [i for i in range(n+1)]

pos =[0, ]

for _ in range(m):
    x, y = map(int, input().split())
    pos.append((x, y))


def find(x):

    if x == p[x]:
        return x
    
    return find(p[x])

def merge(a, b):
    
    a = find(a)
    b = find(b)

    if a>b:
        p[a] = b
    else:
        p[b] = a

for i in range(1, m+1):
    x, y = pos[i]

    if find(x) != find(y):
        merge(x, y)
    else:
        print(i)
        sys.exit()
    


print(0)