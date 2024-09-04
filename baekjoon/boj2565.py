n = int(input())
info = []

for _ in range(n):
    a, b = map(int, input().split())
    info.append((a, b))

info.sort()

dp = [1 for _ in range(n)]

dp[0] = 1
maxLen = 0
for i in range(1, n):
    curFrom, curTo = info[i]
    for j in range(0, i):
        prevFrom, prevTo = info[j]
        if prevTo < curTo:
            dp[i] = max(dp[i], dp[j]+1)
            maxLen = max(dp[i], maxLen)

print(n-maxLen)
