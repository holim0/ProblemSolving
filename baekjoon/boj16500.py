import sys
s = input()

n = int(input())

a = []

for _ in range(n):
    word = input()
    a.append(word)

dp = [0 for _ in range(len(s))]

if s[0] in a:
    dp[0] = 1

for i in range(len(s)):
    for j in range(0, i):
        str2 = s[j+1:i+1]
        if dp[j] == 1 and str2 in a:
            dp[i] = 1
        if s[:i+1] in a:
            dp[i] = 1

print(dp[len(s)-1])
        
