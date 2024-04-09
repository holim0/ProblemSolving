import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

mapp = []
p = [i for i in range(n+1)]

for _ in range(n):
    value = list(map(int, input().split()))
    mapp.append(value)


def find(x):
    if x == p[x]:
        return x

    p[x] = find(p[x])
    return p[x]

def merge(x, y):
    if x == y: 
        return 
    
    x = find(x)
    y = find(y)

    p[y] = x

def isGroup(x, y):
    x = find(x)
    y = find(y)

    if x==y: return True
    return False


for i in range(n):
    for j in range(n):
        if mapp[i][j] == 0: continue
        merge(i+1, j+1)

route = list(map(int, input().split()))

for i in range(len(route)-1):
    if not isGroup(route[i], route[i+1]):
        print("NO")
        sys.exit()

print("YES")
        