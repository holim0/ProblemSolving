n = int(input())

w = list(map(int, input().split()))
w_sum = sum(w)
m = int(input())
MAX = 40001
target = list(map(int, input().split()))

dp = [[False] * MAX for _ in range(n)]

dp[0][0] = True

for i in range(n):
    dp[i][w[i]] = True

    for weight in range(1, w_sum+1):
        if dp[i-1][weight]:
            dp[i][weight] = True
            dp[i][weight+w[i]] = True
            dp[i][abs(weight-w[i])] = True



for t in target:
    if dp[n-1][t]:
        print("Y", end=" ")
    else:
        print("N", end= " ")