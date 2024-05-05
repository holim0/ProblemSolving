import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())

mapp = []

for _ in range(r):
    row = list(map(int, input().split()))
    mapp.append(row)

accum_mapp =[[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if j==0:
            accum_mapp[i][j] = mapp[i][j]
        else:
            accum_mapp[i][j] = accum_mapp[i][j-1] + mapp[i][j]


for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    cnt = (r2-r1+1) * (c2-c1+1)

    sum = 0 

    for i in range(r1, r2+1):
        if c1 >0:
            cur_sum = accum_mapp[i][c2] - accum_mapp[i][c1-1]
        else:
            cur_sum = accum_mapp[i][c2]
        sum+=cur_sum
    
    print(sum//cnt)

