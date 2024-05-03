n, m = map(int, input().split())

max_score = -1
target = 0
score = list(map(int, input().split()))

for _ in range(m):
    cur = list(input().split())
    number = int(cur[0])
    cur_score = 0
    for i in range(1, n+1):
        if cur[i] == "O":
            cur_score += score[i-1]
    
    if max_score < cur_score:
        max_score = cur_score
        target = number

    elif max_score == cur_score:
        if target>number:
            target = number

print(target, max_score)