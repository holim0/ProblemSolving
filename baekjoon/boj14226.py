from collections import deque
s = int(input())

q = deque([])

q.append((1, 0, 0))

check = [[False for _ in range(s+1)] for _ in range(s+1)]
check[1][0] = True

while q:
    curCnt, clipboardCnt, time = q.popleft()
    
    if curCnt == s:
        print(time)
        break

    # 복사
    if curCnt >0 and not check[curCnt][curCnt]:
        check[curCnt][curCnt] = True
        q.append((curCnt, curCnt, time+1))
    
    

    if clipboardCnt>0 and curCnt+clipboardCnt<=s and not check[curCnt+clipboardCnt][clipboardCnt]:
        check[curCnt+clipboardCnt][clipboardCnt] = True
        q.append((curCnt+clipboardCnt, clipboardCnt, time+1))
    
    if curCnt > 1 and not check[curCnt-1][clipboardCnt]:
        check[curCnt-1][clipboardCnt] = True
        q.append((curCnt-1, clipboardCnt, time+1))
  
