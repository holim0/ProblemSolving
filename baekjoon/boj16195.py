import sys
input = sys.stdin.readline

MOD = 1000000009
t = int(input())

dp = [[0 for _ in range(1001)] for _ in range(1001)]

dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

for curNum in range(4, 1001):
    for useCnt in range(1, 1001):
        dp[curNum][useCnt] = (dp[curNum-1][useCnt-1] + dp[curNum-2][useCnt-1] +dp[curNum-3][useCnt-1]) % MOD




for _ in range(t):
    n, m = map(int, input().split())
    cur = dp[n]
    cur = cur[:m+1]
    print(sum(cur) % MOD)