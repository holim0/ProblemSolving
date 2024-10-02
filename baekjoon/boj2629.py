n = int(input())

info = list(map(int, input().split()))
w_sum = sum(info)

m = int(input())

target = list(map(int, input().split()))

dp = [False for _ in range(40001)]

dp[0] = True

for i in range(n):

