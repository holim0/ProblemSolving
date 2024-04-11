import sys
input = sys.stdin.readline

n = int(input())

info = []

for _ in range(n):
    t, p = map(int, input().split())
    info.append((t, p))

dp = [0 for _ in range(n+1)]

k = 0
for i in range(n):
    k = max(k, dp[i])
    t, p = info[i]

    if i + t >n: continue

    nxt = i+t

    dp[nxt] = max(dp[nxt], p + k)

print(max(dp))