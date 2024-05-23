n, x = map(int, input().split())

visit = list(map(int, input().split()))

acc = [visit[0]]

for i in range(1, len(visit)):
    acc.append(acc[-1]+visit[i])


answer = 0
lenCnt = 0
for i in range(0, n-x+1):
    curCnt = 0

    if i==0:
        curCnt = acc[i+x-1]
    else:
        curCnt = acc[i+x-1] - acc[i-1]

    if curCnt > answer:
        answer = curCnt
        lenCnt = 1
    elif curCnt == answer:
        lenCnt+=1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(lenCnt)