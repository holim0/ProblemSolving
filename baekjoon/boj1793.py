dp = [0 for _ in range(251)]
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, 251):
    dp[i] += dp[i-1]
    dp[i] += (dp[i-2] * dp[2]) - dp[i-2]
    

while True:

    try:
        n = int(input())
        print(dp[n])


    except EOFError:
        break