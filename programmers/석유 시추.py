from collections import deque
def solution(land):
    answer = 0
    
    colSize = len(land[0])
    rowSize = len(land)
    visited = [[False] * colSize for _ in range(rowSize)]
    isLandNumber = 0
    oil = [0 for _ in range(colSize)]
    for i in range(0, colSize):
        
        for j in range(rowSize):
            if land[j][i] == 1 and not visited[j][i]:
                q = deque([])
                cnt = 0
                q.append((j, i))
                visitRow = set()
                visited[j][i] = True
                while q:
                    cx, cy = q.popleft()
                    cnt+=1
                    visitRow.add(cy)
                    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nx, ny = cx+a, cy+b
                        
                        if 0<=nx<rowSize and 0<=ny<colSize and not visited[nx][ny] and land[nx][ny] ==1:  
                            visited[nx][ny] = True
                            q.append((nx, ny))
                
                
                
                for v in visitRow:
                    oil[v] += cnt
                    
        
        
    answer = max(oil)
    return answer