n, m = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input()))
    mapp.append(row)

answer = 1
maxSize = min(n, m)


def find(i, j):
    global mapp
    global answer
    
    for l in range(1, maxSize):
        if i+l>=n or j+l>=m: continue
        a, b, c, d = mapp[i][j], mapp[i+l][j], mapp[i][j+l], mapp[i+l][j+l]

        if a==b and b==c and c==d:
            answer = max(answer, pow((l+1), 2))



for i in range(n-1):
    for j in range(m-1):
        find(i, j)




print(answer)