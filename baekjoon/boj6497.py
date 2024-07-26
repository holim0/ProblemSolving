import sys
input = sys.stdin.readline


p =[]
def find(x):
    if p[x] ==x:
        return x
    
    return find(p[x])

def merge(x, y):
    x = find(x)
    y = find(y)

    if x>y:
        p[x] = y
    else:
        p[y] = x




while True:
    m, n = map(int, input().split())
    if m==0 and n==0: break

    p = [i for i in range(m+1)]
    totalCost = 0
    g = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        totalCost+=z
        g.append((z, x, y))
    
    g.sort()
    
    for z, x, y in g:
        
        if find(x)!= find(y):
            merge(x, y)
            totalCost-=z

    print(totalCost)

    




