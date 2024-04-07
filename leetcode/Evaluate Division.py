from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nope = float(-1)
        answer = []

        g = {}
        visited = {}
        for i in range(len(equations)):
            a, b = equations[i]
            if a not in visited: visited[a] = False
            if b not in visited: visited[b] = False

            if a not in g:
                g[a] = [(b, values[i])]
            else:
                g[a].append((b, values[i]))

            if b not in g:
                g[b] = [(a, 1/values[i])]
            else:
                g[b].append((a, 1/values[i]))

        
        for i, j in queries:
            if i not in g or j not in g:
                answer.append(nope)
            else:
                for value in visited: visited[value] = False
                q = deque([(i, 1)])
                visited[i] = True
                answer_value = float(-1)
                while q:
                    cur, cur_value = q.popleft()
                    if cur == j:
                        answer_value = cur_value
                        break
                    if cur not in g: continue

                    for nxt, mul in g[cur]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append((nxt, cur_value * mul))

                answer.append(answer_value)
        
        return answer