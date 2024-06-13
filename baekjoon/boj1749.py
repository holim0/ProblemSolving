n, m = map(int, input().split())
answer = -1e10
mapp = [[0 for _ in range(m+1)]]

for _ in range(n):
    row = list(map(int, input().split()))
    row.insert(0, 0)
    mapp.append(row)

acc = [[0 for _ in range(m+1)]]

for i in range(1, n+1):
    acc_row = [0, ]
    for j in range(1, m+1):
        acc_value = acc[i-1][j] + acc_row[-1] + mapp[i][j] - acc[i-1][j-1]
        acc_row.append(acc_value)
    acc.append(acc_row)


for i in range(1, n+1):
    for j in range(1, m+1):
        sx, sy = i, j
        for a in range(sx, n+1):
            for b in range(sy, m+1):
                ex, ey = a, b
                
                
                sum = acc[ex][ey] - (acc[sx-1][ey] + acc[ex][sy-1]) + acc[sx-1][sy-1]
                
                answer = max(answer, sum)

print(answer)



