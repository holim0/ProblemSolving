import sys
input = sys.stdin.readline

n, m = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

accum_map = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if j==0:
            accum_map[i][j] = mapp[i][j]
        else:
            accum_map[i][j] = accum_map[i][j-1] + mapp[i][j]

k = int(input())

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    answer = 0
    for i in range(x1, x2+1):
        if y1==0:
            answer += accum_map[i][y2]
        else:
            answer += accum_map[i][y2] - accum_map[i][y1-1]

    print(answer)



