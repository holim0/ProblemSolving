n = int(input())
INF = 1e10
dp = [INF for _ in range(n+1)]

value = [1]



i = 2

while True:
    curValue = value[-1] + i
    if curValue>n:
        break
    
    value.append(curValue)
    i+=1

acc = [1]
dp[1] = 1

for i in range(1, len(value)):
    nxt = acc[-1] + value[i]
    if nxt>n: break
    dp[nxt] = 1
    acc.append(nxt)


for i in range(1, n+1):
    for j in range(len(acc)):
        if acc[j]<=i:
            dp[i] = min(dp[i], dp[i-acc[j]] +1)

print(dp[n])