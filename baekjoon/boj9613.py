t = int(input())


def gcd(a, b):
    if a % b ==0:
        return b
    elif b==0:
        return a
    else:
        return gcd(b, a%b)

for _ in range(t):
    l = list(map(int, input().split()))

    cnt = l[0]
    answer = 0
    for i in range(1, len(l)-1):
        for j in range(i+1, len(l)):
            answer+= gcd(l[i], l[j])

    print(answer)