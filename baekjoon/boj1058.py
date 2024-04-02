from collections import deque
n = int(input())

g = {}



for i in range(n):
    s = input()
    s = list(s)
    for j in range(n):
        if s[j] == "N": continue
        if i not in g:
            g[i] = [j]
        else:
            g[i].append(j)
        
        


answer = 0

for i in range(n):
    visited = [False] * n
    if not visited[i]:
        visited[i] = True
        q = deque([])
        q.append((i, 0))
        cnt = 0
        while q:
            cur, curCnt = q.popleft()
            if cur not in g: continue
            for fr in g[cur]:
                if not visited[fr]:
                    if curCnt+1 <=2:
                        visited[fr] = True
                        cnt+=1
                        q.append((fr, curCnt+1))

        answer =max(answer, cnt)
        

print(answer)