import sys
tc = int(input())

INF = 1e10

for _ in range(tc):
    n, m, w = map(int, input().split())

    dist = [INF] * (n+1)
    g = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        g.append((a, b, c))
        g.append((b, a, c))
    
    for _ in range(w):
        a, b, c = map(int, input().split())
        g.append((a, b, -c))
    
    
    def bf(start):
        dist = [0] * (n+1)
       
        for i in range(1, n+1):
            for j in range(len(g)):
                fromm, to, cost = g[j]

                if dist[to] > dist[fromm] + cost:
                    dist[to] = dist[fromm] + cost

                    if i == n:
                        return True 
        
        return False
    
    if bf(1):
        print("YES")
    else:
        print("NO")
    # for i in range(1, n+1):
    #     if(bf(i)):
    #         print("YES")
    #         sys.exit()
    
    # print("NO")
    





