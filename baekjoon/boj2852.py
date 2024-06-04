n = int(input())

one = 0
two = 0

one_winning_time = 0
two_winning_time =0

goal = []

for _ in range(n):
    team, time = input().split()

    time = int(time.split(":")[0]) * 60 + int(time.split(":")[1])

    goal.append((time, int(team)))

goal.sort()

stack = []
curWinningTeam = -1
curWinningStartTime = 0

for i in range(len(goal)):
    curGoalTime, curTeam = goal[i]

    if curTeam ==1:
        one+=1
    else:
        two+=1
    
    if curWinningStartTime ==0 and curWinningTeam == -1:
            curWinningTeam = curTeam
            curWinningStartTime = curGoalTime
            continue

    if one>two:
        if curWinningTeam == 2 and curWinningStartTime !=-1:
            two_winning_time += (curGoalTime - curWinningStartTime)
            curWinningTeam = 1
            curWinningStartTime = curGoalTime
            continue
            
        
    

    elif one<two:
        if curWinningTeam == 1 and curWinningStartTime !=-1:
            one_winning_time += (curGoalTime - curWinningStartTime)
            curWinningTeam = 2
            curWinningStartTime = curGoalTime
            continue

    elif one==two:
        if curWinningTeam != -1:
            if curWinningTeam ==1:
                one_winning_time+= (curGoalTime-curWinningStartTime)
                
            else:
                two_winning_time+= (curGoalTime-curWinningStartTime)

        curWinningTeam = -1
        curWinningStartTime = 0
    

if curWinningTeam != -1 and curWinningStartTime !=0:
    if curWinningTeam ==1:
        one_winning_time+= (48*60) - curWinningStartTime
    else:
        two_winning_time+= (48*60) - curWinningStartTime


def genTime(time):

    hour = str(time//60)
    if len(hour)==1:
        hour = "0"+hour
    
    minute = str(time%60)
    if len(minute) ==1:
        minute = "0"+minute

    return hour+":"+minute


one_time = genTime(one_winning_time)
two_time = genTime(two_winning_time)

print(one_time)
print(two_time)