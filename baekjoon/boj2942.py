r, g = map(int, input().split())

def gcd(a, b):
 
    while b>0:
        a, b = b, a%b
    return a

gcdValue = gcd(r, g)

answer = []

for i in range(1, int(gcdValue**(1/2))+1):
    if gcdValue % i ==0:
        answer.append((i, r//i, g//i))
        rest = gcdValue//i
        if rest != i:
            answer.append((rest, r//rest, g//rest))


for a in answer:
    i, j, k = a
    print(i, j, k)

    