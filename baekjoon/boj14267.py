n, m = map(int, input().split())

boss = list(map(int, input().split()))
boss.insert(0, 0)
say = []

score = [0 for _ in range(n+1)]
for _ in range(m):
    i, w = map(int, input().split())
    score[i]+=w


for i in range(2, n+1):
    score[i] += score[boss[i]]
score = score[1:]
answer = " ".join(str(s) for s in score)

print(answer)





