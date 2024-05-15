from collections import deque

n, k = map(int, input().split())

q = deque([])

check = {}
check[n] = True

q.append((n, str(n), 0))

while q:
    cur, route, time = q.popleft()

    if cur == k:
        print(time)
        print(route.replace(".", " "))
        break

    if cur-1 >=0 and cur-1 not in check:
        check[cur-1] = True
        nxtRoute = route+ "." + str(cur-1)
        
        q.append((cur-1, nxtRoute, time+1))
    
    if cur+1<=100000 and cur+1 not in check:
        check[cur+1] = True
        nxtRoute = route+ "." + str(cur+1)
        q.append((cur+1, nxtRoute, time+1))
    
    if 2*cur <=100000 and 2*cur not in check:
        check[cur*2] = True
        nxtRoute = route+ "." + str(2*cur)
        q.append((cur*2, nxtRoute, time+1))