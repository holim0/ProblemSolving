n, m = map(int, input().split())

ab = list(map(int, input().split()))

ab = sorted(ab)

p1, p2 = 0, len(ab)-1
answer = 0
while p1 < p2:

    s = ab[p1] + ab[p2]

    if s>=m:
        answer+=1
        p1+=1
        p2-=1

    else:
        p1+=1

print(answer)