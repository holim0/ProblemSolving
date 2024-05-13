n = int(input())

task = [0 for _ in range(n+1)]

score = 0
stack = []
for i in range(1, n+1):
    l = list(map(int, input().split()))

    if l[0]==1:
        if l[2]-1 ==0:
            score+=l[1]
        else:
            stack.append((l[1], l[2]-1))
    else:
        if stack:
            a, b = stack[-1]
            b-=1
            if b<=0:
                score+=a
                stack.pop()
            else:
                stack.pop()
                stack.append((a, b))

print(score)
