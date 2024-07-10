from collections import deque

t = int(input())

for _ in range(t):

    n = int(input())
    answer = n
    like = list(map(int, input().split()))
    like.insert(0, 0)

    degree =[0 for _ in range(n+1)]

    for i in range(1, n+1):
        fromm, to = i, like[i]
        degree[to]+=1

    start = []

    for i in range(1, n+1):
        if degree[i]==0:
            start.append(i)

    for i in range(len(start)):
        curValue = start[i]
        q = deque([])
        q.append(curValue)

        while q:
            cur = q.popleft()

            nxt = like[cur]

            degree[nxt]-=1

            if degree[nxt]==0:
                q.append(nxt)
    cnt =0
    for i in range(1, n+1):
        if degree[i]==1:
            cnt+=1
    
    answer-=cnt
    print(answer)
            
            



