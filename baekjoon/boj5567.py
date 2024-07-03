from collections import deque
n = int(input())
m = int(input())

g = {}

answer = 0
for _ in range(m):
    a, b = map(int, input().split())
    
    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)

    if b not in g:
        g[b] = [a]
    else:
        g[b].append(a)


check =[False] * (n+1)
q = deque([])
q.append((1, 0))
check[1] = True

while q:
    cur, depth = q.popleft()

    if cur != 1 and depth<=2:
        answer+=1

    if cur not in g:
        continue

    for nxt in g[cur]:
        if not check[nxt]:
            check[nxt] = True
            q.append((nxt, depth+1))

print(answer)