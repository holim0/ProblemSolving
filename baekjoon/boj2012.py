n = int(input())

order = [0, ]

for _ in range(n):
    o = int(input())
    order.append(o)

order.sort()


answer = 0

for i in range(1, n+1):
    answer+= abs(i-order[i])

print(answer)