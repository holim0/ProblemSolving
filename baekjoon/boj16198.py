n = int(input())

ball = list(map(int, input().split()))

answer= 0


def getSol(curBall, curSum):
    global answer
    if len(curBall)==2:
        answer = max(answer, curSum)
        return 
    
    nextBall =[]

    for i in range(1, len(curBall)-1):
        nextBall = []
        before, after = curBall[i-1], curBall[i+1]
        for j in range(0, len(curBall)):
            if j!=i:
                nextBall.append(curBall[j])
        
        getSol(nextBall, curSum+ (before * after))
            





getSol(ball, 0)

print(answer)