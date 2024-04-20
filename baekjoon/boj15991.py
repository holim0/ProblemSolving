t = int(input())

MOD = 1000000009

dp = [0 for _ in range(100001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2

for curNum in range(4, 100001):
    if curNum-2 >=0:
        dp[curNum] += dp[curNum-2]
    
    if curNum-4>=0:
        dp[curNum] += dp[curNum-4]

    if curNum-6>=0:
        dp[curNum] += dp[curNum-6]
    dp[curNum] %= MOD

for _ in range(t):
    number = int(input())
    print(dp[number] % MOD)
    
        
        
    