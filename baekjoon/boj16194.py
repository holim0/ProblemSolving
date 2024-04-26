n = int(input())

card = list(map(int, input().split()))
card.insert(0, 0)
answer = max(card)

INF = 1e10

dp = [INF for _ in range(n+1)]

dp[0] = 0
dp[1] = card[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j]+ card[j])


print(dp[n])