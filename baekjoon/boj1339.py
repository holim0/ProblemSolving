n = int(input())

alpha = {}

word =[]
answer = 0

for _ in range(n):
    w = input().rstrip()
    word.append(w)
    for i in range(len(w)):
        cur = w[i]
        if cur not in alpha:
            alpha[cur] = pow(10, len(w)-i-1)
        else:
            alpha[cur]+=pow(10, len(w)-i-1)

value = []

for key in alpha:
    value.append(alpha[key])
value.sort(reverse=True)

mul = 9

for i in range(len(value)):
    answer+= (value[i] * mul)
    mul-=1

print(answer)