import sys
input = sys.stdin.readline
t = int(input())

MAX=1000000

dp = [1] * 1000001

dp[1] = 1

for i in range(2, MAX+1):
    j=1
    while i*j<=MAX:
        dp[i*j]+=i
        j+=1

acc = [0, 1]

for i in range(2, MAX+1):
    acc.append(acc[-1] + dp[i])

for _ in range(t):
    n = int(input())
    print(acc[n])