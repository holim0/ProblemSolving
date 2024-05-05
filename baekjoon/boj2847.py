n = int(input())

answer = 0

score = []

for _ in range(n):
    s = int(input())
    score.append(s)

for i in range(n-1, 0, -1):
    cur = score[i]
    pre = score[i-1]

    if pre>=cur:
        answer += (score[i-1] - (cur-1))
        score[i-1] = cur - 1

print(answer)
        