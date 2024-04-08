import sys
input = sys.stdin.readline
n, m = map(int, input().split())

mapp = [i for i in range(n+1)]

def find(x):

    if x == mapp[x]:
        return x
    
    mapp[x] = find(mapp[x])

    return mapp[x]


def merge(x, y):

    x = find(x)
    y = find(y)

    if x==y: return

    mapp[y] = x

def isUnion(x, y):
    x = find(x)
    y = find(y)

    if x==y: return True
    return False

for _ in range(m):
    order, a, b = map(int, input().split())

    if order ==0:
        merge(a, b)

    else:
        print("YES") if isUnion(a, b) else print("NO")

