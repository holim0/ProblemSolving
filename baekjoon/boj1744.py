n = int(input())

plus = []
minus = []

for _ in range(n):
    num = int(input())
    if num<=0:
        minus.append(num)
    else:
        plus.append(num)
plus = sorted(plus, reverse=True)
minus = sorted(minus)

answer = 0


for i in range(0, len(plus)-1, 2):
    a, b = plus[i], plus[i+1]
    answer+= max(a*b, a+b)

if len(plus)%2 !=0:
    answer+=plus[-1]



for i in range(0, len(minus)-1, 2):
    a, b = minus[i], minus[i+1]
    answer+= (a*b)

if len(minus)%2 !=0:
    answer+=minus[-1]

print(answer)
