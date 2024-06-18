n = int(input())

curSum = 1
f = [1, ]

plus = 2
while f[-1]<=n:

    nxt = f[-1] + plus
    f.append(nxt)
    curSum+=nxt
    plus+=1



acc = [f[0], ]

for i in range(1, len(f)):
    acc.append(acc[-1]+f[i])

INF = 1e10
dp = [INF for _ in range(n+1)]

for a in acc:
    if a<=n:
        dp[a] = 1

for i in range(1, n+1):
    for j in range(len(acc)):
        cur = acc[j]
        if i>=cur:
            dp[i] = min(dp[i], dp[i-cur]+dp[cur])


print(dp[n])