n = int(input())
cost = list(map(int, input().split()))
m = int(input())

dp = [-1 for _ in range(51)]
answer = 0
for i in range(len(cost)):
    c = cost[i]
    dp[c] = i

for i in range(1, m+1):
    answer = max(answer, dp[i])


minCost = min(cost)

for curMoney in range(minCost, m+1):

    for i in range(1, curMoney):
        if curMoney-i>0 and dp[i] !=-1 and dp[curMoney-i] != -1:
            v1 = str(dp[i]) + str(dp[curMoney-i])
            v1 = "".join(sorted(v1, reverse=True))
            v1 = int(v1)

            dp[curMoney] = max(dp[curMoney], v1)
            answer = max(answer, dp[curMoney])
print(answer)