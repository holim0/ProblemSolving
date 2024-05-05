import sys
sys.setrecursionlimit(100000)
n = int(input())

number = list(map(int, input().split()))

answer = 1e10

def isValid(curNumber):

    for i in range(len(curNumber)-2):
        if curNumber[i] - curNumber[i+1] != curNumber[i+1] - curNumber[i+2]:
            return False
        
    return True


def solve(curIdx, preNumber, operCnt, curDiff):
    global answer
    if operCnt >= answer: return 
    if curIdx == n:
        answer = min(operCnt, answer)
        return 
    
    
    if curDiff == number[curIdx] - preNumber:
        solve(curIdx+1, number[curIdx], operCnt, curDiff)
    if curDiff == number[curIdx]+1 - preNumber:
        solve(curIdx+1, number[curIdx]+1, operCnt+1, curDiff)
    if curDiff == number[curIdx]-1 - preNumber:
        solve(curIdx+1, number[curIdx]-1, operCnt+1, curDiff)

if n <=2:
    print(0)
    sys.exit(0)
else:
    solve(2, number[1], 0, number[1]-number[0])
    solve(2, number[1]+1, 1, number[1]+1-number[0])
    solve(2, number[1]-1, 1, number[1]-1-number[0])
    solve(2, number[1], 1, number[1]-(number[0]+1))
    solve(2, number[1], 1, number[1]-(number[0]-1))
    solve(2, number[1]-1, 2, number[1]-1-(number[0]-1))
    solve(2, number[1]-1, 2, number[1]-1-(number[0]+1))
    solve(2, number[1]+1, 2, number[1]+1-(number[0]-1))
    solve(2, number[1]+1, 2, number[1]+1-(number[0]+1))

if answer == 1e10:
    print(-1)
else:
    print(answer)

