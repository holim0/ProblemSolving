import sys
input = sys.stdin.readline

t = int(input())
parent = []

def find(x):
    global parent

    if x == parent[x]:
        return x

    return find(parent[x])

def merge(x, y):

    x = find(x)
    y = find(y)

    if x>y:
        parent[x] = y
    else:
        parent[y] = x

for i in range(1, t+1):

    n = int(input())

    parent = [i for i in range(n)]

    k = int(input())

    for _ in range(k):
        a, b = map(int, input().split())
        if find(a) != find(b):
            merge(a, b)

    m = int(input())
    answer = []
    for _ in range(m):
        u, v = map(int, input().split())
        if find(v) == find(u):
            answer.append(1)
        else:
            answer.append(0)
    print("Scenario "+str(i)+":")
    for a in answer:
        print(a)
    print()
        
    

