n = int(input())

mapp = []

for i in range(n):
    value = map(int, input().split())
    mapp.append(list(value))

INF = 1e10
g = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1:
            g[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1: continue
            if g[i][k] ==1 and g[k][j] == 1:
                g[i][j] = 1
            

for i in range(n):
    print(" ".join(str(value) for value in g[i]))
