n = int(input())

abil = list(map(int, input().split()))

answer = 0

abil = sorted(abil)

for i in range(n-2):
    first = abil[i]

    p1, p2 = i+1, n-1

    while p1<p2:

        sum = abil[p1] + abil[p2]

        if sum == -first:
            if abil[p1] == abil[p2]:
                answer += ((p2-p1+1) * (p2-p1))//2
                break
            else:    
                curP1 = p1
                curP2 = p2
                lc, rc =0, 0
                while abil[curP1] == abil[p1] and curP1<p2:
                    lc+=1
                    curP1+=1
                while abil[curP2] == abil[p2] and curP2>p1:
                    rc+=1
                    curP2 -=1
                answer += (lc * rc)
            
                p1 = curP1
                p2 = curP2

        elif sum < -first:
            p1+=1
    
        else:
            p2-=1

print(answer)