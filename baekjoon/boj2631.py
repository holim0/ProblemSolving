n = int(input())

people = []

for _ in range(n):
    cur = int(input())
    people.append(cur)

dp = [1 for _ in range(n)]



for i in range(1, n):
    for j in range(0, i):
        if people[i]>people[j]:
            dp[i] = max(dp[i], dp[j]+1)

        

print(n-max(dp))