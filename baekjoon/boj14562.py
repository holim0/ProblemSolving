from collections import deque

c = int(input())

for _ in range(c):
    s, t = map(int, input().split())

    q = deque([])

    # visited = [False for _ in range(2*t+1)]

    # visited[s] = True

    q.append((s, t, 0))

    while q:
        myScore, targetScore, cnt = q.popleft()

        if myScore == targetScore:
            print(cnt)
            break

        nxt = myScore + 1
        if nxt<=targetScore:
            q.append((nxt, targetScore, cnt+1))
        
        nxt = 2* myScore

        if nxt <=targetScore+3 :
            q.append((nxt, targetScore+3, cnt+1))


