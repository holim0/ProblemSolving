from collections import deque

n = int(input())

stone = list(map(int, input().split()))

start = int(input())

start = start - 1

visited = [False for _ in range(n)]

visited[start] = True

q = deque([])
q.append(start)

answer = 0

while q:
    cur = q.popleft()
    answer+=1

    value = stone[cur]

    if cur + value < n and not visited[cur+value]:
        visited[cur+value] = True
        q.append(cur+value)
    
    if cur - value >=0 and not visited[cur-value]:
        visited[cur-value] = True
        q.append(cur-value)


print(answer)