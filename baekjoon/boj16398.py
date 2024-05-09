import sys
import heapq as hp
input = sys.stdin.readline
n = int(input())

flow = []

for _ in range(n):
    row = list(map(int, input().split()))
    flow.append(row)

q = []
check = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i!=j:
            if not check[i][j] and not check[j][i]:
                q.append((flow[i][j], i, j))

p = [i for i in range(n+1)]

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def merge(x, y):

    x = find(x)
    y = find(y)
    if x == y: return 
    if x>y:
        p[y] = x
    else:
        p[x] = y

answer = 0



q = sorted(q)
for cost, x, y in q:

    if find(x) != find(y):
        merge(x, y)
        answer+=cost


print(answer)