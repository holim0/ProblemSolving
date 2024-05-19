n = int(input())

s = []

mapp = []
dayCnt = [0 for _ in range(366)]
for _ in range(n):
    a, b = map(int, input().split())
    for k in range(a, b+1):
        dayCnt[k]+=1
    s.append((a, b))

s.sort(key=lambda x: (x[0], -x[1]))



answer = 0
row = 0
col = 0

for i in range(366):
    if dayCnt[i] !=0:
        row = max(row, dayCnt[i])
        col +=1
    else:
        answer += row * col
        row = 0
        col = 0

answer += row * col
print(answer)
