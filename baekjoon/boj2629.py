n = int(input())

info = list(map(int, input().split()))
w_sum = sum(info)

m = int(input())

target = list(map(int, input().split()))

dp = [[False] *40001 for _ in range(n)]

dp[0][0] = True

for i in range(n):
    dp[i][info[i]] = True
    for w in range(1, w_sum+1):
        if dp[i-1][w]:
            dp[i][w] = True
            dp[i][info[i]+w] = True
            dp[i][abs(info[i]-w)] = True
    

for t in target:
    if dp[n-1][t]:
        print("Y", end=" ")
    else:
        print("N", end= " ")