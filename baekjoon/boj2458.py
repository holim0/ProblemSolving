n, m = map(int, input().split())

compare = []

rel = [[0 for _ in range(n+1)] for _ in range(n+1)]

answer =0

for _ in range(m):
    a, b = map(int, input().split())
    compare.append((a, b))
    rel[a][b] = -1
    rel[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if rel[a][k] == 1 and rel[k][b]==1:
                rel[a][b] = 1
            
            elif rel[a][k] == -1 and rel[k][b]== -1:
                rel[a][b] = -1

for i in range(1, n+1):
    isAllLink = True
    for j in range(1, n+1):
        if i==j: continue
        if rel[i][j] == 0 or rel[j][i] ==0:
            isAllLink = False
            break
    
    if isAllLink: answer+=1

print(answer)
