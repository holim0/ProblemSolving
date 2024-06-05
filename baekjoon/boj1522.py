s = input()

aCnt = 0

for ss in s:
    if ss=="a":
        aCnt+=1

size = len(s)

searchStr = s+s
answer = 1e10
for i in range(0, size):
    curStr = searchStr[i:i+aCnt]
    bCnt = 0

    for cur in curStr:
        if cur=="b": bCnt+=1
    
    answer =min(answer, bCnt)

print(answer)

