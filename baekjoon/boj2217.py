n = int(input())

rope = []

for _ in range(n):
    r = int(input())
    rope.append(r)



rope = sorted(rope, reverse=True)
answer = 0

for i in range(len(rope)):
    answer = max(answer, rope[i] * (i+1))

print(answer)



