n = int(input())

first = list(map(int, input().split()))

grow = list(map(int, input().split()))

pair = []

for i in range(n):
    pair.append((grow[i], first[i]))

pair = sorted(pair)

answer = 0

for i in range(n):
    g, f = pair[i]
    answer+= f + g * i
print(answer)
