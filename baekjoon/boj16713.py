n, q = map(int, input().split())
 
num = list(map(int, input().split()))

acc = []

for i in range(len(num)):
    if i==0:
        acc.append(num[i])
    else:
        acc.append(acc[-1] ^ num[i])

answer = []

for _ in range(q):
    s, e = map(int, input().split())
    s, e = s-1, e-1

    if s==0:
        answer.append(acc[e])
    else:
        answer.append(acc[e] ^ acc[s-1])

for i in range(1, len(answer)):
    answer[i] = answer[i] ^ answer[i-1]

print(answer[-1])