INF = 1e10
t = 1
while True:
    
    n = int(input())
    if n==0: break

    mapp = []

    for _ in range(n):
        row = list(map(int, input().split()))
        mapp.append(row)
    
    dp = [[INF for _ in range(3)] for _ in range(n)]

    dp[0][1] = mapp[0][1]
    dp[0][2] = dp[0][1] + mapp[0][2]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + mapp[i][0]
        dp[i][1] = min(min(dp[i][0], dp[i-1][0]), min(dp[i-1][1], dp[i-1][2])) + mapp[i][1]
        dp[i][2] = min(min(dp[i][1], dp[i-1][1]), dp[i-1][2]) + mapp[i][2]

    print(str(t) + ". " + str(dp[n-1][1]))
    t+=1