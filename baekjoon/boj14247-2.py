n = int(input())

l = list(map(int, input().split()))
grow = list(map(int, input().split()))

total = []

for i in range(n):
    total.append((grow[i], l[i]))

answer = 0

total = sorted(total)

for i in range(len(total)):
    gg, ll = total[i]

    answer += (ll + gg*i)

print(answer)